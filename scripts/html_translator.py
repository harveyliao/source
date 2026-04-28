#!/usr/bin/env python3
"""
HTML-aware text block extractor and reassembler for complex-analysis translation.
Strategy:
1. Protect LaTeX math, <iframe>, <script>, <style> → @@verbatim:...@@ or @@math:...@@
2. Find block-level tags (p, li, h1-h6, figcaption) via regex + close-tag matching
3. Extract inner content, convert inline HTML to compact markers
4. Replace inner content with placeholders in HTML string
5. Reassemble: restore translated text (with markers → HTML) and verbatim content
"""

import re, json, sys, os, uuid
from html.parser import HTMLParser

# ─── Configuration ───────────────────────────────────────────────────────
BLOCK_TAGS = {'p', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'figcaption', 'dt', 'dd', 'td', 'th'}
INLINE_TAGS = {'em', 'strong', 'code', 'span', 'sup', 'sub', 'a', 'cite', 'q', 'abbr', 'i', 'b', 'u', 'small', 'mark'}

# Patterns
COMMENT_RE = re.compile(r'<!--.*?-->', re.DOTALL)
MATH_DISPLAY_RE = re.compile(r'\$\$[^$]+\$\$|\$\$(?:\\.|[^$])+\$\$', re.DOTALL)
MATH_INLINE_RE = re.compile(r'(?<!\$)\$[^$\n]+?\$(?!\$)|\\\[[^\]]*?\\\]', re.DOTALL)
MATH_ENV_RE = re.compile(r'\\begin\{(equation|eqnarray|align|gather|multline)\*?\}(.*?)\\end\{\1\*?\}', re.DOTALL)

_ph_id = [0]
def ph(cat):
    p = f'@@{cat}:{_ph_id[0]}:{uuid.uuid4().hex[:6]}@@'
    _ph_id[0] += 1
    return p

# ─── Protection ──────────────────────────────────────────────────────────
def protect_all(html):
    """Protect math, iframes, scripts, styles, comments with placeholders. Returns (protected_html, map)."""
    vmap = {}
    # Comments first
    text = COMMENT_RE.sub(lambda m: _store(vmap, ph('verbatim'), m.group()), html)
    # Script tags
    text = re.sub(r'<script\b[^>]*>.*?</script>', lambda m: _store(vmap, ph('verbatim'), m.group()), text, flags=re.DOTALL)
    # Style tags
    text = re.sub(r'<style\b[^>]*>.*?</style>', lambda m: _store(vmap, ph('verbatim'), m.group()), text, flags=re.DOTALL)
    # Iframes
    text = re.sub(r'<iframe\b[^>]*>.*?</iframe>', lambda m: _store(vmap, ph('verbatim'), m.group()), text, flags=re.DOTALL)
    # Display math (longest first)
    text = MATH_ENV_RE.sub(lambda m: _store(vmap, ph('math'), m.group()), text)
    text = MATH_DISPLAY_RE.sub(lambda m: _store(vmap, ph('math'), m.group()), text)
    text = MATH_INLINE_RE.sub(lambda m: _store(vmap, ph('math'), m.group()), text)
    return text, vmap

def _store(vmap, placeholder, value):
    vmap[placeholder] = value
    return placeholder

# ─── Marker encoding ─────────────────────────────────────────────────────
def html_to_marker(inner):
    """Convert inline HTML to compact markers. Preserves @@placeholders."""
    result = inner
    # <a href="URL" attr="val">text</a> → [[a href="URL" attr="val"]]text[[/a]]
    result = re.sub(
        r'<(a\b[^>]*)>(.*?)</a>',
        r'[[\1]]\2[[/a]]',
        result, flags=re.DOTALL | re.IGNORECASE
    )
    # <br>
    result = re.sub(r'<br\s*/?>', ' [[br]] ', result, flags=re.IGNORECASE)
    # Other inline tags: <tag attr="val">text</tag> → [[tag attr="val"]]text[[/tag]]
    inline_pat = '|'.join(INLINE_TAGS - {'a'})
    result = re.sub(
        rf'<({inline_pat})(\b[^>]*)>(.*?)</\1>',
        r'[[\1\2]]\3[[/\1]]',
        result, flags=re.DOTALL | re.IGNORECASE
    )
    return result

def marker_to_html(text):
    """Convert markers back to HTML. Repeats until stable (handles nested markers)."""
    inline_pat = '|'.join(INLINE_TAGS)
    marker_re = re.compile(
        rf'\[\[({inline_pat})(\b[^\]]*)\]\](.*?)\[\[/(\1)\]\]',
        re.DOTALL | re.IGNORECASE
    )
    prev = None
    while text != prev:
        prev = text
        text = marker_re.sub(r'<\1\2>\3</\1>', text)
    text = text.replace(' [[br]] ', '<br>')
    return text

# ─── Block finding ───────────────────────────────────────────────────────
def _find_closing_tag(html, pos, tag):
    """Find matching </tag> starting from pos. Handles nested same-tags."""
    depth = 1
    i = pos
    while i < len(html):
        # Find next occurrence of the tag
        open_match = re.search(rf'<{tag}\b', html[i:], re.IGNORECASE)
        close_match = re.search(rf'</{tag}>', html[i:], re.IGNORECASE)
        if close_match is None:
            return -1
        if open_match and open_match.start() < close_match.start():
            depth += 1
            i += open_match.end()
        else:
            depth -= 1
            if depth == 0:
                return i + close_match.end()
            i += close_match.end()
    return -1

def extract_blocks(protected_html):
    """Find all block-level tags in protected HTML, extract inner content with byte positions.
    Returns [(block_id, tag, raw_content, marker_text, byte_start, byte_end_inner), ...]."""
    blocks = []
    idx = 0
    pos = 0
    open_pattern = rf'<({"|".join(BLOCK_TAGS)})(\b[^>]*|)>'
    
    while pos < len(protected_html):
        m = re.search(open_pattern, protected_html[pos:], re.IGNORECASE)
        if not m:
            break
        tag = m.group(1).lower()
        tag_start = pos + m.start()
        inner_start = pos + m.end()
        close_pos = _find_closing_tag(protected_html, inner_start, tag)
        if close_pos < 0:
            pos = inner_start
            continue
        inner_end = close_pos - len(f'</{tag}>')
        
        raw_inner = protected_html[inner_start:inner_end]
        marker_text = html_to_marker(raw_inner)
        blocks.append({
            'id': f'block_{idx}', 'tag': tag,
            'raw': raw_inner, 'text': marker_text,
            'byte_start': inner_start, 'byte_end': inner_end
        })
        idx += 1
        pos = close_pos
    
    return blocks

def apply_placeholders(html, blocks):
    """Replace block inner content with placeholders. Uses list slice assignment."""
    result = list(html)
    for block in reversed(blocks):
        p = ph('text')
        result[block['byte_start']:block['byte_end']] = p
        block['placeholder'] = p
    return ''.join(result)

# ─── Command: extract ────────────────────────────────────────────────────
def cmd_extract(html_path, output_path=None):
    with open(html_path, 'r', encoding='utf-8') as f:
        raw = f.read()
    
    protected, vmap = protect_all(raw)
    blocks = extract_blocks(protected)
    template = apply_placeholders(protected, blocks)
    
    result = {
        'file': os.path.basename(html_path),
        'original_length': len(raw),
        'num_text_blocks': len(blocks),
        'num_verbatim': sum(1 for k in vmap if '@@verbatim:' in k),
        'verbatim_map': vmap,
        'text_blocks': [{
            'id': b['id'], 'tag': b['tag'],
            'text': b['text'], 'raw_len': len(b['raw']),
            'placeholder': b.get('placeholder', ''),
            'byte_start': b['byte_start'], 'byte_end': b['byte_end']
        } for b in blocks],
        'reassembly_template': template,
        '_protected_html': protected
    }
    
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"{html_path}: {len(blocks)} blocks, {result['num_verbatim']} verbatim", file=sys.stderr)
    
    if output_path:
        print(output_path)
    return result

# ─── Command: reassemble ─────────────────────────────────────────────────
def cmd_reassemble(extract_json_path, translations_json_path, output_path):
    with open(extract_json_path, 'r', encoding='utf-8') as f:
        ext = json.load(f)
    with open(translations_json_path, 'r', encoding='utf-8') as f:
        translations = json.load(f)
    
    template = ext['reassembly_template']
    vmap = ext['verbatim_map']
    
    for block, trans in zip(ext['text_blocks'], translations):
        trans_html = marker_to_html(trans)
        template = template.replace(block['placeholder'], trans_html, 1)
    
    # Restore all verbatim/math placeholders (replace ALL occurrences — 
    # some markers may appear twice if the template has them outside blocks
    # AND the translated text re-introduces them inside blocks)
    for placeholder, original in vmap.items():
        while placeholder in template:
            template = template.replace(placeholder, original)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(template)
    print(f"Reassembled: {output_path} ({len(template)} chars)", file=sys.stderr)

# ─── CLI ─────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    subs = parser.add_subparsers(dest='cmd')
    
    ext = subs.add_parser('extract')
    ext.add_argument('html_file')
    ext.add_argument('-o', '--output')
    
    asm = subs.add_parser('reassemble')
    asm.add_argument('extract_json')
    asm.add_argument('translations_json')
    asm.add_argument('output_html')
    
    args = parser.parse_args()
    if args.cmd == 'extract':
        cmd_extract(args.html_file, args.output)
    elif args.cmd == 'reassemble':
        cmd_reassemble(args.extract_json, args.translations_json, args.output_html)
    else:
        parser.print_help()
