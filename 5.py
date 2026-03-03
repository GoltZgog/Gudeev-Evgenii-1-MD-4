import random

#5.1

a=int(input("mazani:"))
d=1
c=""
while d<=a:
    print("d: ", d)
    d+=1
    b=input("mazani slovechko:")
    c=c+" "+b
print(c)


#5.2
d=0
c=""
while d<=1:
    b=input("mazani slovechko:")
    if b=="stop" or b=="стоп":
        break
    c=c+" "+b
print(c)

#5.3
b=input("mazani:")
r=0
for a in b:
    if a=="ф":
        r=1
if r==1:
    print("Ого! Это редкое слово!")
else:
    print("Эх, это не очень редкое слово...")

#5.4
d=0
g=0
while d<=1:
    a=random.randint(1,100)
    b=random.randint(1,100)
    c=a+b
    v=int(input(f'{a}+{b}='))
    if v==c:
        g+=1
    else:
        break
print(g)