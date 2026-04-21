from idlelib.configdialog import font_sample_text

from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os, shutil,csv
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