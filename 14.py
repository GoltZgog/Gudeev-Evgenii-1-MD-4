#14.1

class Restaurant:
    def __init__(self,restaurant_name,cuisine_type,sost,reyt):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.sost = sost
        self.reyt = reyt
    def describe_restaurant(self):
        print(f"чресторан {self.restaurant_name} c {self.cuisine_type} мазьнёй и рейтинг его {self.reyt}")
    def sort_restaurant(self):
        print(f"чресторан {self.restaurant_name} {self.sost}")
    def reyt1(self):
        print(f"рейтинг этой забигаловки={self.reyt}")

chrestoran=Restaurant("newRestaurant","чайна","открыт","10 из 5")
print(chrestoran.restaurant_name)
print(chrestoran.cuisine_type)
chrestoran.describe_restaurant()
chrestoran.sort_restaurant()
chrestoran.reyt1()

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,sost,reyt,flavors):
        super().__init__(restaurant_name,cuisine_type,sost,reyt)
        self.flavors = flavors
    def Flavors(self):
        print(f"це такие сорта имеются {self.flavors}")

s=int(input("скок сортов тебе надо: "))
S=0
e=[]
while S<s:
    r=input("ну давай перчисляй быстрее(по одному): ")
    e.append(r)
    S+=1
icecafe=IceCreamStand("IceCreamStand","необычная","да","чёткий",e)
icecafe.describe_restaurant()
icecafe.Flavors()

#14.2
a=input("описания локации:  ")
b=input("времени работы:  ")
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,sost,reyt,flavors,koment,time):
        super().__init__(restaurant_name,cuisine_type,sost,reyt)
        self.flavors = flavors
        self.koment = koment
        self.time = time
    def Flavors(self):
        print(f"це такие сорта имеются {self.flavors}")

    def Flavors_add(self,add):
        if not (add in self.flavors):
            self.flavors.append(add)
            print(f"вацочек всё в ажуре {add} уже в списке({self.flavors}) притаился")
        else:
            print(f"Эээ чё ты делаешь {add} уже и так в списке!")

    def Flavors_remove(self,remove):
        if remove in self.flavors:
            self.flavors.remove(remove)
            print(f"хехех ща мы {remove} приговорим")

    def chek(self,d):
        if d in self.flavors:
            print(f"да без б {d} есть в наличаи из {self.flavors}")
        else:
            print(f"не {d} нет такого")

    def stick(self,m):
        if m in self.flavors:
            print(f"без б эскимо с {m} будет тебе!")
        else:
            print(f"не ватс эскимо не будэ нет у нас {m}")
    def soft(self,m):
        if m in self.flavors:
            print(f"без б мягкое мороженое с {m} будет тебе!")
        else:
            print(f"не ватс мягкое мороженое не будэ нет у нас {m}")
s=int(input("скок сортов тебе надо: "))
S=0
e=[]
while S<s:
    r=input("ну давай перчисляй быстрее(по одному): ")
    e.append(r)
    S+=1

icecafe=IceCreamStand("IceCreamStand","необычная","да","чёткий",e,a,b)

S=input("мазанул лишний сорт, убрать хочешь иль наоборот добавить?(да/нет):  ")
while S=="да" or S=="выйти":
    d=input("добавить/убрать/выйти:  ")
    if d=="убрать":
        d = input("какой сорт приговоришь?: ")
        icecafe.Flavors_remove(d)
        S=input("чёнить ещё изменишь?(да/нет):  ")
    elif d=="добавить":
        d = input("мазани?:  ")
        icecafe.Flavors_add(d)
        S=input("чёнить ещё изменишь?(да/нет):  ")
    elif d=="выйти":
        break
icecafe.describe_restaurant()
icecafe.Flavors()

d=input("морожку хочешь?(да/нет):  ")
if d=="да":
    d=input("какую хочешь(эскимо/мягкое)?:  ")
    if d=="эскимо":
        m1=input("сорт:  ")
        icecafe.stick(m1)
    elif d=="мягкое":
        m1 = input("сорт:  ")
        icecafe.soft(m1)
elif d=="нет":
    print("богатым будешь")

d=input('проверка налячия сорта, мазани сорт:  ')
icecafe.chek(d)