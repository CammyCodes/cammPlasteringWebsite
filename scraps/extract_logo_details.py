from PIL import Image

img = Image.open('assets/camm-logo.png.bak').convert('RGBA')
w, h = img.size

# Let's inspect pixels in key regions to extract exact colors and positions
colors = {}
for y in range(h):
    for x in range(w):
        r, g, b, a = img.getpixel((x, y))
        if a > 100 and not (r > 240 and g > 240 and b > 240): # Not white/transparent
            hex_c = f"#{r:02x}{g:02x}{b:02x}"
            colors[hex_c] = colors.get(hex_c, 0) + 1

# Sort top colors
top_colors = sorted(colors.items(), key=lambda x: x[1], reverse=True)[:10]
print("Top logo colors (hex, pixel count):", top_colors)
