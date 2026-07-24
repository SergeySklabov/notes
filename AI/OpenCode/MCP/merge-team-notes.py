#!/usr/bin/env python3
"""Merge Работа/Astra/Команда/Команда Платформы AC/* into Работа/Astra/Команда/Команда Платформы AC/
and update all internal links across the vault."""

import os, re, unicodedata, shutil

VAULT = "/Users/sergeysklabovskiy/Obsidian/Sergey's Vault"
OLD_DIR = os.path.join(VAULT, "Работа/Astra/Команда/Коллеги")
NEW_DIR = os.path.join(VAULT, "Работа/Astra/Команда/Команда Платформы AC")
OLD_PREFIX = "Работа/Astra/Команда/Команда Платформы AC/"
NEW_PREFIX = "Работа/Astra/Команда/Команда Платформы AC/"

def normalize(name):
    """Normalize Unicode and strip [X] suffix."""
    n = unicodedata.normalize('NFC', name)
    n = re.sub(r'\s*\[X\]\s*', '', n).strip()
    return n

def name_to_key(name):
    """Convert filename to a set of name parts for matching."""
    base = os.path.splitext(name)[0]
    base = normalize(base)
    parts = [p.strip() for p in re.split(r'[\s,]+', base) if p.strip()]
    parts_lower = [p.lower() for p in parts]
    return frozenset(parts_lower), parts

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def delete_file(path):
    if os.path.exists(path):
        os.remove(path)

def has_meaningful_content(content):
    """Check if a note has tasks or meaningful text beyond template."""
    lines = content.strip().split('\n')
    # Skip pure template files (empty tasks, no sync notes)
    meaningful = False
    for l in lines:
        s = l.strip()
        if s.startswith('- [') and not s.endswith('_Пока нет записей_'):
            meaningful = True
        if s.startswith('### ') and 'Пока нет' not in s:
            meaningful = True
    return meaningful

# Step 1: Build index of existing Команда Платформы AC files
existing_new = {}
for fname in os.listdir(NEW_DIR):
    if not fname.endswith('.md'):
        continue
    key, parts = name_to_key(fname)
    existing_new[key] = (fname, parts)

# Step 2: Process each Коллеги file
colleghi_files = [f for f in os.listdir(OLD_DIR) if f.endswith('.md')]
moved = 0
created = []
appended = []
is_x = []

for fname in sorted(colleghi_files):
    old_path = os.path.join(OLD_DIR, fname)
    content = read_file(old_path)
    key, parts = name_to_key(fname)
    is_former = '[X]' in fname
    base_no_ext = os.path.splitext(fname)[0]

    if is_former:
        is_x.append((fname, content))
        continue

    if not has_meaningful_content(content):
        continue

    # Find matching existing file
    match = existing_new.get(key)
    if match:
        new_fname, new_parts = match
        new_path = os.path.join(NEW_DIR, new_fname)
        existing_content = read_file(new_path)

        # Merge: append content from Коллеги that isn't already in the target
        merged = existing_content
        if content not in existing_content:
            merged = existing_content.rstrip() + '\n\n<!-- merged from Коллеги -->\n\n' + content
        write_file(new_path, merged)
        appended.append((fname, new_fname))
    else:
        # Create new file in Команда Платформы AC
        new_fname = normalize(fname)
        new_path = os.path.join(NEW_DIR, new_fname)
        write_file(new_path, content)
        created.append((fname, new_fname))

print("=== Files created (new) ===")
for old, new in created:
    print(f"  {old} → {new}")

print("\n=== Files appended (merged) ===")
for old, new in appended:
    print(f"  {old} → {new}")

print(f"\n=== Skipped ([X] former) ===")
for fname, _ in is_x:
    print(f"  {fname}")

# Step 3: Update all links across the vault
print("\n=== Updating links ===")
link_pattern = re.compile(r'(\.md|/Команда Платформы AC/)')

# Find all files that reference old Коллеги paths
files_to_update = []
for root, dirs, files in os.walk(VAULT):
    rel = os.path.relpath(root, VAULT)
    if '.git' in rel or '.obsidian' in rel or 'node_modules' in rel:
        continue
    for f in files:
        if f.endswith('.md') or f.endswith('.py'):
            path = os.path.join(root, f)
            try:
                text = read_file(path)
                if OLD_PREFIX in text or OLD_PREFIX.replace('/', '\\/') in text:
                    files_to_update.append((path, text))
            except:
                pass

updates = 0
for path, text in files_to_update:
    new_text = text.replace(OLD_PREFIX, NEW_PREFIX)
    if new_text != text:
        write_file(path, new_text)
        updates += 1
        rel = os.path.relpath(path, VAULT)
        print(f"  {rel}")

print(f"\nUpdated {updates} files with link replacements")

# Step 4: Delete original Коллеги files (excluding .space/)
print("\n=== Deleting Коллеги files ===")
for fname in colleghi_files:
    old_path = os.path.join(OLD_DIR, fname)
    print(f"  DELETE: {fname}")
    delete_file(old_path)

# Try to remove directory if empty
remaining = [f for f in os.listdir(OLD_DIR) if f != '.space']
if not remaining:
    try:
        os.rmdir(OLD_DIR)
        print("\nКоллеги directory removed")
    except:
        pass

print("\nDone!")
