#9.1
from idlelib.configdialog import font_sample_text

from PIL import Image, ImageFilter,ImageDraw, ImageFont


#a=Image.open(r"C:\Users\Goltz\Desktop\9\maxresdefault.jpg")
"""
a.show()
print("razreshenie",a.size,"\n","format",a.format,"\n","tsvet model",a.mode)

#9.2
a=a.resize((int(a.width/3),int(a.height/3)))
b=a.resize((int(a.height/3),int(a.width/3)))
a.show()
"""
#a=a.save(r"C:\Users\Goltz\Desktop\9\жмых горизонт.jpg")
#b=b.save(r"C:\Users\Goltz\Desktop\9\жмых вертикал.jpg")

#9.3
a=[Image.open(r"C:\Users\Goltz\Desktop\9\9.3\647cd1ef-bfc9-5bdc-8779-30b351146ddf.jpg"),
   Image.open(r"C:\Users\Goltz\Desktop\9\9.3\Gemini_Generated_Image_ezzsjyezzsjyezzs.png"),
   Image.open(r"C:\Users\Goltz\Desktop\9\9.3\Gemini_Generated_Image_mwgdvgmwgdvgmwgd.png"),
   Image.open(r"C:\Users\Goltz\Desktop\9\9.3\P1130748_compressed.jpeg"),
   Image.open(r"C:\Users\Goltz\Desktop\9\9.3\photo_2026-01-16_18-12-40.jpg")
   ]
c=0
b=[
    ImageFilter.CONTOUR,
    ImageFilter.EMBOSS,
    ImageFilter.SHARPEN,
    ImageFilter.EDGE_ENHANCE_MORE,
    ImageFilter.DETAIL
]
for e in a:
    v=e.filter(b[c])
    c += 1
    if v.mode == "RGBA":
        v=v.convert("RGB")
    v.save(f"C:/Users/Goltz/Desktop/9/9.3/save/save_image{c}.jpg")
#9.4
for e in a:
    draw=ImageDraw.Draw(e)
    text="namazano"
    font=ImageFont.load_default(50)
    margin=100
    draw.text((1, 1), text, fill="blue", font=font)
    e.show()