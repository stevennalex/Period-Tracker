import tkinter as tk
from tkinter import ttk
import inputT
import Siklus_K

window_utama = tk.Tk()
window_utama.configure(bg='lightpink')
window_utama.geometry('600x400')
window_utama.resizable(False, False)
window_utama.title('Period Tracker')

tglterakhir = tk.StringVar()
ratarata = tk.StringVar()

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

inputT.hitung_siklus_mens(ratarata.get(), tglterakhir.get())

def next_page():
    window_utama.withdraw()
    next_window = tk.Toplevel(window_utama)
    next_window.configure(bg='lightpink')
    next_window.geometry('600x400')
    next_window.resizable(False, False)
    next_window.title('Choose ur destination')

    button_kalender = ttk.Button(next_window, text='Kalender', command= Siklus_K)
    button_kalender.pack()
button_next = ttk.Button(window_utama, text='Next', command=next_page)
button_next.pack(fill='x', padx=150, expand=True)

window_utama.mainloop()