# Вариант 9
# 1 Из заданного числа вычли сумму его цифр. Из результата вновь вычли сумму
# его цифр и т. д. Через сколько таких действий получится нуль?


def get_sum_digits(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n = n // 10
    return sum


n = float(input("Введите число n: "))

if n <= 0:
    print("Должно быть n > 0")
else:
    steps = 0
    while n > 0:
        n = n - get_sum_digits(n)
        steps += 1

    print("Количество действий до нуля:", steps)
