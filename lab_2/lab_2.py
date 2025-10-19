# 9 вариант
import math


x = int(input("Введите первое целое число x: "))
y = int(input("Введите второе целое число y: "))
z = int(input("Введите третье целое число z: "))

if x <= 0:
    print("x должно быть больше 0")
elif y <= 0 or y == x:
    print("y должно быть больше 0 и не равно x")
else:
    s = abs(
        math.exp(math.log(y) - x * math.log(x))
        - math.copysign(abs(y / x) ** (1 / 3), y / x)
    ) + (y - x) * (math.cos(y) - z / (y - x)) / (1 + (y - x) ** 2)

    print("S =", round(s, 5))
