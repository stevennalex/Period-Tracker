import pandas as pd
import calendar
import tkinter as tk
from tkinter import ttk
from datetime import datetime


def konversi_ke_kalender(data_prediksi):
    root = tk.Toplevel()
    root.configure(bg= "lightpink")
    root.title("Kalender Siklus Menstruasi")
    root.geometry("500x500")

    # Frame untuk kalender
    frame_calendar = tk.Frame(root)
    frame_calendar.pack(pady=20)

    # Navigasi untuk bulan-bulan berikutnya
    def previous_month():
        nonlocal month, year
        month -= 1
        if month < 1:
            month = 12
            year -= 1
        show_calendar()

    def next_month():
        nonlocal month, year
        month += 1
        if month > 12:
            month = 1
            year += 1
        show_calendar()

    btn_previous = tk.Button(root, text="<<", command=previous_month)
    btn_previous.place(x=20, y=20)
    btn_next = tk.Button(root, text=">>", command=next_month)
    btn_next.place(x=60, y=20)

    # Fungsi untuk menampilkan kalender
    def show_calendar():
        # Menghapus kalender yang sudah ada
        for widget in frame_calendar.winfo_children():
            widget.destroy()

        # Mendapatkan jumlah hari dalam bulan yang dipilih
        num_days = calendar.monthrange(year, month)[1]

        # Membuat judul bulan dan tahun
        month_label = tk.Label(frame_calendar, text=calendar.month_name[month] + " " + str(year), font=("Arial", 16, "bold"))
        month_label.grid(row=0, column=0, columnspan=7, padx=10, pady=10)

        # Membuat label untuk nama-nama hari
        days_labels = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for idx, day_label in enumerate(days_labels):
            label = tk.Label(frame_calendar, text=day_label)
            label.grid(row=1, column=idx, padx=5, pady=5)

        # Menentukan indeks kolom dan baris untuk hari pertama di bulan
        first_day = datetime(year, month, 1)
        col_idx = first_day.weekday()
        row_idx = 2

        # Menampilkan tanggal-tanggal dalam kalender
        for day in range(1, num_days + 1):
            if col_idx > 6:
                col_idx = 0
                row_idx += 1

            # Menentukan warna latar belakang berdasarkan fase siklus menstruasi
            background_color = "white"
            for _, row in data_prediksi.iterrows():
                tanggal_awal_mens = datetime.strptime(row['tgl awal mens'], "%d-%m-%Y")
                tanggal_akhir_mens = datetime.strptime(row['tgl akhir mens'], "%d-%m-%Y")
                tanggal_awal_folik = datetime.strptime(row['tgl awal folik'], "%d-%m-%Y")
                tanggal_akhir_folik = datetime.strptime(row['tgl akhir folik'], "%d-%m-%Y")
                tanggal_awal_ovul = datetime.strptime(row['tgl awal ovul'], "%d-%m-%Y")
                tanggal_akhir_ovul = datetime.strptime(row['tgl akhir ovul'], "%d-%m-%Y")
                tanggal_awal_lut = datetime.strptime(row['tgl awal lut'], "%d-%m-%Y")
                tanggal_akhir_lut = datetime.strptime(row['tgl akhir lut'], "%d-%m-%Y")

                if tanggal_awal_mens <= datetime(year, month, day) <= tanggal_akhir_mens:
                    background_color = "pink"
                    break
                elif tanggal_awal_folik <= datetime(year, month, day) <= tanggal_akhir_folik:
                    background_color = "lightblue"
                    break
                elif tanggal_awal_ovul <= datetime(year, month, day) <= tanggal_akhir_ovul:
                    background_color = "yellow"
                    break
                elif tanggal_awal_lut <= datetime(year, month, day) <= tanggal_akhir_lut:
                    background_color = "lightgreen"
                    break

            # Membuat label untuk tanggal
            label = tk.Label(frame_calendar, text=day, bg=background_color, padx=10, pady=5)
            label.grid(row=row_idx, column=col_idx, padx=5, pady=5)

            col_idx += 1

    frame_text = ttk.Frame(root)
    frame_text.place(x=200, y=350)

    label_text = ttk.Label(frame_text, text='- Pink = Menstruasi\n- Biru = Folikular\n- Kuning = Ovulasi\n- Hijau = Luteal')
    label_text.pack()

    # Menginisialisasi bulan dan tahun saat ini
    today = datetime.now()
    month = today.month
    year = today.year

    # Menampilkan kalender
    show_calendar()

    root.mainloop()

# Membaca data prediksi dari file CSV menggunakan Pandas
data_prediksi = pd.read_csv("siklus_mens.csv")

# Memanggil fungsi untuk menampilkan kalender dengan data dari file CSV

def kalender():
    konversi_ke_kalender(data_prediksi)
