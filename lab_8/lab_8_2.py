# 2 В данной действительной квадратной матрице порядка n найти
# наибольший по модулю элемент. Получить квадратную матрицу порядка
# n — 1 путем отбрасывания из исходной матрицы строки и столбца, на
# пересечении которых расположен элемент с найденным значением.


def get_max_abs_and_new_matrix(A):
    n = len(A)
    max_abs = abs(A[0][0])
    max_i = 0
    max_j = 0

    for i in range(n):
        for j in range(n):
            if abs(A[i][j]) > max_abs:
                max_abs = abs(A[i][j])
                max_i = i
                max_j = j

    B = []
    for i in range(n):
        if i == max_i:
            continue
        C = []
        for j in range(n):
            if j == max_j:
                continue
            C.append(A[i][j])
        B.append(C)
    return max_abs, B


if __name__ == "__main__":
    n = int(input("Введите размер квадратной матрицы n: "))

    A = []

    for i in range(n):
        B = []
        for j in range(n):
            B.append(float(input(f"Введите элемент матрицы[{i}][{j}]: ")))
        A.append(B)

    print("\nИсходная матрица:")
    for i in range(n):
        for j in range(n):
            print(A[i][j], end=" ")
        print()
    max_abs, B = get_max_abs_and_new_matrix(A)
    print(f"\nНаибольший по модулю элемент: {max_abs}")
    print("\nНовая матрица n-1:")
    for i in range(n - 1):
        for j in range(n - 1):
            print(B[i][j], end=" ")
        print()
