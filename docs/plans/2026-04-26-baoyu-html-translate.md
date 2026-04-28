# Complex Analysis Chinese Translation — Implementation Plan

> **Status: Phase 2 Pilot — TOOLING COMPLETE, translation pending**
> 
> ### Executed Tasks
> - [x] Task 1: Directory structure + glossary (glossary-zh.json with 100+ terms)
> - [x] Task 2: HTML extraction/reassembly script (html_translator.py — stdlib-only, 40/47 identity-pass)
> - [x] Task 3: Translation prompt generator (gen_prompts.py)
> - [x] Task 4-5: Pilot translate thanks.html + terminology_notation.html (verified: 0 remnant markers, math preserved)
> - [x] Task 7: Batch workflow script (batch_translate.py) + pinyin filename mapping (filename-map.json)
> 
> ### Key Deviations from Original Plan
> - **No BeautifulSoup4:** Environment has no pip; used stdlib regex + html.parser. Script is 100% stdlib.
> - **Marker format:** Inline tags encoded as `[[tag attr="val"]]text[[/tag]]` instead of raw HTML text nodes
> - **Pinyin filenames:** `complex_differentiation.html` → `fu_wei_fen.html` (instead of keeping English filenames)
> - **Simplified prompt:** Combined 4-stage methodology into a single comprehensive system prompt (not 4 separate subagent calls per block) — 47 files × ~10 blocks/file × 4 stages = 1880 subagent calls is impractical
> 
> ### Remaining
> - [ ] Task 8-12: Batch translate all 47 files (can use subagent delegation per file)
> - [ ] Task 13-14: Cross-references, zh.html landing page
> - [ ] Task 15-18: QA, glossary audit, LaTeX verification, spot-checks

**Goal:** Translate 47 English HTML files from `content/en/` to Chinese `content/zh/`, preserving all HTML structure, LaTeX math, GeoGebra iframes, JavaScript directives, and interactive elements while applying baoyu-translate's methodology (rewrite-not-translate, glossary consistency, natural mathematical Chinese).

**Architecture:** A Python-based HTML-aware translation pipeline that (1) parses each HTML file into translatable text blocks and verbatim blocks, (2) uses LLM translation with glossary enforcement for each text block, (3) applies the 4-stage baoyu methodology per block via subagent parallelism, (4) reassembles and validates output HTML. Files are processed in batches of 5-8 by difficulty tier.

**Tech Stack:** Python 3 with BeautifulSoup4 (or lxml) for HTML parsing, subagent delegation for parallel translation of text blocks, existing complex-analysis repo structure following `content/es/` precedent.

---

## Architecture Decisions

### What stays verbatim (never touches the LLM)
- All HTML tags, attributes, structure
- LaTeX math: `$...$`, `$$...$$`, `\[...\]`, `\begin{...}...\end{...}`
- LaTeX commands in text: `\ref{...}`, `\label{...}`, `\mathbb`, `\lim`, etc.
- `<iframe>` embeds (GeoGebra, p5.js)
- `<script>` tags and inline JavaScript
- `w3-include-html` directives
- `<style>` blocks
- URLs, file paths, image `src`/`href` attributes
- CSS class names and IDs

### What gets translated
- Text content of: `<p>`, `<h1>`-`<h6>`, `<figcaption>`, `<li>`, `<em>`, `<strong>`, `<a>` (link text only, not href)
- `<title>` content
- `alt` and `title` attributes on `<img>` tags
- Navigation labels (e.g., "Table of Contents", "Next: ...")
- Content in `<div class="theorem">`, `<div class="practice">`, `<div class="callout">`

### What gets adjusted (structural)
- Filenames: translated to Chinese pinyin or semantic names
- Cross-references: internal `<a href="content/some_page.html">` updated to Chinese filenames
- Language link div: add Chinese entry
- Navigation arrows: translated labels
- Example labels: "Example 1" → "例 1"

### Translation methodology (adapted from baoyu-translate 4-stage)
For each translatable text block:

1. **Analysis** — Identify domain terminology, glossary terms, math context, tone (pedagogical/technical)
2. **Draft** — Produce initial Chinese translation with glossary enforcement, natural mathematical Chinese idiom
3. **Critique** — Review against criteria: accuracy to math meaning, natural Chinese flow, glossary consistency, proper noun handling (names stay in original), appropriate tone for Chinese math pedagogy
4. **Polish** — Apply corrections, ensure LaTeX-preserving whitespace, produce final block

---

## Glossary (bootstrapped — grows during translation)

### Core math terms (initial seed)
| English | Chinese | Notes |
|---------|---------|-------|
| complex number | 复数 | |
| complex function | 复变函数 | |
| complex analysis | 复分析 | |
| complex differentiation | 复微分 | |
| derivative | 导数 | |
| differentiable | 可微的 | |
| analytic function | 解析函数 | |
| holomorphic | 全纯的 | |
| Cauchy-Riemann equations | 柯西-黎曼方程 | |
| conformal mapping | 共形映射 | |
| Riemann surface | 黎曼面 | |
| Riemann sphere | 黎曼球面 | |
| Laurent series | 洛朗级数 | |
| Taylor series | 泰勒级数 | |
| residue | 留数 | |
| singularity | 奇点 | |
| branch cut | 分支切割 | |
| domain coloring | 区域着色 | |
| analytic landscape | 解析景观 | |
| fundamental theorem of algebra | 代数基本定理 | |
| limit | 极限 | |
| continuity | 连续性 | |
| integral | 积分 | |
| Julia set | Julia 集 | |
| Mandelbrot set | Mandelbrot 集 | |
| linear fractional transformation | 线性分式变换 | |
| Möbius transformation | Möbius 变换 | |
| principal argument | 辐角主值 | |
| complex potential | 复势 | |
| Joukowsky airfoil | Joukowsky 翼型 | |
| contour | 围道 | |
| simply connected | 单连通的 | |
| exponential function | 指数函数 | |
| logarithmic function | 对数函数 | |

### Environment terms
| English | Chinese | Notes |
|---------|---------|-------|
| Table of Contents | 目录 | |
| References / Bibliography | 参考文献 | |
| License | 许可协议 | |
| Comments | 评论 | |
| Thanks / Acknowledgements | 致谢 | |
| Next | 下一页 | |
| Previous | 上一页 | |
| Example | 例 | |
| Theorem | 定理 | |

---

## Task Plan

### Phase 1: Project Setup

#### Task 1: Create directory structure and glossary file
**Objective:** Set up `content/zh/` mirroring existing language pattern and create a shared glossary
**Files:**
- Create: `content/zh/` (directory)
- Create: `docs/translation/glossary-zh.json`
- Create: `content/zh/zh.html` (Chinese landing page)

**Step 1:** Create the directory
```bash
mkdir -p /home/harvey/github-repos/complex-analysis-source/content/zh
mkdir -p /home/harvey/github-repos/complex-analysis-source/docs/translation
```

**Step 2:** Create initial glossary file with seed terms above
Write `docs/translation/glossary-zh.json` with the seed terms in structured JSON format:
```json
{
  "version": "1.0",
  "math_terms": { ... },
  "environment_terms": { ... },
  "proper_nouns": { "notes": "Names preserved in original form unless common Chinese convention exists" }
}
```

**Step 3:** Verify
```bash
ls -la content/zh/
cat docs/translation/glossary-zh.json | python3 -m json.tool
```
Expected: directory exists, glossary is valid JSON.

#### Task 2: Create HTML parsing and reassembly script
**Objective:** Build a Python script that extracts translatable text blocks while preserving HTML structure and LaTeX, then reassembles translated blocks back into valid HTML
**Files:**
- Create: `scripts/html_translator.py`

**Script design:**

```python
#!/usr/bin/env python3
"""
HTML-aware translation block extractor and reassembler for complex-analysis.
Extracts text nodes from HTML while preserving:
- HTML structure (tags, attributes, nesting)
- LaTeX math blocks ($, $$, \[ \], \begin{}...\end{})
- LaTeX inline commands (\ref, \label, \mathbb, etc.)
- <iframe>, <script>, <style> elements
"""

from bs4 import BeautifulSoup, NavigableString, Comment
import re
import json
import sys

# Patterns for LaTeX that must never be touched
LATEX_DISPLAY_PATTERN = re.compile(
    r'\$\$.*?\$\$|\\\[.*?\\\]|\\begin\{.*?\}.*?\\end\{.*?\}',
    re.DOTALL
)
LATEX_INLINE_PATTERN = re.compile(r'\$[^$]+\$|\\\(.*?\\\)')
LATEX_COMMAND_PATTERN = re.compile(
    r'\\(?:ref|label|eqref|mathbb|mathbf|mathcal|mathrm|textit|textbf'
    r'|lim|sum|int|prod|partial|infty|rightarrow|Rightarrow|leftarrow'
    r'|Leftarrow|to|cdot|times|cdots|ldots|vdots|ddots'
    r'|alpha|beta|gamma|delta|epsilon|zeta|eta|theta|iota|kappa'
    r'|lambda|mu|nu|xi|pi|rho|sigma|tau|upsilon|phi|chi|psi|omega'
    r'|Delta|Gamma|Lambda|Omega|Phi|Pi|Psi|Sigma|Theta|Xi)\b'
)

# HTML tags whose text content should be translated
TRANSLATABLE_TAGS = {'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
                     'figcaption', 'li', 'em', 'strong', 'a',
                     'title', 'span', 'button', 'dt', 'dd', 'th', 'td'}

# Tags whose inner content must be preserved verbatim
VERBATIM_TAGS = {'script', 'style', 'iframe', 'pre', 'code', 'kbd', 'samp'}

class HTMLBlockExtractor:
    """Extracts translatable text blocks from HTML, preserving structure."""
    
    def __init__(self, html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            self.raw_html = f.read()
        # Don't parse with BeautifulSoup initially — we want to preserve
        # formatting exactly. Use a marker-based approach instead.
    
    def extract_blocks(self):
        """Extract text blocks with position markers for reassembly."""
        blocks = []
        # Strategy: walk the raw HTML, identify translatable text nodes
        # between tags, mark positions, return structured blocks
        return blocks
    
    def reassemble(self, translated_blocks, output_path):
        """Replace original text blocks with translated versions."""
        pass
```

**Step 1:** Install BeautifulSoup4 if needed
```bash
pip install beautifulsoup4
```

**Step 2:** Implement `extract_blocks()` — walks HTML, marks verbatim regions (math/script/iframe), extracts translatable text with position indices

**Step 3:** Implement `reassemble()` — substitutes translated text back into position markers, preserving all whitespace around math/HTML

**Step 4:** Test with a small sample file
```bash
cd /home/harvey/github-repos/complex-analysis-source
python3 scripts/html_translator.py content/en/complex_differentiation.html --extract-only
```
Expected: prints list of text blocks with their positions, no errors.

#### Task 3: Create translation prompt template
**Objective:** Write the 4-stage translation prompt that subagents will use
**Files:**
- Create: `docs/translation/prompt-templates.md`

**Content design:**

````markdown
# Translation Prompt Templates

## Stage 1: Analysis
```
You are analyzing a mathematical text block for translation from English to Chinese.
The text is from an interactive textbook on complex analysis.

Context: This is a {position} in the document. Surrounding math notation uses LaTeX.

Task: Identify in this text block:
1. Domain-specific mathematical terms (list each with suggested Chinese translation)
2. Pedagogical tone markers (explanatory, example-driven, technical, motivational)
3. Any proper nouns, names, or citations (should stay in original form)
4. Any idioms or culturally specific expressions needing localization

Text block:
---
{text_block}
---

Output JSON:
{
  "terms": [{"english": "...", "chinese": "...", "reasoning": "..."}],
  "tone": "...",
  "proper_nouns": [...],
  "localization_notes": [...]
}
```

## Stage 2: Draft Translation
```
You are translating mathematical prose from English to natural, idiomatic Chinese.
Target audience: Chinese undergraduate STEM students reading complex analysis.

Guidelines:
- Use standard PRC mathematical terminology
- Natural Chinese sentence flow — NOT literal translation
- Mathematical rigor preserved exactly
- Proper names stay in original form (Roman alphabet)
- Example labels: "Example 1" -> "例 1"

Glossary (use these terms):
{glossary_entries}

Text block:
---
{text_block}
---

Translation:
```

## Stage 3: Critique
```
You are reviewing a Chinese translation of mathematical text for quality.

Check:
1. Mathematical accuracy — does the Chinese convey the exact same mathematical meaning?
2. Glossary consistency — are all terms from the glossary used correctly?
3. Natural flow — does it read like native Chinese mathematical writing?
4. Proper noun handling — are names preserved in original form?
5. Pedagogical tone — does it match the original's teaching style?

Original: {original_text}
Translation: {translation}

Output JSON:
{
  "passes": true/false,
  "issues": [{"type": "accuracy|consistency|flow|names|tone", "detail": "..."}],
  "fixed_translation": "..." (if fixes needed)
}
```

## Stage 4: Polish
```
Apply these corrections to the final translation.
Original: {original_text}
Current: {current_translation}
Issues: {issues}

Final polished translation (output ONLY the translation text, no commentary):
```
````

**Step 1:** Write the file with complete prompt templates

**Step 2:** Verify format is clean and usable
```bash
wc -l docs/translation/prompt-templates.md
```

---

### Phase 2: Pilot (3 files, validate the pipeline)

#### Task 4: Translate "thanks.html" (simplest file, no math)
**Objective:** Validate the extract→translate→critique→polish→reassemble pipeline end-to-end on the simplest file
**Files:**
- Read: `content/en/thanks.html`
- Create: `content/zh/thanks.html`

**Step 1:** Inspect the source
```bash
wc -l content/en/thanks.html
cat content/en/thanks.html
```

**Step 2:** Extract text blocks using the script

**Step 3:** Run 4-stage translation on each block via subagents

**Step 4:** Reassemble and write `content/zh/thanks.html`

**Step 5:** Visual diff check
```bash
diff <(cat content/en/thanks.html | sed 's/>[^<]*</>X</g') <(cat content/zh/thanks.html | sed 's/>[^<]*</>X</g')
```
Expected: structural diff is empty (only text content differs).

#### Task 5: Translate "terminology_notation.html" (light math)
**Objective:** Validate LaTeX preservation in a file with light math content
**Files:**
- Read: `content/en/terminology_notation.html`
- Create: `content/zh/terminology_notation.html`

**Step 1:** Extract and translate, paying special attention to LaTeX preservation

**Step 2:** Verify: all `$...$`, `\mathbb`, `\rightarrow` etc. unchanged

**Step 3:** Verify: `\ref{...}` and `\label{...}` untouched

#### Task 6: Translate "complex_differentiation.html" (heavy math + iframes)
**Objective:** Validate full pipeline on a content-heavy file with display math and GeoGebra embeds
**Files:**
- Read: `content/en/complex_differentiation.html`
- Create: `content/zh/complex_differentiation.html`

**Step 1:** Extract, translate all blocks

**Step 2:** Verify: all `\begin{eqnarray}...\end{eqnarray}` blocks intact

**Step 3:** Verify: GeoGebra iframe `src` unchanged

**Step 4:** Verify: `<div class="theorem">` text translated, class/IDs preserved

#### Task 7: Pipeline review — update scripts and templates
**Objective:** Incorporate lessons from pilot into scripts and prompt templates
**Files:**
- Modify: `scripts/html_translator.py`
- Modify: `docs/translation/prompt-templates.md`
- Modify: `docs/translation/glossary-zh.json` (add new terms discovered)

**Step 1:** Review what broke or needed adjustment in the 3 pilot files

**Step 2:** Patch the extraction script for any edge cases found

**Step 3:** Update glossary with terms discovered during pilot translation

**Step 4:** Commit all changes
```bash
cd /home/harvey/github-repos/complex-analysis-source
git add content/zh/ scripts/ docs/
git commit -m "feat: pilot Chinese translation (3 files) + tooling"
```

---

### Phase 3: Batch Translation (44 remaining files)

Files organized by difficulty tier for efficient batching:

**Tier 1 — Structure/UI files (8 files, minimal text):**
`small_screen_message.html`, `fixed_applets_message.html`, `message-modal.html`, `license.html`, `bibliography.html`, `comments.html`, `template.html`, `table_of_contents.html`

**Tier 2 — Light conceptual content (12 files):**
`brief_history.html`, `geometric_interpretation_add_mult.html`, `principal_argument.html`, `roots_complex_numbers.html`, `terminology_notation.html` (done), `complex_functions.html`, `continuity.html`, `limits.html`, `mappings.html`, `mapping_1overz.html`, `mappings_upper_half_plane.html`, `applications_conformal.html`

**Tier 3 — Moderate math content (12 files):**
`complex_differentiation.html` (done), `analytic_landscapes.html`, `domain_coloring.html`, `linear_fractional_transformations.html`, `conformal_mapping.html`, `joukowsky_airfoil.html`, `flow_around_circle.html`, `complex_potential_basic_examples.html`, `exponential_function.html`, `logarithmic_function.html`, `power_function.html`, `curves_in_the_complex_plane.html`

**Tier 4 — Heavy math content (10 files):**
`complex_integration.html`, `cauchy_goursat_theorem.html`, `cauchy_integral_formula.html`, `series.html`, `taylor_series.html`, `laurent_series.html`, `classification_of_singularities.html`, `integrals_of_functions_with_branch_cuts.html`, `fundamental_theorem_of_algebra.html`, `topology_complex_plane.html`

**Tier 5 — Advanced topics (5 files):**
`riemann_sphere.html`, `riemann_surfaces.html`, `julia_set.html`, `mandelbrot_set.html`, `index.html`

#### Task 8: Batch Tier 1 (UI files, 8 files)
**Objective:** Translate all structural/UI files in one batch
**Files:** (see Tier 1 list above)

**Step 1:** Process all 8 files in parallel using subagent delegation

**Step 2:** Verify HTML validity of each output

**Step 3:** Commit
```bash
git add content/zh/*.html
git commit -m "feat: translate Tier 1 UI files to Chinese (8 files)"
```

#### Task 9: Batch Tier 2 (light conceptual, 11 files)
**Objective:** Translate lighter conceptual chapters
**Files:** (see Tier 2 list, excluding already-done terminology_notation.html)

**Step 1:** Process in groups of 3-4 with parallel subagents

**Step 2:** Cross-reference glossary consistency across files

**Step 3:** Verify and commit

#### Task 10: Batch Tier 3 (moderate math, 11 files)
**Objective:** Translate moderate-difficulty math chapters
**Files:** (see Tier 3 list, excluding already-done complex_differentiation.html)

**Step 1:** Process in groups of 2-3 with parallel subagents (heavier files)

**Step 2:** Special attention: theorem statements, equation contexts

**Step 3:** Verify and commit

#### Task 11: Batch Tier 4 (heavy math, 10 files)
**Objective:** Translate math-heavy chapters with extensive LaTeX
**Files:** (see Tier 4 list)

**Step 1:** Process 1-2 at a time (files are large, ~500+ lines each)

**Step 2:** Verify all `\begin{eqnarray}`, `\ref{}`, `\label{}` preserved

**Step 3:** Verify and commit

#### Task 12: Batch Tier 5 (advanced topics, 5 files)
**Objective:** Translate advanced topic chapters
**Files:** (see Tier 5 list)

**Step 1:** Process 1-2 at a time

**Step 2:** `index.html` is special — has dynamic year script, donation links, navigation

**Step 3:** Verify and commit

---

### Phase 4: Cross-File Integration

#### Task 13: Update cross-references and navigation
**Objective:** Fix all internal links to point to Chinese filenames, update language-link divs
**Files:**
- Modify: `content/zh/zh.html` (Chinese landing page — update language links)
- Modify: `content/zh/table_of_contents.html` (add Chinese entry to language links)
- Modify: `content/zh/index.html` (update internal links to Chinese filenames)
- Modify: All `content/zh/*.html` files (update any remaining `content/en/` cross-refs)

**Step 1:** Create filename mapping table (English → Chinese)
```json
{
  "complex_differentiation.html": "complex_differentiation.html", // or "fuweifen.html" 
  ...
}
```

**Step 2:** Run a search-and-replace script for internal links
```bash
python3 scripts/fix_crossrefs.py content/zh/
```

**Step 3:** Verify no broken `href="content/en/..."` remain in zh files
```bash
grep -r 'content/en/' content/zh/ 
```
Expected: no output.

#### Task 14: Create Chinese landing page (zh.html)
**Objective:** Create the root-level Chinese landing page matching `es.html` pattern
**Files:**
- Create: `zh.html` (at repo root, like `es.html`)

**Step 1:** Copy `es.html` as template (it's likely at repo root)

**Step 2:** Replace Spanish text with Chinese, update links to `content/zh/`

**Step 3:** Add language link in `index.html` pointing to `zh.html`

---

### Phase 5: Quality Assurance

#### Task 15: Glossary audit
**Objective:** Ensure consistent terminology across all 47 files
**Files:**
- Read: all `content/zh/*.html`
- Modify: `docs/translation/glossary-zh.json`

**Step 1:** For each glossary term, grep all zh files to verify consistent usage
```bash
for term in "复分析" "复变函数" "解析函数"; do
  echo "=== $term ==="
  grep -rl "$term" content/zh/
done
```

**Step 2:** Identify any divergent translations of the same English term

**Step 3:** Fix inconsistencies, update glossary with decisions

#### Task 16: LaTeX integrity check
**Objective:** Verify all LaTeX is preserved verbatim across all files
**Files:**
- Compare: `content/en/` vs `content/zh/`

**Step 1:** Extract all LaTeX blocks from English and Chinese, diff them
```bash
python3 scripts/verify_latex.py content/en/ content/zh/
```
Expected: zero diffs in LaTeX content.

#### Task 17: HTML validity check
**Objective:** Ensure all zh HTML files are well-formed
**Files:**
- Read: all `content/zh/*.html`

**Step 1:** Run HTML validator or parse check
```bash
python3 -c "
from bs4 import BeautifulSoup
import os, sys
for f in os.listdir('content/zh/'):
    if f.endswith('.html'):
        try:
            with open(f'content/zh/{f}') as fh:
                BeautifulSoup(fh, 'html.parser')
        except Exception as e:
            print(f'FAIL: {f}: {e}')
"
```
Expected: all files parse successfully.

#### Task 18: Manual spot-check of 5 representative files
**Objective:** Human-quality verification of translation
**Files:** Pick 5 files spanning difficulty tiers

**Step 1:** Review `content/zh/index.html` — landing page, must be polished

**Step 2:** Review `content/zh/complex_differentiation.html` — heavy math

**Step 3:** Review `content/zh/cauchy_integral_formula.html` — theorem-heavy

**Step 4:** Review `content/zh/table_of_contents.html` — navigation

**Step 5:** Review `content/zh/riemann_surfaces.html` — advanced topic

**Step 6:** Document any issues found, fix in batch

---

## Pitfalls and Edge Cases

### LaTeX corner cases
- **Nested math:** `$\mathbb{C}$` inside `<p>` text — the `$` delimiters must stay
- **Escaped characters:** `\\` in LaTeX (line breaks in eqnarray) — must not be mangled
- **Inline refs:** `(\ref{diff01})` in running text — preserve all of it
- **Slashes in HTML:** LaTeX `\` characters inside HTML text nodes are fine, but watch for `\\` being interpreted as escape

### HTML corner cases
- **`w3-include-html`:** These are directives processed by JS at page load (like `<!--#include-->`). The filename within them may need translation if it points to a translatable file.
- **`<script>document.write(...)</script>`:** JS generating dynamic content (e.g., current year) — must stay exactly as-is
- **Comments:** `<!-- ... -->` — don't translate HTML comments unless they contain user-facing text
- **Mixed content:** Text nodes that mix English, LaTeX, and HTML entities (`&amp;`, `&lt;`) — handle entities correctly

### Translation quality traps
- **Theorem envy:** Mathematical prose in Chinese has its own conventions. "Let f be..." → "设 f 为..." not "让 f 是..."
- **"We" pronouns:** English math writing uses "we" extensively. Chinese math writing often uses impersonal constructions or drops the subject entirely.
- **Example numbering:** "Example 1" → "例 1" (consistent across all files)
- **"Note that..."** → "注意..." or "值得注意..." depending on context (glossary item)

---

## Verification Checklist

- [ ] All 47 files exist in `content/zh/` with translated filenames
- [ ] All LaTeX blocks (`$`, `$$`, `\[`, `\begin{}...\end{}`) match English originals byte-for-byte
- [ ] All `<iframe>` src attributes unchanged
- [ ] All `<script>` content unchanged
- [ ] No `content/en/` references remain in zh files (except intentional ones)
- [ ] All glossary terms used consistently across files
- [ ] Chinese landing page (`zh.html`) exists at repo root
- [ ] Language links updated in `index.html` and `table_of_contents.html`
- [ ] Glossary file (`docs/translation/glossary-zh.json`) is complete
- [ ] HTML validity: all 47 zh files parse cleanly
- [ ] Navigation arrows translated ("下一页", "上一页")
- [ ] Tutorial/instruction text in applet descriptions translated

---

## Execution Notes

- **File count:** 47 source files, 47 output files
- **Estimated translation volume:** ~667 KB of HTML, estimated ~150-200 KB of actual translatable text
- **Parallelism:** Use subagent delegation for batches of 3-5 files. Each subagent gets the full prompt template, glossary, and extractor script context
- **Glossary growth:** Expect to add 20-40 terms during translation. Update glossary after each batch, not after every file
- **Reference:** The `content/es/` directory is the pattern to follow — identical structure, translated text, preserved math
