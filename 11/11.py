
from idlelib.configdialog import font_sample_text

from PIL import Image, ImageFilter,ImageDraw, ImageFont
import os,shutil,csv
#11.1
if not os.path.isdir("save"):
    os.makedirs("save")
elif os.path.isdir("save"):
    shutil.rmtree("save")
    os.makedirs("save")

a=r"C:\Users\Goltz\Desktop\11"
A=os.listdir(a)
c=0
b=[
    ImageFilter.CONTOUR,
    ImageFilter.EMBOSS,
    ImageFilter.SHARPEN,
    ImageFilter.EDGE_ENHANCE_MORE,
    ImageFilter.DETAIL
]
for e in A:
    if os.path.isfile(e):
        t=os.path.join(a,e)
        t=t.split(".")[-1].lower()
        print(t)
        if t in ['jpg', 'jpeg', 'png', 'gif', 'bmp']:
            t = os.path.join(a, e)
            f=Image.open(t)
            f = f.filter(b[c])
            c += 1
            if f.mode == "RGBA":
                f = f.convert("RGB")
            f.save("save/"+e)

#11.2

a=r"C:\Users\Goltz\Desktop\11\pes"
A=os.listdir(a)
for e in A:
    if os.path.isfile(e):
        t=os.path.join(a,e)
        t=t.split(".")[-1].lower()
        print(t)
        if t in ['jpg', 'jpeg', 'png', 'gif', 'bmp']:
            t=os.path.join(a,e)
            with Image.open(t) as f:
                f.show()
                print("razreshenie",f.size,"\n","format",f.format,"\n","tsvet model",f.mode)

#11.3
p=0
with open(r"C:\Users\Goltz\Desktop\11\data.csv",'r') as a:
    with open(r"C:\Users\Goltz\Desktop\11\data.fin.csv", 'w') as f:
        next(a)
        for e in a:
            e=e.split(",")
            e=list(e)
            r=e[0]
            t=int(e[1])
            y=int(e[2])
            print(r,t,y)
            u=(t)*(y)
            p=p+u
            print(f"{r} - {t} шт за {y} руб")
            f.write(f"{r} - {t} шт за {y} руб\n")
        print(f'контрольная сумма {p} руб')
        f.write(f'контрольная сумма {p} руб')