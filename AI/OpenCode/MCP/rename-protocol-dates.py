#!/usr/bin/env python3
"""Rename protocol files from DD-MM-YYYY to YYYY-MM-DD and update all links."""

import os, re, shutil

VAULT = "/Users/sergeysklabovskiy/Obsidian/Sergey's Vault"
PROTOCOL_DIRS = [
    "Работа/Astra/Встречи/Протоколы встреч",
    "Работа/Astra/Встречи/Синки с ИБ",
]

# Rename also the retro file
EXTRA_FILES = [
    os.path.join(VAULT, "Работа/Astra/Встречи/Протоколы встреч", "Ретро релиза ACP 2026-07-09.md"),
]

def parse_dd_mm_yyyy(filename):
    """Try to parse DD-MM-YYYY or DD.MM.YYYY at start of filename."""
    m = re.match(r'(\d{2})[-.](\d{2})[-.](\d{4})(.*)', filename)
    if m:
        return f"{m.group(3)}-{m.group(2)}-{m.group(1)}{m.group(4)}"
    # Try retro format: ... DD.MM.YYYY.md
    m = re.search(r'(\d{2})\.(\d{2})\.(\d{4})', filename)
    if m:
        old_date = f"{m.group(2)}.{m.group(1)}.{m.group(3)}" if False else m.group(0)
        return filename.replace(m.group(0), f"{m.group(3)}-{m.group(2)}-{m.group(1)}")
    return None

# Step 1: collect all renames
renames = []

for d in PROTOCOL_DIRS:
    base = os.path.join(VAULT, d)
    if not os.path.isdir(base):
        continue
    for root, dirs, files in os.walk(base):
        for f in files:
            if not f.endswith('.md'):
                continue
            new_name = parse_dd_mm_yyyy(f)
            if new_name and new_name != f:
                renames.append((os.path.join(root, f), os.path.join(root, new_name), os.path.splitext(f)[0], os.path.splitext(new_name)[0]))

for f in EXTRA_FILES:
    if os.path.exists(f):
        new_name = parse_dd_mm_yyyy(os.path.basename(f))
        if new_name:
            renames.append((f, os.path.join(os.path.dirname(f), new_name), os.path.splitext(os.path.basename(f))[0], os.path.splitext(new_name)[0]))

print(f"=== Renaming {len(renames)} files ===")

# Step 2: build old→new link mapping
link_map = {}
for old_path, new_path, old_stem, new_stem in renames:
    link_map[old_stem] = new_stem
    print(f"  {old_stem}.md → {new_stem}.md")

# Step 3: rename files
for old_path, new_path, _, _ in renames:
    if os.path.exists(new_path):
        print(f"  SKIP (exists): {os.path.basename(new_path)}")
        continue
    os.rename(old_path, new_path)
    print(f"  RENAMED: {os.path.basename(new_path)}")

# Step 4: update all links across the vault
print("\n=== Updating links ===")
link_patterns = []
for old_stem, new_stem in sorted(link_map.items(), key=lambda x: -len(x[0])):
    link_patterns.append((old_stem, new_stem))

files_updated = 0
links_found = 0
for root, dirs, files in os.walk(VAULT):
    rel = os.path.relpath(root, VAULT)
    if '.git' in rel or 'node_modules' in rel:
        continue
    for f in files:
        if not f.endswith('.md') and not f.endswith('.py'):
            continue
        path = os.path.join(root, f)
        try:
            with open(path, 'r', encoding='utf-8') as fh:
                content = fh.read()
        except:
            continue

        new_content = content
        changed = False
        for old_stem, new_stem in link_patterns:
            # Replace [[DD-MM-YYYY ...]] patterns with [[YYYY-MM-DD ...]]
            # Handle: [[DD-MM-YYYY Title]] or [[DD-MM-YYYY Title|alias]]
            old_pattern = old_stem.replace('(', r'\(').replace(')', r'\)').replace('[', r'\[')
            pattern = re.escape(old_stem)
            count = 0
            new_content, count = re.subn(pattern, new_stem, new_content)
            if count > 0:
                changed = True
                links_found += count

        if changed:
            with open(path, 'w', encoding='utf-8') as fh:
                fh.write(new_content)
            files_updated += 1
            print(f"  {os.path.relpath(path, VAULT)}")

print(f"\nUpdated {files_updated} files, {links_found} links replaced")
print("Done!")
