import random

j=1
a1=int(input("Минимальное число диапазона: "))
a2=int(input("Максимальное число диапазона: "))
r=random.randint(a1, a2)
b=int(input("Введи свое число: "))
while b!=r:
    if b<r:
        print("Мое число больше")
    elif b>r:
        print("Мое число меньше")
    b=int(input("Введи новое число: "))
    j=j+1
print("Молодец! Ты угадал число!")
print("Число попыток:", j)
