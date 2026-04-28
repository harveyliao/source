#!/usr/bin/env python3
"""Fix internal links in translated Chinese HTML files by replacing 
English filenames with their Chinese equivalents."""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAP_FILE = os.path.join(ROOT, 'docs', 'translation', 'filename-map.json')
ZH_DIR = os.path.join(ROOT, 'content', 'zh')

with open(MAP_FILE) as f:
    fmap = json.load(f)

# Also build inverse map for checking
inv_map = {v: k for k, v in fmap.items()}

def fix_links_in_file(filepath):
    with open(filepath) as f:
        content = f.read()
    
    original = content
    changed = 0
    
    # Pattern: href="...ENGLISH.html..." or src="...ENGLISH.html..."
    # Matches the full URL including optional path prefix and anchor suffix
    def replacer(m):
        nonlocal changed
        full_url = m.group(3)
        attr = m.group(1)
        quote = m.group(2)
        
        # Split into base + anchor
        anchor = ''
        if '#' in full_url:
            pos = full_url.index('#')
            anchor = full_url[pos:]
            base = full_url[:pos]
        else:
            base = full_url
        
        # Extract filename from path
        filename = os.path.basename(base)
        
        if filename in fmap and fmap[filename] != filename:
            # Reconstruct: path prefix + chinese filename + anchor
            dir_prefix = os.path.dirname(base)
            if dir_prefix:
                new_base = os.path.join(dir_prefix, fmap[filename])
            else:
                new_base = fmap[filename]
            new_url = new_base + anchor
            changed += 1
            return f'{attr}={quote}{new_url}{quote}'
        return m.group(0)
    
    content = re.sub(
        r'''(href|src)=(["'])([^"']*\.html[^"']*)\2''',
        replacer,
        content
    )
    
    if content != original:
        with open(filepath, 'w') as f:
            f.write(content)
    
    return changed

total = 0
for fname in sorted(os.listdir(ZH_DIR)):
    if fname.endswith('.html'):
        path = os.path.join(ZH_DIR, fname)
        n = fix_links_in_file(path)
        if n:
            print(f"  {fname}: {n} links fixed")
            total += n

print(f"\nTotal: {total} links fixed across all files")
