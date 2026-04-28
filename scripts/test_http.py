import urllib.request
import json
import sys

# Test if we can make HTTP requests
try:
    req = urllib.request.Request('https://httpbin.org/get')
    with urllib.request.urlopen(req, timeout=5) as resp:
        print("HTTP: OK")
except Exception as e:
    print(f"HTTP: {e}")
