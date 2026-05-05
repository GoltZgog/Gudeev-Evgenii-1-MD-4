"""#13.1
from sympy import elliptic_e


class Restaurant:
    def __init__(self,restaurant_name,cuisine_type,sost,):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.sost = sost
    def describe_restaurant(self):
        print(f"чресторан {self.restaurant_name} c {self.cuisine_type} мазьнёй")
    def sort_restaurant(self):
        print(f"чресторан {self.restaurant_name} {self.sost}")
chrestoran=Restaurant("newRestaurant","чайна","открыт")
print(chrestoran.restaurant_name)
print(chrestoran.cuisine_type)
chrestoran.describe_restaurant()
chrestoran.sort_restaurant()

#13.2
A=0
B=0
C=0
for i in range(3):
    a=input("погоняло твой шарашкеной конторы: ")
    b=input("чё за мазьня у тебя: ")
    c=input("ну чё... сегодня открыто?: ")
    if i==0:
        A=Restaurant(a,b,c)
    elif i==1:
        B=Restaurant(a,b,c)
    elif i==2:
        C=Restaurant(a,b,c)
    else:
        break
A.sort_restaurant()
B.sort_restaurant()
C.sort_restaurant()
"""
#13.3
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

j=input("оцени сам это место:  ")
chrestoran=Restaurant("newRestaurant","чайна","открыт",j)
chrestoran.describe_restaurant()
chrestoran.reyt1()

