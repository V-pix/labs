import os
import sys


CURRENT_DIR = os.path.dirname(__file__)
LAB8_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "lab_8"))
if LAB8_DIR not in sys.path:
    sys.path.append(LAB8_DIR)

from lab_8_1 import get_count_and_max
from lab_8_2 import get_max_abs_and_new_matrix


INPUT_FILE = "Shakalova_Veronika_UM-252_vvod.txt"
OUTPUT_FILE = "Shakalova_Veronika_UM-252_vivod.txt"


def read_data(filename):
    path = os.path.join(CURRENT_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    n = int(lines[0].split("=")[1])
    k = int(lines[1].split("=")[1])
    A = []
    index_line = 2
    for i in range(n):
        row = []
        for j in range(n):
            value = int(lines[index_line])
            row.append(value)
            index_line += 1
        A.append(row)
    return n, k, A


def write_results(filename, n, k, A, count, maximum, max_abs, new_matrix):
    path = os.path.join(CURRENT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write("Исходная матрица:\n")
        for row in A:
            line = " ".join(str(x) for x in row)
            f.write(line + "\n")
        f.write("\n")
        f.write("Задача 8.1\n")
        f.write(f"n = {n}, k = {k}\n")
        f.write(f"Количество элементов, кратных k: {count}\n")
        if count > 0:
            f.write(f"Наибольший из элементов, кратных k: {maximum}\n")
        else:
            f.write("Элементов, кратных k в матрице нет.\n")
        f.write("\n")

        f.write("Задача 8.2\n")
        f.write(f"Наибольший по модулю элемент: {max_abs}\n")
        f.write("Новая матрица n-1:\n")
        for row in new_matrix:
            line = " ".join(str(x) for x in row)
            f.write(line + "\n")


def main():
    n, k, A_int = read_data(INPUT_FILE)
    count, maximum = get_count_and_max(A_int, k)
    A_float = []
    for row in A_int:
        new_row = []
        for value in row:
            new_row.append(float(value))
        A_float.append(new_row)
    max_abs, new_matrix = get_max_abs_and_new_matrix(A_float)
    write_results(OUTPUT_FILE, n, k, A_int, count, maximum, max_abs, new_matrix)
    print("Результаты записаны в файл", OUTPUT_FILE)


if __name__ == "__main__":
    main()
