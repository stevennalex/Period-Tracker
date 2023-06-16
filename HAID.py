from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import pandas as pd
from tkinter import ttk
import webbrowser

def link_haid():
    shopee_link = "https://bit.ly/rekomendasi-obat"
    webbrowser.open(shopee_link)

def haid():
    window = tk.Tk()
    window.resizable(False, False)
    window.configure(bg='lightpink')
    window.geometry('750x760')
    window.title('Haid Kamu Telat :(')

    label = ttk.Label(window, text='''   Mens merupakan proses keluarnya darah dari vagina yang disebabkan oleh terlepasnya dinding rahim (endometrium). Sebelum terlepas bersama dengan darah, endometrium ini mengalami penebalan yang mengandung pembuluh darah.
    Jika tidak terjadi pembuahan sperma dengan sel telur, maka endometrium ini akan luruh dan keluar bersamaan dengan darah. Mens merupakan siklus bulanan yang alami pada wanita. Siklus normal mens umumnya terjadi setiap 21 hari sampai 35 hari sekali. 
    Dalam setiap periodenya, pendarahan saat mens terjadi 3 hari sampai 7 hari. Namun, memang ada sebagian wanita yang memiliki perbedaan siklus serta lama terjadinya mens. Bahkan, sebagian di antaranya juga mengalami mens yang datangnya telat. Sekalipun mereka sedang tidak hamil.
    Jika kamu salah satu di antaranya, kamu tak bisa mengabaikannya begitu saja. 
    Ada beberapa faktor mens telat yang bisa saja terjadi padamu antara lain adalah kelelahan, stress, pengaruh alat kontrasepsi, PCOS, gangguan kelenjar tiroid, efek merokok, dan menopause. 
    Jika kamu mengalami telat mens, jangan panik sebab ada beberapa cara mengatasi telat Haid dengan alami, yaitu seperti mengonsumsi vitamin C, konsumsi jamu kunyit, minum teh dari jahe, relaksasi, dan memanfaatkan air hangat (mandi dengan air hangat)'''
            ,justify="center", wraplength=450)
    label.pack(pady=10)

    df = pd.read_csv('durasi_siklus.csv')

    bulan = df['Bulan']
    durasi_mens = df['Durasi Mens']
    durasi_folikular = df['Durasi Folikular']
    durasi_ovulasi = df['Durasi Ovulasi']
    durasi_luteal = df['Durasi Luteal']

    fig = Figure(figsize=(4, 4))
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
    canvas.get_tk_widget().pack(pady=10)

    button = tk.Button(window, text="Rekomendasi Obat", command=link_haid)
    button.pack()

    window.mainloop()
