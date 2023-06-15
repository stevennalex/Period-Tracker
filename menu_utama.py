import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import json
import insight

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
window_utama.geometry('750x750')
window_utama.resizable(False, False)
window_utama.title('Period Tracker')

image = Image.open("foto_tubes.jpg")
resize_image = image.resize((600,400))
foto = ImageTk.PhotoImage(resize_image)
label_foto = tk.Label(window_utama, image=foto)
label_foto.pack(pady=20)

if login_count==1:
    try:
        input_frame1 = ttk.Frame(window_utama)
        input_frame1.pack(side='left', fill='x', padx=70, expand=True)
        input_frame2 = ttk.Frame(window_utama)
        input_frame2.pack(side='right', fill='x', padx=70, expand=True)

        label_tgl_terakhir_mens = ttk.Label(input_frame1, text='Tanggal Terakhir Mens Kamu: (DD)')
        label_tgl_terakhir_mens.pack(padx=10, pady=10, fill='x', expand=True)
        entry_tgl_terakhir_mens = ttk.Entry(input_frame1)
        entry_tgl_terakhir_mens.pack(padx=10, pady=10, fill='x', expand=True)

        label_bln_terakhir_mens = ttk.Label(input_frame1, text='Bulan Terakhir Mens Kamu: (MM)')
        label_bln_terakhir_mens.pack(padx=10, pady=10, fill='x', expand=True)
        entry_bln_terakhir_mens = ttk.Entry(input_frame1)
        entry_bln_terakhir_mens.pack(padx=10, pady=10, fill='x', expand=True)

        label_thn_terakhir_mens = ttk.Label(input_frame2, text='Tahun Terakhir Mens Kamu: (YYYY)')
        label_thn_terakhir_mens.pack(padx=10, pady=10, fill='x', expand=True)
        entry_thn_terakhir_mens = ttk.Entry(input_frame2)
        entry_thn_terakhir_mens.pack(padx=10, pady=10, fill='x', expand=True)

        label_ratarata = ttk.Label(input_frame2, text='Rata-Rata Durasi Mens Kamu (Hari):')
        label_ratarata.pack(padx=10, pady=10, fill='x', expand=True)
        entry_ratarata = ttk.Entry(input_frame2)
        entry_ratarata.pack(padx=10, pady=10, fill='x', expand=True)

        button_next = ttk.Button(window_utama, text='Hitung')
        button_next.pack(fill='x', pady=20, expand=True)
    except:
        messagebox.showerror('Error', 'Masukkan Input Ulang Ya')

#belum nyambungin ke T

def next_page():
    window_utama.withdraw()

    def closedwindow1():
        next_window.withdraw()
        window_utama.deiconify()

    def modulinsight():
        next_window.withdraw()

        insight_window = tk.Toplevel()
        insight_window.configure(bg='lightpink')
        insight_window.geometry('750x700')
        insight_window.resizable(False, False)
        insight_window.title('Insight')

        def closedwindow2():
            insight_window.withdraw()
            next_window.deiconify()

        button_frame = ttk.Frame(insight_window)
        button_frame.pack(padx=60, pady=10, fill='x', expand=True)
        
        def modulolahraga():
            insight_window.withdraw()
            insight.olahraga()
        
        def modulmakanan():
            insight_window.withdraw()
            insight.makanan()
        
        def modultidur():
            insight_window.withdraw()
            insight.tidur()

        button_olahraga = ttk.Button(button_frame, text='Olahraga Yang Cocok Saat Mens', command=modulolahraga)
        button_olahraga.pack(padx=60, pady=10, fill='x', expand=True)
        
        button_makanan = ttk.Button(button_frame, text='Makanan Yang Menaikkan Mood Kamu', command=modulmakanan)
        button_makanan.pack(padx=60, pady=10, fill='x', expand=True)
        
        button_tidur = ttk.Button(button_frame, text='Nyeri Mens Mengganggu Tidur? Ini Tipsnya', command=modultidur)
        button_tidur.pack(padx=60, pady=10, fill='x', expand=True)

        button_back = ttk.Button(button_frame, text='Back', command= closedwindow2)
        button_back.pack(padx=60, pady=10, fill='x', expand=True)

        insight_window.mainloop()

    next_window = tk.Toplevel()
    next_window.configure(bg='lightpink')
    next_window.geometry('750x700')
    next_window.resizable(False, False)
    next_window.title('Choose ur destination')

    button_frame = ttk.Frame(next_window)
    button_frame.pack(padx=60, pady=10, fill='x', expand=True)

    button_kalender = ttk.Button(button_frame, text='Kalender')
    button_kalender.pack(padx=60, pady=10, fill='x', expand=True)

    button_insight = ttk.Button(button_frame, text='Insight', command=modulinsight)
    button_insight.pack(padx=60, pady=10, fill='x', expand=True)

    button_editperiod = ttk.Button(button_frame, text='Edit Period')
    button_editperiod.pack(padx=60, pady=10, fill='x', expand=True)

    button_back = ttk.Button(button_frame, text='Back', command= closedwindow1)
    button_back.pack(padx=60, pady=10, fill='x', expand=True)

    next_window.mainloop()
    
button_next = ttk.Button(window_utama, text='Next', command=next_page)
button_next.pack(fill='x', pady=10, expand=True)

window_utama.mainloop()
