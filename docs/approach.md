Overall Workflow

The pipeline has 4 stages, orchestrated by scripts/batch_translate.py:


content/en/*.html            (46 English source files)
        │
        ▼
  [1] extract
        │    html_translator.py extracts text blocks + verbatim_map
        │    (math IDs, code blocks, etc.)
        ▼
  docs/translation/extracts/*.json 
        │
        ▼
  [2] prompts
        │    gen_prompts.py generates system+user prompts
        │    for each file, guided by glossary-zh.json
        ▼
  docs/translation/prompts/*.json
        │
        ▼
  [3] 🔧 MANUAL or AI Step: Translate the blocks
        │    Each extract has N blocks — produce N Chinese equivalents.
        │    @@markers@@ (math, code, URLs) must be preserved exactly.
        │    Store results in docs/translation/translations/*.json
        │
        │    For the merged JSON approach:
        │    docs/translation/translations-merged.json
        │      →  python3 batch_translate.py fill translations-merged.json
        │         (splits merged JSON back into per-file translations)
        ▼
  [4] reassemble
        │    html_translator.py reassembles each file:
        │    extract.json + translation.json → content/zh/CHINESE.html
        │    (Chinese filename from docs/translation/filename-map.json)
        ▼
content/zh/*.html            (46 Chinese output files)
        │
        ▼
  [5] fix_zh_links.py
        │    Reads filename-map.json, replaces English filenames
        │    in href/src attributes with their Chinese equivalents.
        │    (101 links fixed across 43 files)
        ▼
content/zh/*.html            (fully navigable Chinese site)


Key files summary:

| File | Role |
|------|------|
| content/en/*.html | 46 English source pages |
| content/zh/*.html | 46 Chinese output pages (pinyin filenames) |
| scripts/batch_translate.py | Pipeline orchestrator (4 subcommands) |
| scripts/html_translator.py | Core engine: extract/reassemble individual files |
| scripts/gen_prompts.py | Generates LLM translation prompts |
| scripts/fix_zh_links.py | Post-processing: fixes internal links after rename |
| docs/translation/filename-map.json | English→pinyin filename mapping (46 entries) |
| docs/translation/glossary-zh.json | Terminology glossary for translation consistency |
| docs/translation/extracts/*.json | 46 extracted block sets with verbatim maps |
| docs/translation/translations/*.json | 46 translated block sets |
| docs/translation/translations-merged.json | Single-file merged format for bulk fill |



How to Tell the Maintainer (Juan Carlos Ponce)

Based on the README, two channels exist:

1. Email — jcponcemath@gmail.com (specifically mentioned as the way to "get instructions on how to make a translation")
2. GitHub Issues — https://github.com/complex-analysis/complex-analysis.github.io/issues

I'd suggest this approach:

Step A: Open a GitHub issue with a summary like:

> Title: Chinese (Mandarin) translation completed — 46 pages ready for review
>
> Body: I've completed a full Chinese translation of the complex-analysis.com textbook using this repo's source HTML files. All 46 English pages have been translated to Chinese and reassembled into content/zh/, with pinyin-based filenames following the existing docs/translation/filename-map.json. Internal links have been updated so the Chinese pages form a fully navigable site.
>
> What's new in this repo:
> - scripts/fix_zh_links.py — post-reassembly link fixer (addresses a gap in the pipeline where reassembly doesn't update inter-page links)
> - docs/translation/translations/ — 46 per-file Chinese translation JSONs
> - docs/translation/translations-merged.json — single-file merged format
>
> Translation notes:
> - Mathematical notation and code blocks are preserved verbatim
> - Terminology follows standard Chinese math conventions
> - 1353 text blocks translated across 46 pages
> - Pipeline: extract → translate → fill → reassemble → fix links
>
> Ready for review. Let me know if you'd like any adjustments to the pinyin filenames or would prefer the Chinese pages be served from complex-analysis.com.

Step B: Follow up by email to the address in the README, since that's the channel the maintainer explicitly set aside for translation discussions. Attach or link to the issue.

Step C: If this turns into a PR, note that the pipeline scripts (batch_translate.py, html_translator.py, gen_prompts.py, and the docs/translation/ directory) were already in the repo — the Chinese translation is additive: new translation JSONs + output HTML + the fix_zh_links.py utility.
