#!/usr/bin/env python3
import json, os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

TOKEN_PATH = os.path.expanduser('~/.config/opencode/secrets/jira_pat')
with open(TOKEN_PATH) as f:
    JIRA_TOKEN = f.read().strip()
BASE = "https://jira.astralinux.ru/rest/api/2/issue"
OBSIDIAN_VAULT = os.path.expanduser('/Users/sergeysklabovskiy/Obsidian/Sergey\'s Vault')
COMP_DIR = os.path.join(OBSIDIAN_VAULT, 'Работа', 'Astra', 'Astra Cloud Platform', 'Компоненты')
COLLEAGUES_DIR = os.path.join(OBSIDIAN_VAULT, 'Работа', 'Astra', 'Команда', 'Команда Платформы AC')

def load_json(path):
    with open(path) as f:
        raw = f.read()
    start = raw.find('{')
    if start == -1:
        start = raw.find('[')
    return json.loads(raw[start:])

def fetch_issue(key):
    cmd = [
        'curl', '-s',
        '-H', f'Authorization: Bearer {JIRA_TOKEN}',
        f'{BASE}/{key}?expand=changelog&fields=summary,status,assignee,updated'
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        data = json.loads(result.stdout)
        return key, data
    except:
        return key, None

# 1. Load epics
epics_data = load_json('/tmp/jira_epics_v2.json')
epics = epics_data['issues']

# 2. Assignee mapping & overrides
assignee_to_comp = {
    'Михаил Перевалов': '[SCP]',
    'Виталий Козловский': '[IAM]',
    'Максим Югай': '[TMS]'
}
epic_override = {'AIC-1816': '[TMS]'}

def get_primary_comp(ep):
    key = ep['key']
    if key in epic_override:
        return epic_override[key]
    assignee = ep['fields'].get('assignee')
    if assignee and assignee.get('displayName') in assignee_to_comp:
        return assignee_to_comp[assignee['displayName']]
    components = [c['name'] for c in ep['fields'].get('components', [])]
    if components:
        return components[0]
    return '[OTHER]'

# Folder naming (old code → display name)
comp_folder = {
    'APIM': 'API Gateway (APIM)',
    'BCKP': 'Резервное копирование (BCKP)',
    'BIL': 'Billing (BIL)',
    'CTR': 'Kubernetes (CTR)',
    'IAM': 'IAM (UIDM)',
    'MON': 'Мониторинг (MON)',
    'REP': 'REP',
    'OTHER': 'OTHER',
    'SCP': 'Личный Кабинет (SCP)',
    'SDN': 'SDN (APOS)',
    'SDS': 'Интеграция с TROK (SDS)',
    'TMS': 'Tenant (TMS)',
    'VIR': 'Брест (VIT)',
}

def get_folder_name(code):
    return comp_folder.get(code, code)

comp_owner = {
    'APIM': 'Александр Шадрин',
    'CTR': 'Александр Шадрин',
    'IAM': 'Виталий Козловский',
    'SCP': 'Михаил Перевалов',
    'TMS': 'Максим Югай',
    'VIR': 'Дмитрий Попенов',
}

# 3. Build epic info & collect all keys
all_keys = set()
comp_groups = {}
epic_info = {}

for ep in epics:
    key = ep['key']
    all_keys.add(key)
    primary_comp = get_primary_comp(ep)
    comp_groups.setdefault(primary_comp, []).append(key)
    
    # Blockers - check BOTH directions
    blockers = []
    for link in ep['fields'].get('issuelinks', []):
        lt = link.get('type', {})
        if lt.get('name') not in ('Блокада', 'Blocks'):
            continue
        # outwardIssue = this epic blocks (bloquiert)
        # inwardIssue = this epic is blocked by (ist blockiert von)
        if 'inwardIssue' in link:
            inn = link['inwardIssue']
            blockers.append({
                'key': inn['key'],
                'summary': inn['fields']['summary'],
                'status': inn['fields']['status']['name'],
                'direction': 'blocked_by'
            })
        if 'outwardIssue' in link:
            out = link['outwardIssue']
            blockers.append({
                'key': out['key'],
                'summary': out['fields']['summary'],
                'status': out['fields']['status']['name'],
                'direction': 'blocks'
            })
    
    assignee = ep['fields'].get('assignee')
    epic_info[key] = {
        'summary': ep['fields']['summary'],
        'status': ep['fields']['status']['name'],
        'blockers': blockers,
        'assignee': assignee.get('displayName', '') if assignee else ''
    }

# Collect blocker keys for fetching
blocker_keys = set()
for info in epic_info.values():
    for b in info['blockers']:
        blocker_keys.add(b['key'])
all_keys.update(blocker_keys)

# 4. Load children & collect subtask keys
children_dir = '/tmp/jira_data/'
subtask_parent = {}
subtask_data = {}

for ep in epics:
    ek = ep['key']
    cf = os.path.join(children_dir, f"{ek}_children.json")
    if os.path.exists(cf):
        cdata = load_json(cf)
        subtask_data[ek] = cdata.get('issues', [])
        for iss in cdata.get('issues', []):
            ck = iss['key']
            all_keys.add(ck)
            subtask_parent[ck] = ek

print(f"Total keys: {len(all_keys)} (epics={len(epics)}, blockers={len(blocker_keys)}, subtasks={len(subtask_parent)})", file=sys.stderr)

# 5. Fetch all keys in parallel
changelog_data = {}
with ThreadPoolExecutor(max_workers=12) as pool:
    futures = {pool.submit(fetch_issue, k): k for k in all_keys}
    for fut in as_completed(futures):
        k, data = fut.result()
        changelog_data[k] = data
        if len(changelog_data) % 30 == 0:
            print(f"  Fetched {len(changelog_data)}/{len(all_keys)}", file=sys.stderr)

print(f"Done fetching. Got {len(changelog_data)} results.", file=sys.stderr)

# 6. Helper: get current assignee from live data
def get_assignee(key):
    data = changelog_data.get(key)
    if data and 'fields' in data:
        a = data['fields'].get('assignee')
        if a:
            return a.get('displayName', '')
    return ''

# 7. Get latest change for epic group
active_statuses = {s.lower() for s in ('Backlog', 'В работе', 'In Progress', 'SELECTED FOR DEVELOPMENT', 'в работе')}

def get_change_desc(scope, key, field, from_str, to_str, author, created, changelog_data):
    try:
        dt = datetime.strptime(created.split('.')[0], '%Y-%m-%dT%H:%M:%S')
        date_str = dt.strftime('%d.%m.%Y')
    except:
        date_str = created[:10]
    
    # Get the issue summary if it's a subtask
    name = ''
    if scope == 'Подзадача':
        data = changelog_data.get(key)
        if data and 'fields' in data:
            name = data['fields'].get('summary', '')
    
    suffix = f". {scope} {key}"
    if name:
        suffix += f" {name}"
    suffix += ":"
    
    if field == 'status':
        return f"**Последнее изменение:** {date_str}{suffix} статус изменён: '{from_str}' → '{to_str}' ({author})"
    elif field == 'summary':
        return f"**Последнее изменение:** {date_str}{suffix} название изменено ({author})"
    elif field == 'assignee':
        return f"**Последнее изменение:** {date_str}{suffix} исполнитель изменён: '{from_str}' → '{to_str}' ({author})"
    else:
        return f"**Последнее изменение:** {date_str}{suffix} {field}: '{from_str}' → '{to_str}' ({author})"

def get_latest_change(epic_key):
    candidates = []
    
    def extract(key, scope):
        data = changelog_data.get(key)
        if not data or 'fields' not in data:
            return
        histories = data.get('changelog', {}).get('histories', [])
        for h in reversed(histories):
            created = h.get('created', '')
            author = h.get('author', {}).get('displayName', 'Unknown')
            items = h.get('items', [])
            for item in items:
                field = item.get('field', '')
                if field in ('status', 'summary', 'assignee', 'priority', 'components'):
                    from_s = item.get('fromString', '') or '(none)'
                    to_s = item.get('toString', '') or '(none)'
                    if from_s != to_s:
                        candidates.append((created, scope, key, field, from_s, to_s, author))
                        break
    
    extract(epic_key, 'Эпик')
    for sk, pk in subtask_parent.items():
        if pk == epic_key:
            extract(sk, 'Подзадача')
    
    if not candidates:
        return None, None
    candidates.sort(key=lambda x: x[0], reverse=True)
    created, scope, key, field, from_s, to_s, author = candidates[0]
    try:
        change_dt = datetime.strptime(created.split('.')[0], '%Y-%m-%dT%H:%M:%S')
    except:
        change_dt = None
    return get_change_desc(scope, key, field, from_s, to_s, author, created, changelog_data), change_dt

def is_epic_stale(epic_key):
    _, dt = get_latest_change(epic_key)
    if dt is None:
        return False
    return (datetime.now() - dt).days > 14

# 8. Generate individual epic files
comp_order = ['[IAM]', '[VIR]', '[SDN]', '[SCP]', '[IAAS]', '[MON]', '[SDS]', '[BCKP]', '[CTR]', '[TMS]', '[APIM]', '[BIL]', '[REP]', '[XAAS]', '[OTHER]']
all_comps = list(dict.fromkeys(comp_order + [c for c in comp_groups if c not in comp_order]))

# Collect all unique assignees
all_assignees = set()
for info in epic_info.values():
    if info['assignee']:
        all_assignees.add(info['assignee'])
for sk, pk in subtask_parent.items():
    a = get_assignee(sk)
    if a:
        all_assignees.add(a)
for info in epic_info.values():
    for b in info['blockers']:
        a = get_assignee(b['key'])
        if a:
            all_assignees.add(a)

print(f"Unique assignees: {sorted(all_assignees)}", file=sys.stderr)

# Ensure colleagues dir exists
os.makedirs(COLLEAGUES_DIR, exist_ok=True)

# Create colleague notes if missing
for name in sorted(all_assignees):
    note_path = os.path.join(COLLEAGUES_DIR, f"{name}.md")
    if not os.path.exists(note_path):
        with open(note_path, 'w') as f:
            f.write(f"# {name}\n")

# Generate files
for comp in all_comps:
    if comp not in comp_groups:
        continue
    comp_code = comp.strip('[]')
    comp_name = get_folder_name(comp_code)
    comp_dir = os.path.join(COMP_DIR, comp_name)
    os.makedirs(comp_dir, exist_ok=True)
    
    # Create component entity note
    entity_file = os.path.join(comp_dir, f"{comp_name}.md")
    if not os.path.exists(entity_file):
        with open(entity_file, 'w') as f:
            f.write(f"# {comp_name}\n")
    
    # Build ACP 2.2.0 note
    lines = []
    lines.append("---")
    lines.append("tags:")
    lines.append("  - acp/2.2.0")
    lines.append(f"  - component/{comp_code}")
    
    owner = comp_owner.get(comp_code)
    if owner:
        col_path = f"Работа/Astra/Команда/Команда Платформы AC/{owner}"
        lines.append(f'Ответственный: "[[{col_path}|{owner}]]"')
    
    entity_rel = f"Работа/Astra/Astra Cloud Platform/Компоненты/{comp_name}/{comp_name}"
    lines.append(f'Компонент: "[[{entity_rel}|{comp_name}]]"')
    lines.append("---")
    lines.append("")
    lines.append(comp_name)
    lines.append("")
    lines.append(f"# {comp_name} — ACP 2.2.0 (НОЯБРЬ 2026)")
    lines.append("")
    
    for ek in comp_groups[comp]:
        info = epic_info[ek]
        
        stale_flag = ' ❗' if is_epic_stale(ek) else ''
        lines.append(f"## [{ek}](https://jira.astralinux.ru/browse/{ek}){stale_flag} — {info['summary']}")
        lines.append("")
        lines.append(f"**Статус:** {info['status']}")
        
        live_assignee = get_assignee(ek) or info['assignee']
        if live_assignee:
            col_path = f"Работа/Astra/Команда/Команда Платформы AC/{live_assignee}"
            lines.append(f"**Ответственный:** [[{col_path}|{live_assignee}]]")
        
        lines.append("")
        
        # Subtasks
        children = []
        if ek in subtask_data:
            for iss in subtask_data[ek]:
                ck = iss['key']
                cs = iss['fields']['summary']
                cst = iss['fields']['status']['name']
                ca = get_assignee(ck)
                if cst.lower() in active_statuses:
                    icon = '🟢' if cst.lower() in ('в работе', 'in progress') else '🔵'
                    line = f"- {icon} **[{ck}](https://jira.astralinux.ru/browse/{ck})** — {cs} [{cst}]"
                    if ca:
                        col_path = f"Работа/Astra/Команда/Команда Платформы AC/{ca}"
                        line += f" — [[{col_path}|{ca}]]"
                    children.append(line)
        
        if children:
            lines.append("### Подзадачи\n")
            lines.extend(children)
        else:
            lines.append("*Нет активных подзадач*")
        
        lines.append("")
        
        # Blockers
        if info['blockers']:
            lines.append("### ⛔ Блокеры\n")
            for b in info['blockers']:
                ba = get_assignee(b['key'])
                suffix = f" — [[Работа/Astra/Команда/Команда Платформы AC/{ba}|{ba}]]" if ba else ''
                bk = b['key']
                lines.append(f"- [{bk}](https://jira.astralinux.ru/browse/{bk}) — {b['summary']} [{b['status']}]{suffix}")
            lines.append("")
        
        # Latest change
        change_text, _ = get_latest_change(ek)
        if change_text:
            lines.append(change_text)
            lines.append("")
        
        lines.append("---\n")
    
    content = '\n'.join(lines)
    filepath = os.path.join(comp_dir, "ACP 2.2.0.md")
    with open(filepath, 'w') as f:
        f.write(content)
    
    print(f"  Wrote {filepath} ({len(comp_groups[comp])} epics)", file=sys.stderr)

print("\n=== Done! ===", file=sys.stderr)
print(f"Files in {COMP_DIR}:", file=sys.stderr)
existing_dirs = set()
for comp in all_comps:
    if comp not in comp_groups:
        continue
    comp_code = comp.strip('[]')
    d = os.path.join(COMP_DIR, get_folder_name(comp_code))
    if os.path.isdir(d):
        count = len([f for f in os.listdir(d) if f.endswith('.md')])
        print(f"  {get_folder_name(comp_code)}: {count} files", file=sys.stderr)
        existing_dirs.add(d)
