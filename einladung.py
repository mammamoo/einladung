"""num = int(input("Если в км: "))
num_1 = int(input("Если в м: "))
h = num * 1000
m = num_1 * 100
print("Результат в км:", h)
print("Результат в м:", m)

a = int(input("Введите любое число: "))
b = int(input("Введите любое число: "))
act = input("Введите действие:")
def arithmetic(a,b,act):
    if act == "+":
        return a+b
    elif act == "-":
        return a-b
    elif act == "*":
        return a*b
    elif act == "/":
        return a/b
    else:
        print("Неизвестная операция")
print(arithmetic(a,b,act))

a = int(input("Введите сумму вклада: "))
years = int(input("Введите срок: "))
#b = ((a * 0.1) * years) + a
def bank (a,years):
    if years > 0:
        return ((a * 0.1) * years) + a
print(bank(a,years))

i = 0
while i < 10:
    print(i, " ")
    i += 2

a = 100
while a >= 10:
    print(a, " ")
    a -= 10
list_my_group = ["Adakhan", "Turan", "Janka", [1, 2, 3]]
list_my_group[1] = "Turan jindi"
list_my_group.append("Jarkynai")
list_my_group.remove([1, 2, 3])
list_my_group.insert(0, "Adakhan fu")
print(list_my_group[::2])
for s in list_my_group:
    print(s, " ")

n = tuple ("Hello")
print((n[0]))

d = {"test": 45,
     "word": 46}
print(d["test"])
c = dict(f=5, s=6)
print(c["f"])
dictionary = dict.fromkeys([4, 7, 6], 'c')
print(dictionary)

#множество, можно вывести в случайном порядке и не будут повторяться одинаковые элементы
a = set("hello")
print(a)
s = {"x", 'c', 5, 6, 5}
print(s)
#мы не можем изменять
h = frozenset('fuck')
print(h)
#функция
mult = lambda x,y: x*y
print(mult(6,5))
#modul

import math
print(math.e)

class Car:
    name = "None"
    height = 1000
    speed = 200.00

    def set(self, name, height, speed):
        self.name = name
        self.height = height
        self.speed = speed

class Truck(Car):
    wheels = 8

man = Truck()
man.wheels = 12
man.set("Man", 4500, 140.5)
print(man.height)

audi = Car ()
audi.set("Audi", 1450, 320.30)
print(audi.name)
print(audi.height)
print(audi.speed)

vw = Car ()
vw.set("VW", 1500, 350.30)
print(vw.name)
print(vw.height)
print(vw.speed)"""