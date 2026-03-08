import random

#7.1
x=[9,10,42,3600,5600]
y=int(input("mazani: "))
if y in x:
    print("this nice men")
else:
    print("no good-no respect")
    
#7.2
a=0
c=[]
while a<12:
    x=(input("mazani: "))
    if x=='stop':
        break
    else:
        c.append(x)
for i in c:
    a=0
    for j in c:
        if i==j:
            a=a+1
        if a>=2:
            c.remove(j)
    if a>=2:
        print(i,"вот эти ошибки природы")

#7.3
x=("пн","вт","ср","чт","пт","сб","вс")
y=int(input("mazani skok vihodnih hochesh: "))
g=[]
h=[]
z=7-y
u=1
for i in x:
    if u<z:
        u=u+1
        g.append(i)
    else:
        h.append(i)
h.reverse()
g.reverse()
print("vihodnie", h,"\n","budni",g)

#7.4
#a=1
#x=[]
#y=[]
#while a<10:
    #x1=input("mazani familiy grup1: ")
    #x.append(x1)
    #y1=input("mazani familiy grup2: ")
    #y.append(y1)
    #a=a+1
x=["Иванов","Петров","Сидоров","Смирнов","Кузнецов","Попов","Васильев","Соколов","Михайлов","Новиков"]
y=["Фёдоров","Морозов","Волков","Алексеев","Лебедев","Семёнов","Егоров","Павлов","Козлов","Степанов"]
z=[]
r=random.sample(range(1,10),5)
t=random.sample(range(1,10),5)
for i in r:
    z.append(x[i])
for i in t:
    z.append(y[i])
z=tuple(z)
print("grupa1",x,"\n","grupa2",y,"\n","sport komanda", z, "\n","dlina",len(z),"\n","Иванов", z.count("Иванов"))