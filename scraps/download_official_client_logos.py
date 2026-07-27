import urllib.request
import os

assets_clients_dir = os.path.join('assets', 'clients')
os.makedirs(assets_clients_dir, exist_ok=True)

logos = {
    'harron-homes.svg': 'https://media.harronhomes.com/wp-content/uploads/2020/04/24173327/HARRON-LOGO.svg',
    'avant-homes.svg': 'https://www.avanthomes.co.uk/images/homepage/1_top/avant_logo.svg'
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for fname, url in logos.items():
    dest = os.path.join(assets_clients_dir, fname)
    print(f"Downloading {fname} from {url}...")
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp, open(dest, 'wb') as f:
        f.write(resp.read())
    print(f"Saved {fname} ({os.path.getsize(dest)} bytes)")

print("Official client logos downloaded successfully!")
