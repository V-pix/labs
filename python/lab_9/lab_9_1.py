# 2 Дано натуральные числа a,b Вычислить остаток от деления a на b


def get_remainder(a, b):
    if a < b:
        return a
    return get_remainder(a - b, b)


a = int(input("Введите делимое натуральное число a: "))
b = int(input("Введите делитель натуральное число b: "))

if a <= 0 or b <= 0:
    print("Нужно a ≥ 0 и b ≥ 0")
else:
    result = get_remainder(a, b)
    print("Остаток от деления a на b:", result)
