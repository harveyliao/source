import urllib.request
import json

# Try libre translate
data = json.dumps({"q": "Hello world", "source": "en", "target": "zh", "format": "text"}).encode()
req = urllib.request.Request('https://libretranslate.com/translate', data=data, 
    headers={'Content-Type': 'application/json'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        print(resp.read().decode())
except Exception as e:
    print(f"Error: {e}")
