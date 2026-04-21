# 9 вариант
# S = f + v, f < 4,v > 6
# S = k * k  ,v < 6
# S = 2v,в остальных

f = float(input("Введите число f: "))
v = float(input("Введите число v: "))
k = float(input("Введите число k: "))

if f < 4 and v > 6:
    S = f + v
elif v < 6:
    S = k**2
else:
    S = 2 * v

print("S =", S)
