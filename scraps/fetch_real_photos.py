import urllib.request
import os

assets_dir = 'assets'

# High resolution real photo URLs (Unsplash CDN direct image endpoints)
photos = {
    # Plasterer working on wall with trowel
    'hero.jpg': 'https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=1200&q=85',
    # Close up of trowel / plastering
    'svc-plastering.jpg': 'https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=800&q=85',
    # Drylining / plasterboard construction site interior
    'svc-drylining.jpg': 'https://images.unsplash.com/photo-1541888946425-d0fbb186a5b3?auto=format&fit=crop&w=800&q=85',
    # Modern rendered house exterior
    'svc-rendering.jpg': 'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=800&q=85'
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for filename, url in photos.items():
    dest_path = os.path.join(assets_dir, filename)
    print(f"Downloading real photo for {filename} from {url}...")
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp, open(dest_path, 'wb') as f:
        f.write(resp.read())
    print(f"Saved {filename} successfully ({os.path.getsize(dest_path)} bytes)")

print("All real photos downloaded successfully!")
