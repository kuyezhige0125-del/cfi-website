import sys
sys.stdout.reconfigure(encoding="utf-8")
from PIL import Image, ImageDraw, ImageFont
import os

img = Image.new("RGB", (800, 800), (255, 248, 237))
draw = ImageDraw.Draw(img)

ORANGE = (223, 74, 22)
DARK = (23, 19, 15)

# Geometric circles
for i in range(3):
    cx, cy = 200 + i*200, 300 + i*100
    r = 250 + i*30
    alpha = Image.new("RGBA", (800, 800), (0, 0, 0, 0))
    ad = ImageDraw.Draw(alpha)
    ad.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(223, 74, 22, 25 + i*10))
    img = Image.alpha_composite(img.convert("RGBA"), alpha).convert("RGB")
    draw = ImageDraw.Draw(img)

# Grid lines
for x in range(0, 800, 40):
    draw.line([(x, 0), (x, 800)], fill=(23, 19, 15, 12), width=1)
for y in range(0, 800, 40):
    draw.line([(0, y), (800, y)], fill=(23, 19, 15, 12), width=1)

# Forward triangle
draw.polygon([(300, 500), (500, 500), (400, 300)], fill=ORANGE)
draw.polygon([(350, 430), (450, 430), (400, 330)], fill=(255, 248, 237))

# Accent bars
draw.rectangle([(150, 580), (650, 586)], fill=ORANGE)
draw.rectangle([(200, 595), (600, 599)], fill=DARK)

# Dots
for i in range(7):
    dot_x = 300 + i * 35
    draw.ellipse([dot_x-3, 630-3, dot_x+3, 630+3], fill=ORANGE)

# Try fonts
font_large = ImageFont.load_default()
font_small = ImageFont.load_default()
for fp in ["C:\\Windows\\Fonts\\msyh.ttc", "C:\\Windows\\Fonts\\simhei.ttf"]:
    if os.path.exists(fp):
        font_large = ImageFont.truetype(fp, 36)
        font_small = ImageFont.truetype(fp, 20)
        break

draw.text((400, 670), "CRIPPING FUTURE INSTITUTE", fill=DARK, font=font_small, anchor="mt")
draw.text((400, 700), "\u6ca1\u6709\u6211\u4eec\u7684\u53c2\u4e0e\uff0c\u4e0d\u8981\u505a\u6709\u5173\u6211\u4eec\u7684\u51b3\u5b9a", fill=ORANGE, font=font_small, anchor="mt")
draw.text((400, 735), "\u7528\u793e\u7fa4\u529b\u91cf \u91cd\u5851\u672a\u6765", fill=DARK, font=font_large, anchor="mt")

# Mono labels
try:
    font_mono = ImageFont.truetype("C:\\Windows\\Fonts\\cour.ttf", 14)
    draw.text((50, 50), "CFI // ARCHIVE // 001", fill=ORANGE, font=font_mono)
    draw.text((50, 70), "EST. 2024 // RESEARCH // COMMUNITY", fill=DARK, font=font_mono)
except:
    pass

img = img.convert("RGB")
img.save("static/brand-reference.jpg", "JPEG", quality=95)
print(f"Image saved: {os.path.abspath('static/brand-reference.jpg')} ({img.size})")
