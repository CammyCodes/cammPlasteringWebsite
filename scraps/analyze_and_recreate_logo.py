from PIL import Image

img = Image.open('assets/camm-logo.png.bak')
print("Original size:", img.size)
print("Mode:", img.mode)

img_rgba = img.convert('RGBA')

# High resolution upscale using Lanczos
scale = 10
high_res = img_rgba.resize((img.width * scale, img.height * scale), Image.LANCZOS)
high_res.save('scraps/upscaled_logo.png')
print("Saved upscaled_logo.png at size:", high_res.size)
