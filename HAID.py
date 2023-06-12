from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import pandas as pd

def haid():
    window = tk.Tk()
    window.resizable(False, False)
    window.configure(bg='lightpink')
    window.geometry('750x700')
    df = pd.read_csv('durasi_siklus.csv')

    bulan = df['     Bulan']
    durasi_mens = df['      Durasi Mens']
    durasi_folikular = df['      Durasi Folikular']
    durasi_ovulasi = df['     Durasi Ovulasi']
    durasi_luteal = df['   Durasi Luteal']

    fig = Figure(figsize=(6, 6))
    ax = fig.add_subplot(111)

    ax.bar(bulan, durasi_mens, label='Durasi Mens', color='blue')
    ax.bar(bulan, durasi_folikular, bottom=durasi_mens, label='Durasi Folikular', color='orange')
    ax.bar(bulan, durasi_ovulasi, bottom=[i+j for i,j in zip(durasi_mens, durasi_folikular)], label='Durasi Ovulasi', color='green')
    ax.bar(bulan, durasi_luteal, bottom=[i+j+k for i,j,k in zip(durasi_mens, durasi_folikular, durasi_ovulasi)], label='Durasi Luteal', color='purple')

    ax.set_xlabel('Bulan')
    ax.set_ylabel('Durasi (hari)')
    ax.set_title('Durasi Siklus Menstruasi Setiap Bulan')
    ax.set_xticklabels(bulan, rotation='vertical')
    ax.legend()

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()

    window.mainloop()

haid()
