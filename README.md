# Folder-Hunter
<img width="751" height="506" alt="Screen Shot 2026-05-23 at 13 50 13" src="https://github.com/user-attachments/assets/7fd2136b-f7b5-4410-ba08-077a10ca7d42" />

# Simple Folder Hunter

Простий GUI-додаток на Python для пошуку та видалення порожніх папок.
Інтерфейс побудований на `customtkinter`.

---

## Можливості

* Вибір папки через графічний інтерфейс
* Пошук порожніх директорій
* Ігнорування системних папок:

  * `$RECYCLE.BIN`
  * `System Volume Information`
* Видалення всіх знайдених порожніх папок
* Темна тема (`dark mode`)
* Простий та зрозумілий UI

---

## Скріншот

```text
Simple Empty Folder Hunter
----------------------------------
[ Select Folder ] [ шлях до папки ]

Тут з'являться знайдені порожні папки...

[ Scan ] [ Clean All ]

Знайдено папок: 0
```

---

# Встановлення

## 1. Клонувати або завантажити проєкт

```bash
git clone https://github.com/yourusername/simple-folder-hunter.git
cd simple-folder-hunter
```

---

## 2. Встановити залежності

```bash
pip install customtkinter
```

---

# Запуск

```bash
python main.py
```

---

# Структура проєкту

```text
simple-folder-hunter/
│
├── main.py
└── README.md
```

---

# Як працює програма

## Пошук порожніх папок

Програма обходить директорії знизу догори (`topdown=False`) через `os.walk()`.

Папка вважається порожньою якщо:

* у ній немає файлів
* у ній немає підпапок
* системні папки ігноруються

---

# Основні методи

## `select_folder()`

Відкриває діалог вибору папки.

---

## `find_empty_folders(start_path)`

Шукає всі порожні папки у вибраній директорії.

---

## `scan()`

Запускає пошук порожніх папок та оновлює UI.

---

## `clean_all()`

Видаляє всі знайдені порожні папки після підтвердження користувача.

---

# Використані бібліотеки

| Бібліотека      | Призначення                |
| --------------- | -------------------------- |
| `os`            | Робота з файловою системою |
| `shutil`        | Видалення папок            |
| `tkinter`       | Стандартний GUI            |
| `customtkinter` | Сучасний UI для Tkinter    |

---

# Приклад коду запуску

```python
if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = SimpleFolderHunter()
    app.mainloop()
```

---

# Можливі покращення

* Видалення лише вибраних папок
* Логування результатів
* Підтримка багатопоточності
* Індикатор прогресу сканування
* Експорт результатів у `.txt`

---

# Ліцензія

MIT License

---


