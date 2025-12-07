# Вариант 9
# 1 Для целочисленной квадратной матрицы найти число элементов,
# кратных k, и наибольший из этих элементов.


def get_count_and_max(A, k):
    n = len(A)
    count = 0
    maximum = None

    for i in range(n):
        for j in range(n):
            if A[i][j] % k == 0:
                count += 1
                if maximum is None or A[i][j] > maximum:
                    maximum = A[i][j]
    return count, maximum


if __name__ == "__main__":
    n = int(input("Введите размер квадратной матрицы n: "))
    k = int(input("Введите целое число k: "))

    A = []

    for i in range(n):
        B = []
        for j in range(n):
            B.append(int(input(f"Введите элемент матрицы[{i}][{j}]: ")))
        A.append(B)

    print("\nИсходная матрица:")
    for i in range(n):
        for j in range(n):
            print(A[i][j], end=" ")
        print()
    count, maximum = get_count_and_max(A, k)
    print("\nКоличество элементов, кратных k:", count)
    if count > 0:
        print("Наибольший из элементов, кратных k:", maximum)
    else:
        print("Элементов, кратных k, в матрице нет.")
