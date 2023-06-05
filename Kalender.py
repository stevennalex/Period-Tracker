from datetime import datetime, timedelta
import csv
import calendar
import tkinter as tk
from tkinter import messagebox

def hitung_siklus_mens():
    # Input rata-rata durasi mens user
    rata_waktu_mens = int(input("Masukkan rata-rata durasi menstruasi (dalam hari): "))

    # Input tanggal mens terakhir user
    tgl_terakhir_mens = input("Masukkan tanggal terakhir menstruasi (format: DD-MM-YYYY): ")
    tgl_terakhir_mens = datetime.strptime(tgl_terakhir_mens, '%d-%m-%Y')

    # Menghitung tanggal awal menstruasi berikutnya
    tgl_awal_mens_berikutnya = tgl_terakhir_mens + timedelta(days=28)

    # Menghitung tanggal akhir menstruasi berikutnya
    tgl_akhir_mens_berikutnya = tgl_terakhir_mens + timedelta(days=28 + rata_waktu_mens)

    # Menghitung tanggal awal folikular berikutnya
    tgl_awal_folikular_berikutnya = tgl_akhir_mens_berikutnya + timedelta(days=1)

    # Menghitung tanggal akhir folikular berikutnya
    if rata_waktu_mens > 5:
        tgl_akhir_folikular_berikutnya = tgl_awal_folikular_berikutnya + timedelta(days=7)
    else:
        tgl_akhir_folikular_berikutnya = tgl_awal_folikular_berikutnya + timedelta(days=9)

    # Menghitung tanggal awal ovulasi berikutnya
    tgl_awal_ovulasi_berikutnya = tgl_akhir_folikular_berikutnya + timedelta(days=1)

    # Menghitung tanggal akhir ovulasi berikutnya
    tgl_akhir_ovulasi_berikutnya = tgl_akhir_folikular_berikutnya + timedelta(days=3)

    # Menghitung tanggal awal luteal berikutnya
    tgl_awal_luteal_berikutnya = tgl_akhir_ovulasi_berikutnya + timedelta(days=1)

    # Menghitung tanggal akhir luteal berikutnya
    if rata_waktu_mens > 5:
        tgl_akhir_luteal_berikutnya = tgl_awal_luteal_berikutnya + timedelta(days=9)
    else:
        tgl_akhir_luteal_berikutnya = tgl_awal_luteal_berikutnya + timedelta(days=11)

    # Mengembalikan hasil dalam bentuk tuple
    return (
        tgl_awal_mens_berikutnya,
        tgl_akhir_mens_berikutnya,
        tgl_awal_folikular_berikutnya,
        tgl_akhir_folikular_berikutnya,
        tgl_awal_ovulasi_berikutnya,
        tgl_akhir_ovulasi_berikutnya,
        tgl_awal_luteal_berikutnya,
        tgl_akhir_luteal_berikutnya,
    )

hasil = hitung_siklus_mens()

def simpan_ke_csv(hasil):
    nama_file = 'siklus_mens.csv'
    template_csv = '''
            tgl awal mens                            tgl akhir mens                     tgl awal folik                      tgl akhir folik                       tgl awal ovul                    tgl akhir ovul                     tgl awal lut                        tgl akhir lut
         {}                     {}                  {}                  {}                  {}              {}                {}              {}'''.format(hasil[0], hasil[1], hasil[2], hasil[3], hasil[4], hasil[5], hasil[6], hasil[7])
    file_datamens = open(nama_file, 'a')
    file_datamens.write(template_csv)
    file_datamens.close()
        

    messagebox.showinfo("Sukses", "Hasil berhasil disimpan dalam file {}".format(nama_file))

simpan_ke_csv(hasil)

def konversi_ke_kalender(hasil):
    root = tk.Tk()
    root.title("Kalender Siklus Menstruasi")
    root.geometry("800x600")

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
            explanation = ""
            if hasil[0] <= datetime(year, month, day) <= hasil[1]:  # Masa Menstruasi
                background_color = "pink"
                explanation = "Masa Menstruasi"
            elif hasil[2] <= datetime(year, month, day) <= hasil[3]:  # Masa Folikular
                background_color = "lightblue"
                explanation = "Masa Folikular"
            elif hasil[4] <= datetime(year, month, day) <= hasil[5]:  # Masa Ovulasi
                background_color = "yellow"
                explanation = "Masa Ovulasi"
            elif hasil[6] <= datetime(year, month, day) <= hasil[7]:  # Masa Luteal
                background_color = "lightgreen"
                explanation = "Masa Luteal"

            # Membuat label untuk tanggal
            label = tk.Label(frame_calendar, text=day, bg=background_color, padx=10, pady=5)
            label.grid(row=row_idx, column=col_idx, padx=5, pady=5)

            # Menambahkan penjelasan fase siklus menstruasi sebagai tooltip
            tooltip = tk.Label(label, text=explanation, bg="white", relief="solid", borderwidth=1)
            tooltip.pack_forget()

            def show_tooltip(event):
                tooltip.pack()

            def hide_tooltip(event):
                tooltip.pack_forget()

            label.bind("<Enter>", show_tooltip)
            label.bind("<Leave>", hide_tooltip)

            col_idx += 1

    # Menginisialisasi bulan dan tahun saat ini
    today = datetime.today()
    month = today.month
    year = today.year

    # Menampilkan kalender
    show_calendar()

    root.mainloop()

konversi_ke_kalender(hasil)
