# По данному натуральному n вычислите сумму 1^3+2^3+3^3+...+n^3.

n = int(input("Введите n целое положительное: "))

if n < 1:
    print("n должно быть ≥ 1")
else:
    total = 0
    for i in range(1, n + 1):
        total += i**3
    print("Сумма =", total)
