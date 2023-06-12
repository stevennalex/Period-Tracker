import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import json

file_path = "login_count.json"

def load_data():
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data

def save_data(data):
    with open(file_path, "w") as file:
        json.dump(data, file)

data = load_data()

if "login_count" in data:
    login_count = data["login_count"]
else:
    login_count = 0
    
login_count += 1

data["login_count"] = login_count
save_data(data)

window_utama = tk.Tk()
window_utama.configure(bg='lightpink')
window_utama.geometry('750x700')
window_utama.resizable(False, False)
window_utama.title('Period Tracker')

image = Image.open("foto_tubes.jpg")
resize_image = image.resize((600,400))
foto = ImageTk.PhotoImage(resize_image)
label_foto = tk.Label(window_utama, image=foto)
label_foto.pack()

tglterakhir = tk.StringVar()
ratarata = tk.StringVar()

if login_count==1:
    input_frame = ttk.Frame(window_utama)
    input_frame.pack(padx=60, pady=10, fill='x', expand=True)

    label_tgl_terakhir_mens = ttk.Label(input_frame, text='Tanggal Terakhir Mens Kamu (DD-MM-YYYY):')
    label_tgl_terakhir_mens.pack(padx=10, pady=10, fill='x', expand=True)

    entry_tgl_terakhir_mens = ttk.Entry(input_frame, textvariable=tglterakhir)
    entry_tgl_terakhir_mens.pack(padx=10, pady=10, fill='x', expand=True)

    label_ratarata = ttk.Label(input_frame, text='Rata-Rata Durasi Mens Kamu:')
    label_ratarata.pack(padx=10, pady=10, fill='x', expand=True)

    entry_ratarata = ttk.Entry(input_frame, textvariable=ratarata)
    entry_ratarata.pack(padx=10, pady=10, fill='x', expand=True)

#belum nyambungin ke T

def next_page():
    window_utama.withdraw()

    def closedwindow():
        next_window.withdraw()

    next_window = tk.Tk()
    next_window.configure(bg='lightpink')
    next_window.geometry('750x700')
    next_window.resizable(False, False)
    next_window.title('Choose ur destination')

    button_frame = ttk.Frame(next_window)
    button_frame.pack(padx=60, pady=10, fill='x', expand=True)

    button_kalender = ttk.Button(button_frame, text='Kalender')
    button_kalender.pack(padx=60, pady=10, fill='x', expand=True)

    button_insight = ttk.Button(button_frame, text='Insight')
    button_insight.pack(padx=60, pady=10, fill='x', expand=True)

    button_editperiod = ttk.Button(button_frame, text='Edit Period')
    button_editperiod.pack(padx=60, pady=10, fill='x', expand=True)

    button_exit = ttk.Button(button_frame, text='Exit', command= closedwindow)
    button_exit.pack(padx=60, pady=10, fill='x', expand=True)

    next_window.mainloop()
button_next = ttk.Button(window_utama, text='Next', command=next_page)
button_next.pack(fill='x', padx=150, expand=True)

window_utama.mainloop()