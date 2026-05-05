import json, os

#12.1
data = """{
  "products": [
{
 "name": "Шоколад",
 "price": 50,
 "available": true,
 "weight": 100
},
{
 "name": "Кофе",
 "price": 100,
 "available": false,
 "weight": 250
},
{
 "name": "Чай",
 "price": 70,
 "available": true,
 "weight": 50
}
  ]
 }"""
dataa=json.loads(data)
for g in dataa['products']:
    if g["available"]==True:
        st="na meste"
    else:
        st="ne ma"
    print(f"Название: {g['name']} \nЦена: {g['price']} \nВес: {g['weight']} \nсостояние: {st}  ")

#12.2
data = """{
  "products": [
{
 "name": "Шоколад",
 "price": 50,
 "available": true,
 "weight": 100
},
{
 "name": "Кофе",
 "price": 100,
 "available": false,
 "weight": 250
},
{
 "name": "Чай",
 "price": 70,
 "available": true,
 "weight": 50
}
  ]
 }"""
dataa=json.loads(data)
for g in dataa['products']:
    if g["available"]==True:
        st="na meste"
    else:
        st="ne ma"
    print(f"Название: {g['name']} \nЦена: {g['price']} \nВес: {g['weight']} \nсостояние: {st}  ")

b=input("хотите добавить лот? (да/нет): ")
while b=="да":
    s = {}
    a=input("Имя товара: ")
    s["name"]=a
    a = input("Цена товара: ")
    s["price"] = a
    a = input("вес товара: ")
    s["weight"] = a
    a = input("наличие товара (да/нет): ")
    if a=="да":
        a=True
    elif a=="нет":
        a=False
    s["available"] = a
    dataa["products"].append(s)
    b=input("хотите добавить лот? (да/нет): ")

for g in dataa['products']:
    if g["available"]==True:
        st="na meste"
    else:
        st="ne ma"
    print(f"Название: {g['name']} \nЦена: {g['price']} \nВес: {g['weight']} \nсостояние: {st}  ")

data=json.dumps(dataa,indent=4,ensure_ascii=False)
print(data)

#12.3
with open(r"D:\aip\Gudeev-Evgenii-1-MD-4\12\ru-en.txt","w",encoding="utf-8") as l:
    a=r"D:\aip\Gudeev-Evgenii-1-MD-4\12\en-ru.txt"
    а=os.path.join(a)
    with open(a,'r',encoding='utf-8') as f:
        for s in f:
            v=[]
            s=s.split("-")
            d=f"{s[1].strip()} - {s[0]}\n"
            l.write(d)