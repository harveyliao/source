#!/usr/bin/env python3
"""
Batch translate complex-analysis HTML from content/en/ to content/zh/.
Workflow:
  1. extract  - Extract text blocks from all English files
  2. prompts  - Generate translation prompts (system + user)
  3. fill     - Apply translations from a JSON file
  4. reassemble - Reassemble all translated HTML to content/zh/

Usage:
  python3 batch_translate.py extract
  python3 batch_translate.py prompts
  python3 batch_translate.py fill translations.json
  python3 batch_translate.py reassemble
"""

import json, os, sys, subprocess, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EN_DIR = os.path.join(ROOT, 'content', 'en')
ZH_DIR = os.path.join(ROOT, 'content', 'zh')
GLOSSARY = os.path.join(ROOT, 'docs', 'translation', 'glossary-zh.json')
MAP_FILE = os.path.join(ROOT, 'docs', 'translation', 'filename-map.json')
EXTRACT_DIR = os.path.join(ROOT, 'docs', 'translation', 'extracts')
PROMPT_DIR = os.path.join(ROOT, 'docs', 'translation', 'prompts')
EXTRACTOR = os.path.join(ROOT, 'scripts', 'html_translator.py')
PROMPT_GEN = os.path.join(ROOT, 'scripts', 'gen_prompts.py')

def load_map():
    with open(MAP_FILE) as f:
        return json.load(f)

def get_en_files():
    fmap = load_map()
    return sorted([f for f in os.listdir(EN_DIR) if f.endswith('.html') and f in fmap])

def cmd_extract():
    os.makedirs(EXTRACT_DIR, exist_ok=True)
    fmap = load_map()
    files = get_en_files()
    
    for i, fn in enumerate(files):
        en_path = os.path.join(EN_DIR, fn)
        ext_path = os.path.join(EXTRACT_DIR, fn.replace('.html', '.json'))
        zh_fn = fmap[fn]
        
        print(f"[{i+1}/{len(files)}] Extracting {fn} → {zh_fn}")
        r = subprocess.run(
            ['python3', EXTRACTOR, 'extract', en_path, '-o', ext_path],
            capture_output=True, text=True, timeout=60
        )
        if r.returncode != 0:
            print(f"  ERROR: {r.stderr.strip()}")
        else:
            with open(ext_path) as f:
                ext = json.load(f)
            print(f"  {ext['num_text_blocks']} blocks, {ext['num_verbatim']} verbatim")
    
    # Save index
    index = {'files': {fn: fmap[fn] for fn in files}}
    with open(os.path.join(EXTRACT_DIR, '_index.json'), 'w') as f:
        json.dump(index, f, indent=2)

def cmd_prompts():
    os.makedirs(PROMPT_DIR, exist_ok=True)
    fmap = load_map()
    files = get_en_files()
    
    for i, fn in enumerate(files):
        ext_path = os.path.join(EXTRACT_DIR, fn.replace('.html', '.json'))
        prompt_path = os.path.join(PROMPT_DIR, fn.replace('.html', '.json'))
        
        print(f"[{i+1}/{len(files)}] {fn}")
        r = subprocess.run(
            ['python3', PROMPT_GEN, ext_path, GLOSSARY],
            capture_output=True, text=True, timeout=30
        )
        with open(prompt_path, 'w') as f:
            f.write(r.stdout)

def cmd_fill(translations_file):
    """Apply translations from a JSON file.
    Format: {"filename.html": ["translated block 0", "translated block 1", ...], ...}
    """
    with open(translations_file) as f:
        all_trans = json.load(f)
    
    fmap = load_map()
    trans_dir = os.path.join(ROOT, 'docs', 'translation', 'translations')
    os.makedirs(trans_dir, exist_ok=True)
    
    for fn, translations in all_trans.items():
        zh_fn = fmap.get(fn, fn)
        trans_path = os.path.join(trans_dir, fn.replace('.html', '.json'))
        with open(trans_path, 'w') as f:
            json.dump(translations, f, indent=2, ensure_ascii=False)
        print(f"  Wrote {len(translations)} translations for {fn}")

def cmd_reassemble():
    fmap = load_map()
    files = get_en_files()
    trans_dir = os.path.join(ROOT, 'docs', 'translation', 'translations')
    
    os.makedirs(ZH_DIR, exist_ok=True)
    
    for i, fn in enumerate(files):
        ext_path = os.path.join(EXTRACT_DIR, fn.replace('.html', '.json'))
        trans_path = os.path.join(trans_dir, fn.replace('.html', '.json'))
        zh_fn = fmap[fn]
        zh_path = os.path.join(ZH_DIR, zh_fn)
        
        if not os.path.exists(trans_path):
            print(f"[{i+1}/{len(files)}] SKIP {fn} — no translations yet")
            continue
        
        print(f"[{i+1}/{len(files)}] Reassembling {fn} → {zh_fn}")
        r = subprocess.run(
            ['python3', EXTRACTOR, 'reassemble', ext_path, trans_path, zh_path],
            capture_output=True, text=True, timeout=30
        )
        if r.returncode != 0:
            print(f"  ERROR: {r.stderr.strip()}")
        else:
            # Check for remnants
            with open(zh_path) as f:
                content = f.read()
            remnant = re.findall(r'@@\w+:\d+:[a-f0-9]+@@', content)
            if remnant:
                print(f"  WARNING: {len(remnant)} remnant placeholders")
            else:
                size = os.path.getsize(zh_path)
                print(f"  OK: {size} bytes, 0 remnants")

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    cmd = sys.argv[1]
    if cmd == 'extract':
        cmd_extract()
    elif cmd == 'prompts':
        cmd_prompts()
    elif cmd == 'fill':
        if len(sys.argv) < 3:
            print("Usage: batch_translate.py fill translations.json")
            sys.exit(1)
        cmd_fill(sys.argv[2])
    elif cmd == 'reassemble':
        cmd_reassemble()
    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
        sys.exit(1)

if __name__ == '__main__':
    main()
