# Вариант 9
# Определить, сколько раз в тексте встречается заданное слово.

text = input("Введите текст: ")
word = input("Введите слово для поиска: ")

for i in ",.!?;:-()\"'":
    text = text.replace(i, " ")

count = text.lower().split().count(word.lower())

print(f"Слово '{word}' встречается {count} раза")
