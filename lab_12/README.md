# GitHub API (GUI)

Вводите в поле:

- username (например `Kubernetes`, `Automattic`)
- **owner/repo** (например `Automattic/wp-calypso`)
- **ссылку на репозиторий** (например `https://github.com/Automattic/wp-calypso`)

Программа автоматически берёт **owner** и запрашивает:

`https://api.github.com/users/{owner}`

Сохраняет в новый файл только поля:

- company
- created_at
- email
- id
- name
- url

## Запуск

```bash
pip install -r requirements.txt
python main.py
```

Результат сохраняется в папку `output/`.

## Пример

### 9 Вариант
 Automattic WordPress Calypso
JavaScript и API-интерфейс для WordPress.com
```bash
Репозиторий: github.com/Automattic/wp-calypso
Веб-сайт: developer.wordpress.com/calypso
```