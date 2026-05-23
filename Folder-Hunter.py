import os
import shutil
import sys
import tkinter as tk
from tkinter import filedialog, messagebox

try:
    import customtkinter as ctk
except ImportError:
    print("Missing dependency: customtkinter. Install with: pip install customtkinter", file=sys.stderr)
    sys.exit(1)
class SimpleFolderHunter(ctk.CTk):
    """Проста версія Empty Folder Hunter для навчання"""
    IGNORED_DIRS = {"$RECYCLE.BIN", "System Volume Information"}
    def __init__(self):
        super().__init__()
        self.title("Simple Folder Hunter")
        self.geometry("760x520")
        self.selected_path = ""
        self.empty_folders = []
        self._build_ui()
    def _build_ui(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        title = ctk.CTkLabel(
            self,
            text="Simple Empty Folder Hunter",
            font=ctk.CTkFont(size=22, weight="bold")
        )
        title.grid(row=0, column=0, padx=12, pady=(12,6), sticky="w")
        top = ctk.CTkFrame(self)
        top.grid(row=1, column=0, padx=12, pady=6, sticky="ew")
        top.grid_columnconfigure(1, weight=1)
        select_btn = ctk.CTkButton(top, text="Select Folder", command=self.select_folder)
        select_btn.grid(row=0, column=0, padx=8, pady=8)
        self.path_var = tk.StringVar(value="Оберіть папку для сканування")
        path_entry = ctk.CTkEntry(top, textvariable=self.path_var)
        path_entry.grid(row=0, column=1, padx=(0, 8), pady=8, sticky="ew")
        self.results_box = ctk.CTkTextbox(self)
        self.results_box.grid(row=2, column=0, padx=12, pady=6, sticky="nsew")
        self.results_box.insert("1.0", "Тут з'являться знайдені порожні папки...")
        self.results_box.configure(state="disabled")
        bottom = ctk.CTkFrame(self)
        bottom.grid(row=3, column=0, padx=12, pady=(6,12), sticky="ew")
        bottom.grid_columnconfigure(2, weight=1)
        scan_btn = ctk.CTkButton(
            bottom, 
            text="Scan",
            fg_color="#2563EB",
            hover_color="#1D4ED8",
            command=self.scan,
        )
        scan_btn.grid(row=0, column=0, padx=(8, 6), pady=8)
        clean_btn = ctk.CTkButton(
            bottom,
            text="Clean All",
            fg_color="#DC2626",
            hover_color="#B91C1C",
            command=self.clean_all,
        )
        clean_btn.grid(row=0, column=1, padx=(0, 8), pady=8)
        self.status_var = tk.StringVar(value="Знайдено папок: 0")
        status = ctk.CTkLabel(bottom, textvariable=self.status_var, anchor="w")
        status.grid(row=0, column=2, padx=8, pady=8, sticky="ew")
    def select_folder(self):
        """Вибір стартової папки."""
        folder = filedialog.askdirectory(title="Оберіть папку")
        if folder:
            self.selected_path = folder
            self.path_var.set(folder)
            self.empty_folders = []
            self._show_results([])
            self.status_var.set("Знайдено папок: 0")
    def find_empty_folders(self, start_path):
        """Шукає парожні папки (обхід знизу дороги)."""
        result = []
        for root, dirs, files in os.walk(start_path, topdown=False):
            folder_name = os.path.basename(root)
            if folder_name in self.IGNORED_DIRS:
                continue
            normal_dirs = [d for d in dirs if d not in self.IGNORED_DIRS]
            if not files and not normal_dirs:
                result.append(root)
        return result
    def scan(self):
        """Запукс пошуку порожніх папок."""
        if not self.selected_path:
            messagebox.showwarning("Увага", "Спочатку натисніть Select Folder.")
            return
        if not os.path.isdir(self.selected_path):
            messagebox.showerror("Помилка", "Обрана папка недоступна.")
            return
        self.empty_folders = self.find_empty_folders(self.selected_path)
        self._show_results(self.empty_folders)
        self.status_var.set(f"Знайдено папок: {len(self.empty_folders)}")
    def clean_all(self):
        """Видаляє всі знайдені порожні папки після підтвердження."""
        if not self.empty_folders:
            messagebox.showinfo("Інформація", "Немає папок для видалення.")
            return
        ok = messagebox.askyesno("Підтвердження", "Видалити всі знайдені порожні папки?")
        if not ok:
            return
        deleted = 0
        for path in self.empty_folders:
            try:
                shutil.rmtree(path)
                deleted += 1
            except (FileNotFoundError, PermissionError, OSError):
                pass
        self.empty_folders = []
        self._show_results([])
        self.status_var.set("Знайдено папок: 0")
        messagebox.showinfo("Готово", f"Видалено {deleted} порожніх папок.")
    def _show_results(self, paths):
        """Показує результати в текстовому полі."""
        self.results_box.configure(state="normal")
        self.results_box.delete("1.0", "end")
        if paths:
            self.results_box.insert("end", "\n".join(paths))
        else:
            self.results_box.insert("end", "Порожні папки не знайдено.")
        self.results_box.configure(state="disabled")
if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    app = SimpleFolderHunter()
    app.mainloop()