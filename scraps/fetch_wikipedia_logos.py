import urllib.request
import re

def get_wikimedia_image(page_url):
    req = urllib.request.Request(page_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    html = urllib.request.urlopen(req).read().decode('utf-8')
    m = re.search(r'href="(https://upload\.wikimedia\.org/wikipedia/commons/[^"]+)"', html)
    if m:
        return m.group(1)
    return None

cscs_url = get_wikimedia_image('https://commons.wikimedia.org/wiki/File:CSCS-Logo.png')
print("CSCS URL:", cscs_url)

if cscs_url:
    req = urllib.request.Request(cscs_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    with urllib.request.urlopen(req) as resp, open('assets/accreditations/cscs.png', 'wb') as f:
        f.write(resp.read())
    print("CSCS logo saved successfully")
