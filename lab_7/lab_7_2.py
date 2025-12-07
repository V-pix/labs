# Вариант 9
# 2 Даны 3 различных массива целых чисел. В каждом массиве найти
# произведение элементов и среднеарифметическое значение.


def input_array(name):
    array_len = int(input(f"\nВведите количество элементов массива {name}: "))
    array = []
    print(f"Введите элементы массива {name} (целые числа):")
    for i in range(array_len):
        array.append(int(input(f"{name}[{i}] = ")))
    return array


def get_multiplication(array):
    result = 1
    for i in array:
        result *= i
    return result


def get_average(array):
    return sum(array) / len(array)


array_1 = input_array("array_1")
array_2 = input_array("array_2")
array_3 = input_array("array_3")

for name, array in (("array_1", array_1), ("array_2", array_2), ("array_3", array_3)):
    print(f"\nМассив {name}: {array}")
    print("Произведение элементов:", get_multiplication(array))
    print("Среднее арифметическое:", get_average(array))
