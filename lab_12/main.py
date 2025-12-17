import json
import os
import re
from tkinter import *
from tkinter import messagebox
import requests


FIELDS = ("company", "created_at", "email", "id", "name", "url")


def extract_owner_from_input(input: str) -> str:
    clean_input = input.strip()
    url_match = re.search(r"github\.com/([^/\s]+)(?:/([^/\s]+))?", clean_input)
    if url_match:
        return url_match.group(1)
    if "/" in clean_input:
        owner_part = clean_input.split("/", 1)[0].strip()
        if owner_part:
            return owner_part
    return clean_input


def fetch_user(owner: str) -> dict:
    url = f"https://api.github.com/users/{owner}"
    headers = {"Accept": "application/vnd.github+json"}
    response = requests.get(url, headers=headers, timeout=15)
    try:
        data = response.json()
    except Exception:
        data = {}
    if response.status_code >= 400:
        message = data.get("message") or f"HTTP {response.status_code}"
        raise RuntimeError(f"Ошибка запроса: {message}")
    return data


def take_required_fields(full_data: dict) -> dict:
    return {field: full_data.get(field) for field in FIELDS}


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Получения данных с Git")
        self.geometry("760x440")
        self.resizable(True, True)
        self._build_ui()

    def _build_ui(self):
        frame = Frame(self, padx=12, pady=12)
        frame.pack(expand=1, fill="both")
        label_input = Label(
            frame, text="Введите username / owner/repo / ссылку на репозиторий GitHub:"
        )
        label_input.grid(row=0, column=0)
        self.entry = Entry(frame, width=46)
        self.entry.grid(row=1, column=0, pady=6)
        self.entry.insert(0, "https://github.com/Automattic/wp-calypso")

        btn = Button(frame, text="Получить и сохранить", command=self.on_fetch)
        btn.grid(row=1, column=1, padx=10, pady=6)
        frame.grid_columnconfigure(0, weight=1)

        self.text = Text(frame, wrap="word", height=18)
        self.text.grid(row=2, column=0, columnspan=2, sticky="nsew", pady=(12, 0))
        frame.grid_rowconfigure(2, weight=1)

    def on_fetch(self):
        raw = self.entry.get().strip()
        if not raw:
            messagebox.showwarning("Пустой ввод", "Введите значение.")
            return
        owner = extract_owner_from_input(raw)
        self.text.delete("1.0", END)
        self.text.insert(
            END, f"Определён владелец (owner): {owner}\nЗапрос к GitHub API...\n"
        )

        try:
            data = fetch_user(owner)
            required_fields = take_required_fields(data)
            pretty_json = json.dumps(required_fields, ensure_ascii=False, indent=2)
            self.text.delete("1.0", END)
            self.text.insert(END, pretty_json)

            out_dir = os.path.join(os.path.dirname(__file__), "output")
            os.makedirs(out_dir, exist_ok=True)
            out_path = os.path.join(out_dir, f"{owner}_user.json")
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(required_fields, f, ensure_ascii=False, indent=2)
            messagebox.showinfo("Готово", f"Сохранено: {out_path}")

        except Exception as e:
            self.text.delete("1.0", END)
            self.text.insert(END, f"Ошибка: {e}")
            messagebox.showerror(f"Ошибка", {e})


if __name__ == "__main__":
    App().mainloop()
