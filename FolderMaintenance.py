import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Funkcja porządkująca pliki w wybranym folderze
def organize_files(folder_path):
    file_categories = {
        "Obrazki": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
        "PDF": [".pdf"],
        "Office": [".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx"],
        "Instalki": [".exe"],
        "ZIP": [".zip", ".rar"]
    }

    for category in file_categories.keys():
        category_path = os.path.join(folder_path, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isdir(file_path):
            continue

        file_ext = os.path.splitext(filename)[1].lower()
        moved = False
        for category, extensions in file_categories.items():
            if file_ext in extensions:
                shutil.move(file_path, os.path.join(folder_path, category, filename))
                moved = True
                break
        
        if not moved:
            other_folder = os.path.join(folder_path, "Inne")
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)
            shutil.move(file_path, os.path.join(other_folder, filename))

# Funkcja obsługująca wybór folderu
def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder_path)

# Funkcja obsługująca rozpoczęcie procesu porządkowania
def start_organizing():
    folder_path = folder_entry.get()
    if not folder_path:
        messagebox.showwarning("Błąd", "Najpierw wybierz folder!")
    elif not os.path.exists(folder_path):
        messagebox.showerror("Błąd", "Podany folder nie istnieje! Proszę wybrać istniejący folder.")
    else:
        organize_files(folder_path)
        messagebox.showinfo("Sukces", "Porządkowanie zakończone!")
        folder_entry.delete(0, tk.END)  # Czyszczenie pola po zakończeniu procesu

# Funkcja wyświetlająca informacje o autorze
def show_author_info():
    author_info = (
        "Autor programu: \n"
        "Marcin Tomaszewski\n"
        "Email: tomaszewsky.marcin@gmail.com\n"
        "GitHub: github.com/martom93\n"
        "\n"
        "Program do porządkowania plików w folderze.\n"
    )
    messagebox.showinfo("Informacje o autorze", author_info)

# Tworzenie GUI
root = tk.Tk()
root.title("Organizator Plików")

# Ustawienie okna na środku ekranu
root.update_idletasks()
width = 500
height = 150
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry(f"{width}x{height}+{x}+{y}")
root.resizable(False, False)  # Zablokowanie zmiany rozmiaru okna

# Etykieta informacyjna
label = tk.Label(root, text="Wybierz folder, który chcesz uporządkować:", padx=20, pady=10)
label.pack()

# Ramka na pole tekstowe i przycisk "Wybierz Folder"
folder_frame = tk.Frame(root)
folder_frame.pack(padx=20, pady=5)

# Pole do wyświetlania wybranej ścieżki folderu
folder_entry = tk.Entry(folder_frame, width=50)
folder_entry.pack(side=tk.LEFT, padx=5)

# Przycisk do wybierania folderu (po prawej stronie pola tekstowego)
select_button = tk.Button(folder_frame, text="Wybierz Folder", command=select_folder, padx=10)
select_button.pack(side=tk.RIGHT)

# Ramka na przyciski "Rozpocznij Porządkowanie" i "Informacje o Autorze"
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Przycisk do rozpoczęcia procesu porządkowania
organize_button = tk.Button(button_frame, text="Rozpocznij Porządkowanie", command=start_organizing, padx=20, pady=10)
organize_button.pack(side=tk.LEFT, padx=10)

# Przycisk do wyświetlania informacji o autorze (po prawej stronie przycisku "Rozpocznij Porządkowanie")
author_button = tk.Button(button_frame, text="Informacje o Autorze", command=show_author_info, padx=20, pady=10)
author_button.pack(side=tk.RIGHT, padx=10)

# Uruchomienie głównej pętli interfejsu graficznego
root.mainloop()
