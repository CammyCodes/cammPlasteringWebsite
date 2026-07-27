import urllib.request
import re
from PIL import Image

def download_file(url, out_path):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    with urllib.request.urlopen(req) as resp, open(out_path, 'wb') as f:
        f.write(resp.read())

# Fetch CSCS logo
try:
    print("Fetching CSCS...")
    download_file('https://www.cscs.uk.com/wp-content/uploads/2021/04/CSCS-logo.png', 'assets/accreditations/cscs.png')
    print("CSCS downloaded successfully")
except Exception as e:
    print("CSCS error:", e)

# Fetch CHAS logo
try:
    print("Fetching CHAS...")
    download_file('https://www.chas.co.uk/wp-content/uploads/2023/02/veriforce-chas-logo.png', 'assets/accreditations/chas.png')
    print("CHAS downloaded successfully")
except Exception as e:
    print("CHAS error:", e)

# Fetch SSIP logo
try:
    print("Fetching SSIP...")
    download_file('https://ssip.org.uk/wp-content/uploads/2020/09/ssip-logo.png', 'assets/accreditations/ssip.png')
    print("SSIP downloaded successfully")
except Exception as e:
    print("SSIP error:", e)

# Fetch NHBC logo
try:
    print("Fetching NHBC...")
    download_file('https://www.nhbc.co.uk/themes/custom/nhbc_theme/logo.png', 'assets/accreditations/nhbc.png')
    print("NHBC downloaded successfully")
except Exception as e:
    print("NHBC error:", e)
