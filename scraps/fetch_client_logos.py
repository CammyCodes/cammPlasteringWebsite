import urllib.request
import os

assets_clients_dir = os.path.join('assets', 'clients')
os.makedirs(assets_clients_dir, exist_ok=True)

urls = {
    'harron-homes.png': 'https://img.logo.dev/harronhomes.co.uk?token=pk_X_60V7lUS-23nUq6Vn4Hbg&size=400',
    'avant-homes.png': 'https://img.logo.dev/avanthomes.co.uk?token=pk_X_60V7lUS-23nUq6Vn4Hbg&size=400',
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for fname, url in urls.items():
    dest = os.path.join(assets_clients_dir, fname)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp, open(dest, 'wb') as f:
            f.write(resp.read())
        print(f"Downloaded {fname} successfully ({os.path.getsize(dest)} bytes)")
    except Exception as e:
        print(f"Error downloading {fname}: {e}")
