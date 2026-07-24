#!/bin/bash

CALENDAR_URL="https://mail.astralinux.ru/SOGo/dav/ssklabovskii@astralinux.ru/Calendar/personal.ics"
AUTH_USER="ssklabovskii@astralinux.ru"
PASS_FILE="$HOME/.config/opencode/secrets/calendar_pass"
DATE=${1:-today}

if [ ! -f "$PASS_FILE" ]; then
  echo "Ошибка: файл с паролем не найден ($PASS_FILE)"
  exit 1
fi

AUTH_PASS=$(cat "$PASS_FILE")

curl -s --max-time 10 -u "$AUTH_USER:$AUTH_PASS" "$CALENDAR_URL" -H "Accept: text/calendar" | python3 -c "
import sys, re, datetime

target = None
d = '$DATE'
if d == 'today':
    target = datetime.date.today()
elif d == 'tomorrow':
    target = datetime.date.today() + datetime.timedelta(days=1)
elif d == 'week':
    target = None
else:
    try:
        target = datetime.datetime.strptime(d, '%Y-%m-%d').date()
    except:
        target = datetime.date.today()

raw = sys.stdin.read()
if not raw.strip():
    print('Нет данных от календаря')
    sys.exit(0)

raw = re.sub(r'\r\n', '\n', raw)
unfolded = []
for line in raw.split('\n'):
    if not line:
        continue
    if line[0] in (' ', '\t') and unfolded:
        unfolded[-1] += line[1:]
    else:
        unfolded.append(line)

events = []
current = None
depth = 0

for line in unfolded:
    s = line.strip()
    if s == 'BEGIN:VEVENT':
        current = {}
        depth = 1
    elif s == 'BEGIN:VALARM':
        depth += 1
    elif s == 'END:VALARM':
        depth -= 1
    elif s == 'END:VEVENT':
        if current is not None:
            events.append(current)
        current = None
        depth = 0
    elif current is not None and depth == 1 and ':' in s:
        key, _, val = s.partition(':')
        base_key = key.split(';')[0]
        current[base_key] = val

def parse_dt(v):
    v = v.replace('Z', '')
    if 'T' in v:
        return datetime.datetime.strptime(v[:15], '%Y%m%dT%H%M%S')
    else:
        return datetime.datetime.strptime(v[:8], '%Y%m%d')

seen = []
for e in events:
    start = e.get('DTSTART', '')
    end = e.get('DTEND', '')
    summary = e.get('SUMMARY', '').strip()
    location = e.get('LOCATION', '').strip()
    desc = e.get('DESCRIPTION', '').strip()

    if not start:
        continue
    if not summary and not desc:
        continue

    try:
        dt_start = parse_dt(start)
        dt_end = parse_dt(end) if end else dt_start + datetime.timedelta(hours=1)
    except:
        continue

    event_date = dt_start.date()
    if target and event_date != target:
        continue

    dedup = f'{event_date}_{summary}_{location}'
    if dedup in seen:
        continue
    seen.append(dedup)

    time_str = ''
    if 'T' in start:
        time_str = f\"{dt_start.strftime('%H:%M')}\u2013{dt_end.strftime('%H:%M')}\"
    else:
        time_str = '\u0432\u0435\u0441\u044c \u0434\u0435\u043d\u044c'

    loc_str = f' @ {location}' if location else ''
    desc_short = (desc[:100] + '...') if len(desc) > 100 else desc
    desc_str = f' - {desc_short}' if desc_short else ''

    print(f'- [{time_str}]{loc_str} {summary}{desc_str}')

if target:
    label = target.strftime('%d.%m.%Y')
else:
    label = '\u043d\u0435\u0434\u0435\u043b\u044e'
print(f'\\n=== \u0421\u043e\u0431\u044b\u0442\u0438\u044f \u043d\u0430 {label} ===')
"