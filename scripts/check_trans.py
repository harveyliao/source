#!/usr/bin/env python3
"""Check available translation libs."""
try:
    from deep_translator import GoogleTranslator
    print("deep_translator: OK")
except:
    print("deep_translator: NOT AVAILABLE")

try:
    import googletrans
    print("googletrans: OK")
except:
    print("googletrans: NOT AVAILABLE")

try:
    import translate
    print("translate: OK")
except:
    print("translate: NOT AVAILABLE")

# Try pip list
import subprocess
r = subprocess.run(["pip3", "list"], capture_output=True, text=True)
for line in r.stdout.split('\n'):
    if 'transl' in line.lower():
        print(f"  pip: {line}")
