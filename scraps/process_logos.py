from PIL import Image

def process_logo(filename):
    path = f'assets/accreditations/{filename}.png'
    img = Image.open(path).convert("RGBA")
    datas = img.getdata()
    
    new_data = []
    for item in datas:
        # Convert near-white background pixels to transparent
        if item[0] > 240 and item[1] > 240 and item[2] > 240:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    
    # Auto-crop non-transparent bounding box
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
        
    img.save(path, "PNG")
    print(f"Processed {filename}.png, new size: {img.size}")

for name in ['nhbc', 'ssip', 'chas', 'cscs']:
    try:
        process_logo(name)
    except Exception as e:
        print(f"Error processing {name}: {e}")
