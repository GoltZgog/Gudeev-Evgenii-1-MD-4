import random
from idlelib.configdialog import font_sample_text

from PIL import Image, ImageFilter,ImageDraw, ImageFont
#10.1
a=Image.open(r"C:\Users\Goltz\Desktop\10\ccda46fcae4a7df3ed8ac8e3c63bd907.jpg")
b=""
b=a.crop((439,745,905,880))
b.save(r"C:\Users\Goltz\Desktop\10\save\ccda46fcae4a7df3ed8ac8e3c63bd907.jpg")

#10.2
a={"день бобра":r"C:\Users\Goltz\Desktop\10\10.2\Foiz.PRO_-День-Бобра-.jpg",
   "день пяток":r"C:\Users\Goltz\Desktop\10\10.2\oar2.jpg",
   "день риса":r"C:\Users\Goltz\Desktop\10\10.2\Заставка-рис.jpg"}
t=list(a.keys())
print("какой праздик желаете выбрать? ",t)
r=input("mazani:  ")
if r in a:
   r=Image.open(a[r])
   r.show()

#10.3

a={"день бобра":r"C:\Users\Goltz\Desktop\10\10.2\Foiz.PRO_-День-Бобра-.jpg",
   "день пяток":r"C:\Users\Goltz\Desktop\10\10.2\oar2.jpg",
   "день риса":r"C:\Users\Goltz\Desktop\10\10.2\Заставка-рис.jpg"}
t=list(a.keys())
print("какой праздик желаете выбрать  и кого поздравить? ",t)
r=input("mazani:  ")
y=input("mazani pogonyalo:  ")
y=f"поздравляю с праздником {y}"

if r in a:
   r=Image.open(a[r])
   i,o=r.size
   r = r.resize((1024, 1024))
   draw=ImageDraw.Draw(r)
   font = [(r"C:\Windows\Fonts\arialbd.ttf", 30),
   (r"C:\Windows\Fonts\calibrib.ttf", 35),
   (r"C:\Windows\Fonts\timesbd.ttf", 30),
   (r"C:\Windows\Fonts\tahomabd.ttf", 35)
   ]
   c=["red","blue","green","magenta","orange","gold","deepskyblue"
   ]
   d,f=random.choice(font)
   font =ImageFont.truetype(d,f)
   rgb=random.choice(c)
   margin = 20
   text_width=draw.textlength(y,font)
   xy=[(1024/2-text_width/2,margin),(1024/2-margin-text_width/2,1024-50)]
   draw.text((random.choice(xy)),text=y,font=font,fill=rgb)
   r.show()
   r.save(r"C:\Users\Goltz\Desktop\10\10.3\otkritka.png")