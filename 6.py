#6.1

def f(x):
    if x%3==0:
        print(f"не мандражуй {x} нам подходит")
    else:
        print(f"не ватс {x} фуфел полный")
x=int(input("mazani chislo: "))
a=f(x)

#6.2
def f(x):
    try:
        e=100/int(x)
        return e
    except ZeroDivisionError,NameError,TypeError,ValueError,UnboundLocalError:
        print("Эээ- лабубик ты смотри, что мажешь!")

x=(input("mazani chislo: "))
print(f(x))

#6.3
def f(x,y,z):
    if  x>30 or y>12 or x<0 or y<0:
        print("не ну ты в натуре ливер")
    elif x*y==(z%100):
        print('try')
        print("лабубик эта дата просто бести")
    else:
        print("false")
        print("обычная дата... ни чего интересного")
x=int(input("mazani day: "))
y=int(input("mazani month: "))
z=int(input("mazani year: "))
f(x,y,z)

#6.4
def f(x):
    r=0
    t=0
    g=1
    if len(x)%2==0:
        for a in x:
            if g<=(len(x)/2):
                r=r+int(a)
                g=g+1
            elif g>(len(x)/2):
                t=t+int(a)
                g=g+1
        if r==t:
            print("в этот раз тебе удалось схватить удачу за её вертлявую гриву!")
        else:
            print("твой билет!. и древестный лист!.    ОДНО И ТОЖЕ!")
    else:
        print("что за фуфел у тебя")


x=(input("mazani: "))
f(x)
