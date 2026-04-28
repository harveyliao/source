#!/usr/bin/env python3
"""Generate translation prompts from glossary + extracted blocks."""

import json, sys, os

def load_glossary(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def build_glossary_section(glossary):
    lines = []
    lines.append("## Glossary — Always use these Chinese terms:")
    for en, zh in glossary.get('math_terms', {}).items():
        lines.append(f"  {en} → {zh}")
    for en, zh in glossary.get('environment_terms', {}).items():
        lines.append(f"  {en} → {zh}")
    
    lines.append("")
    lines.append("## Translation Conventions:")
    for key, rule in glossary.get('translation_conventions', {}).items():
        lines.append(f"  - {rule}")
    
    lines.append("")
    lines.append("## Special Translations (idioms/phrases):")
    for en, zh in glossary.get('special_translations', {}).items():
        lines.append(f"  {en} → {zh}")
    
    return '\n'.join(lines)

SYSTEM_PROMPT = """You are a professional Chinese translator specializing in mathematical texts.
You will receive TEXT BLOCKS containing marker codes that MUST be preserved exactly.

## Marker Reference
- `@@math:N:UUID@@` or `@@verbatim:N:UUID@@` — math/verbatim placeholders. PRESERVE EXACTLY, never modify.
- `[[tag attr="val"]]text[[/tag]]` — inline HTML markers. Meaning: `<tag attr="val">text</tag>`.
  Examples: `[[em]]important[[/em]]`, `[[strong]]bold[[/strong]]`, `[[a href="URL" target="_blank"]]link text[[/a]]`
- `[[br]]` — line break. Preserve.
- `[[img:description]]` — image placeholder. Preserve.
- Plain HTML (no [[ markers]) — also preserve exactly.

## Translation Rules
1. Translate English to natural, fluent Chinese (zh-CN).
2. PRESERVE all `@@...@@`, `[[...]]` markers and plain HTML exactly.
3. Use the glossary terms consistently.
4. Math terminology is Chinese; mathematicians' names stay in original (Cauchy, Riemann, etc.).
5. "Theorem N" → "定理 N", "Example N" → "例 N", "Figure N" → "图 N"
6. "we" → omit or use impersonal construction; "Let f be..." → "设 f 为..."
7. "if and only if" → "当且仅当"; "that is" → "即"
8. Output ONLY the translated text, no explanations."""

def main():
    if len(sys.argv) < 2:
        print("Usage: gen_prompts.py <extract.json> [glossary.json]")
        sys.exit(1)
    
    extract_path = sys.argv[1]
    glossary_path = sys.argv[2] if len(sys.argv) > 2 else 'docs/translation/glossary-zh.json'
    
    with open(extract_path, 'r', encoding='utf-8') as f:
        ext = json.load(f)
    
    glossary = load_glossary(glossary_path)
    glossary_text = build_glossary_section(glossary)
    
    # Build prompt for all blocks
    user_prompt = f"Translate these text blocks from {ext['file']}:\n\n"
    for b in ext['text_blocks']:
        user_prompt += f"[{b['id']}] <{b['tag']}>: {b['text']}\n\n"
    
    user_prompt += "\nReturn ONLY a JSON array of translated strings, one per block, in the same order."
    
    prompt = {
        "file": ext['file'],
        "num_blocks": ext['num_text_blocks'],
        "system": SYSTEM_PROMPT + '\n\n' + glossary_text,
        "user": user_prompt
    }
    
    print(json.dumps(prompt, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()
