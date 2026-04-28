---
name: html-translation
category: software-development
description: |
  Translate static HTML websites while preserving technical content.
  Extracts human-readable text from container tags, protects LaTeX math,
  iframes, scripts, and styles with UUID placeholders, translates via LLM,
  and reassembles with perfect structural fidelity. Stdlib-only Python.
  Use when: translating a static HTML site, localizing documentation,
  converting HTML textbooks to another language, or any HTML→HTML
  translation task where technical content must survive verbatim.
tags: [translation, html, localization, static-site, python, latex]
---

# HTML Translation Pipeline

Extract → Protect → Translate → Reassemble for static HTML websites.

## When to use

- Translating a static HTML website (documentation, textbook, blog) to another language
- HTML must stay structurally identical — only human-readable text in container tags changes
- LaTeX math, `<iframe>`, `<script>`, `<style>`, code blocks, or other technical content must survive verbatim
- Source has 10+ HTML files that need batch processing
- Environment lacks pip (stdlib-only Python required)

## Architecture

Three scripts work together:

```
html_translator.py  →  extract blocks, reassemble after translation
gen_prompts.py      →  generate LLM translation prompts from glossary + blocks
batch_translate.py  →  orchestrate all 47 files: extract → prompts → fill → reassemble
```

## Protected content (never touches the LLM)

1. **LaTeX math** — `$...$`, `$$...$$`, `\begin{...}...\end{...}`, `\(...\)`, `\[...\]`
2. **Verbatim tags** — `<iframe>`, `<script>`, `<style>`, `<pre>`, `<code>`
3. **Special directives** — `w3-include-html`, HTML comments with functional content

All protected content gets UUID placeholders (`@@math:N:UUID@@`) and is restored after translation.

## Inline HTML markers

Inline formatting tags inside translatable blocks (`<em>`, `<strong>`, `<a>`, `<span>`, etc.) are converted to markers before translation and restored after:

```
Before:  <a href="URL" target="_blank">link text</a>
Marker:  [[a href="URL" target="_blank"]]link text[[/a]]
After:   <a href="URL" target="_blank">链接文字</a>
```

This preserves ALL attributes (class, id, style, target, href) through the translation round-trip. The translator only modifies the text between `]]` and `[[/`.

**Critical:** The marker regex must be applied REPEATEDLY (loop until stable) because markers can nest:
```
[[span]]<button>[[a href="..." ...]]text[[/a]]</button>[[/span]]
```
A single-pass `re.sub` would consume the outer `[[span]]` and miss the inner `[[a]]`.

## Extraction strategy (html_translator.py)

### Containers vs leaf tags

Only **container-level** tags are extracted as translation blocks: `<p>`, `<li>`, `<h1>`-`<h6>`, `<figcaption>`, `<div class="...">`.

Do NOT extract `<em>`, `<strong>`, `<a>`, `<span>` as separate blocks — these are inline formatting handled by markers.

### Byte-position extraction

Uses regex with non-greedy matching to find opening tag + closing tag, computes exact byte positions in the raw HTML:

```python
_OPEN_RE = re.compile(
    r'<({tags})\b[^>]*>'.format(tags='|'.join(CONTAINER_TAGS)),
    re.IGNORECASE
)
```

Then `_find_closing_tag()` searches for the matching `</tag>`.

### Placeholder replacement

Uses Python list slice assignment to insert placeholders without position shifts:

```python
result = list(html)
for block in reversed(blocks):  # reverse order — earlier positions stay valid
    result[block['byte_start']:block['byte_end']] = p
return ''.join(result)
```

This is CRITICAL: string-concatenation approaches (`result[:start] + p + result[end:]`) fail because `result[end:]` points to wrong positions after modifications.

## Pitfalls

### Nested inline markers
`marker_to_html()` must loop until no more replacements occur (see above).

### Trailing whitespace before closing tags
The extractor includes whitespace between the last character and `</tag>` as part of the inner content. This whitespace gets normalized during marker processing. Identity round-trips may show 1-2 byte differences in trailing whitespace — cosmetic, does not affect rendering.

### MathJax divs inside paragraphs
Some pages have `<div class="scroll-wrapper">` inside `<p>` tags (MathJax-rendered math). These divs appear as literal HTML in translatable blocks. They're not in INLINE_TAGS and pass through to the translator. Test on math-heavy files first.

### Container tag edge cases
`<li>` tags may not have explicit closing `</li>` in the source. The regex must handle both `<li>text</li>` and `<li>text` (implicit close before next `<li>` or `</ul>`).

### Remnant placeholders from verbatim_map mismatches

Each extract JSON has a `verbatim_map` — a dict of `@@type:N:UUID@@` → original content. When writing translation JSONs manually (not via LLM that preserves the original marker UIDs you fed it), the `@@` markers inside your translated strings MUST match the keys in the extract's `verbatim_map` exactly. If they don't, `reassemble` reports "WARNING: N remnant placeholders" and leaves `@@...@@` strings in the output HTML.

There are two distinct failure modes:

**Type A — same marker count, wrong UIDs:** The translation block has the same number of `@@` markers as the extract block, but the 6-char hex UIDs don't match the verbatim_map. This happens when markers were rewritten manually (e.g., sequential UIDs like `@@math:1:000001@@` instead of the extract's hash-based UIDs). Fix: match by **position** — the n-th marker in the translation maps to the n-th marker in the extract block:
```python
tx_markers = re.findall(r'@@\w+:\d+:[a-f0-9]+@@', trans_block)
ex_markers = re.findall(r'@@\w+:\d+:[a-f0-9]+@@', ext_block)
# Replace each tx marker with the corresponding ext marker
for tx_m, ex_m in zip(tx_markers, ex_markers):
    trans_block = trans_block.replace(tx_m, ex_m, 1)
```

**Type B — different marker counts:** The translation block has fewer or more `@@` markers than the extract. This happens when the translation omitted some markers (e.g., shortened a paragraph and dropped math placeholders) or inserted extra ones. For Type B, the **entire block must be rebuilt** from the extract — start from the extract's English text with all its markers intact, and produce a fresh Chinese translation that preserves every marker exactly. Positional matching will fail here because zip() only pairs up to min(len(tx), len(ex)).

**Pre-validation before fill/reassemble:** Catch mismatches early by comparing all translation JSONs against their extracts:
```python
import json, re, os

for fname in os.listdir(trans_dir):
    with open(f'{extracts_dir}/{fname}') as f: ext = json.load(f)
    with open(f'{trans_dir}/{fname}') as f: trans = json.load(f)
    valid_uids = {k.split(':')[-1].rstrip('@') for k in ext['verbatim_map']}
    for i, block in enumerate(trans):
        for m in re.finditer(r'@@(\w+:\d+:[a-f0-9]+)@@', block):
            if m.group(1).split(':')[-1] not in valid_uids:
                print(f"{fname} block[{i}]: BAD {m.group(0)}")
```
Zero output = all markers valid.

### Debugging remnant placeholders

After `reassemble`, any file with `WARNING: N remnant placeholders` has broken `@@` markers. To find them:
```bash
grep -o '@@[^@]*@@' content/zh/problem_file.html | sort | uniq -c
```
For each remnant, check whether it exists as a key in the corresponding extract's `verbatim_map`. If not, classify the failure (Type A or B above) and apply the corresponding fix.

## Batch workflow

```bash
# 1. Extract all blocks
python3 scripts/batch_translate.py extract

# 2. Generate LLM prompts
python3 scripts/batch_translate.py prompts

# 3. Translate (manual or via LLM), save as translations.json
#    Format: {"filename.html": ["translated block 0", ...], ...}

# 4. Apply translations
python3 scripts/batch_translate.py fill translations.json

# 5. Reassemble HTML
python3 scripts/batch_translate.py reassemble

# 6. Fix broken internal links (needed when filename map changes names)
python3 scripts/fix_zh_links.py
```

## Glossary format

```json
{
  "version": "1.0",
  "terms": {
    "complex number": "复数",
    "derivative": "导数",
    ...
  },
  "conventions": {
    "names": "preserve in original form",
    "example_labels": "\"Example 1\" → \"例 1\"",
    "theorem_labels": "\"Theorem 1\" → \"定理 1\"",
    "tone": "pedagogical, natural Chinese mathematical idiom"
  }
}
```

## Post-reassembly: fixing internal links

`batch_translate.py reassemble` renames output files using the filename map
(e.g., `table_of_contents.html` → `mu_lu.html`), but it does NOT update
`href`/`src` attributes inside the HTML.  After reassembly, all internal links
still point to the old English filenames and are broken.

### Automated fix

Run the link fixer, which reads the same `filename-map.json` and rewrites
every `href`/`src` pointing to a mapped `.html` file:

```bash
python3 scripts/fix_zh_links.py
```

It preserves anchors (`#section1`), query strings (`?lang=zh`), and external
URLs (`https://...`).  Files not in the map (untranslated pages, cross-language
links) are left unchanged.  The script is idempotent — safe to re-run.

### Manual pre-flight: check the map

Before running, verify `docs/translation/filename-map.json` covers every
source HTML file that should have its links rewritten:

```bash
python3 -c "
import json, os
with open('docs/translation/filename-map.json') as f:
    fmap = json.load(f)
src = set(os.listdir('content/en/')) & {k for k in fmap}
mapped = set(fmap.values())
missing = src - set(fmap.keys())
print(f'Source files:   {len(src)}')
print(f'Mapped:          {len(mapped)}')
print(f'Not in map:      {missing}')"
```

Any file listed as "Not in map" will have its `href`/`src` references left
in English — those target pages were not translated.

## Verification

After translation, check for remnant placeholders:
```bash
grep -r '@@\w\+:[0-9]\+:[a-f0-9]\+@@' content/zh/
```
Expected: zero output. Any remnant means a placeholder was not restored.

Also verify no broken links remain (only checks files in the map):
```bash
python3 scripts/fix_zh_links.py
```
Re-running it reports zero fixes if all links are already correct.
