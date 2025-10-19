# Даны три целых числа. Выбрать из них те, которые принадлежат
# интервалу[1,3].

first_number = int(input("Введите первое целое число: "))
second_number = int(input("Введите второе целое число: "))
third_number = int(input("Введите третье целое число: "))

numbers = [first_number, second_number, third_number]
result = [i for i in numbers if (1 <= i <= 3)]

print("Числа принадлежащие интервалу [1, 3]:", result)
