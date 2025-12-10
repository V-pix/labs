from tkinter import *
from tkinter import ttk, messagebox, filedialog, scrolledtext


window = Tk()
window.title("Шакалова Вероника Николаевна")
window.geometry("600x600")

tab_control = ttk.Notebook(window)
tab_calculate = ttk.Frame(tab_control)
tab_checkboxes = ttk.Frame(tab_control)
tab_text = ttk.Frame(tab_control)
tab_control.add(tab_calculate, text="Калькулятор")
tab_control.add(tab_checkboxes, text="Чекбоксы")
tab_control.add(tab_text, text="Текст")
tab_control.pack(expand=1, fill="both")

lbl = Label(tab_calculate, text="Число 1:")
lbl.grid(row=0, column=0, padx=10, pady=10)
lbl = Label(tab_calculate, text="Операция:")
lbl.grid(row=0, column=1, padx=10, pady=10)
lbl = Label(tab_calculate, text="Число 2:")
lbl.grid(row=0, column=2, padx=10, pady=10)

entry_1 = Entry(tab_calculate, width=10)
entry_2 = Entry(tab_calculate, width=10)
entry_1.grid(row=1, column=0, padx=10, pady=5)
entry_2.grid(row=1, column=2, padx=10, pady=5)

combo = ttk.Combobox(tab_calculate, width=1, state="readonly")
combo["values"] = ("+", "-", "*", "/")
combo.current(0)
combo.grid(row=1, column=1, padx=10, pady=5)

label_result = Label(tab_calculate, text="Результат: ")
label_result.grid(row=3, column=0, columnspan=3, pady=15)


def calculate():
    try:
        a = float(entry_1.get())
        b = float(entry_2.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа")
        return
    operator = combo.get()
    try:
        if operator == "+":
            res = a + b
        elif operator == "-":
            res = a - b
        elif operator == "*":
            res = a * b
        elif operator == "/":
            if b == 0:
                messagebox.showerror("Ошибка", "Деление на ноль")
                return
            res = a / b
        else:
            messagebox.showerror("Ошибка", "Неизвестная операция")
            return
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))
        return

    label_result.config(text=f"Результат: {res}")


btn_calc = Button(tab_calculate, text="Посчитать", command=calculate)
btn_calc.grid(row=2, column=0, columnspan=3, pady=10)


chk_var1 = BooleanVar()
chk_var2 = BooleanVar()
chk_var3 = BooleanVar()

chk_1 = ttk.Checkbutton(tab_checkboxes, text="Первый", variable=chk_var1)
chk_2 = ttk.Checkbutton(tab_checkboxes, text="Второй", variable=chk_var2)
chk_3 = ttk.Checkbutton(tab_checkboxes, text="Третий", variable=chk_var3)

chk_1.grid(row=0, column=0, padx=10, pady=10)
chk_2.grid(row=1, column=0, padx=10, pady=10)
chk_3.grid(row=2, column=0, padx=10, pady=10)


def show_choice():
    chosen = []
    if chk_var1.get():
        chosen.append("первый вариант")
    if chk_var2.get():
        chosen.append("второй вариант")
    if chk_var3.get():
        chosen.append("третий вариант")
    if not chosen:
        messagebox.showinfo("Выбор", "Вы ничего не выбрали")
    elif len(chosen) == 1:
        messagebox.showinfo("Выбор", f"Вы выбрали {chosen[0]}")
    else:
        messagebox.showinfo("Выбор", "Вы выбрали: " + ", ".join(chosen))


btn_choice = Button(tab_checkboxes, text="Показать выбор", command=show_choice)
btn_choice.grid(row=3, column=1, padx=10, pady=10)


txt = scrolledtext.ScrolledText(tab_text, width=70, height=20, wrap=WORD)
txt.pack(expand=1, fill="both", padx=10, pady=10)


def open_text_file():
    file_path = filedialog.askopenfilename(
        title="Открыть текстовый файл",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*")),
    )
    if not file_path:
        return
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось открыть файл:\n{e}")
        return
    txt.delete("1.0", END)
    txt.insert("1.0", content)


menu = Menu(window)
menu_item = Menu(menu, tearoff=0)
menu.add_cascade(label="Файл", menu=menu_item)
window.config(menu=menu)

menu_item.add_command(label="Загрузть текст из файла", command=open_text_file)
menu_item.add_separator()
menu_item.add_command(label="Выход", command=window.quit)


window.mainloop()
