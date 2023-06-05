import tkinter as tk
import calendar

def create_calendar(year, month):
    # Membuat objek kalender dari modul calendar
    cal = calendar.monthcalendar(year, month)

    # Membuat jendela Tkinter
    root = tk.Tk()
    root.title("Template Kalender")
    root.geometry("400x300")

    # Membuat label untuk judul kalender (nama bulan dan tahun)
    month_year_label = tk.Label(root, text=calendar.month_name[month] + " " + str(year), font=("Arial", 16, "bold"))
    month_year_label.pack(pady=10)

    # Membuat frame untuk grid kalender
    calendar_frame = tk.Frame(root)
    calendar_frame.pack()

    # Membuat label untuk nama-nama hari
    days_labels = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    for idx, day_label in enumerate(days_labels):
        label = tk.Label(calendar_frame, text=day_label, bg="lightgray", width=10, padx=10, pady=5)
        label.grid(row=0, column=idx)

    # Menampilkan tanggal-tanggal dalam kalender
    for week_idx, week in enumerate(cal):
        for day_idx, day in enumerate(week):
            if day != 0:
                label = tk.Label(calendar_frame, text=day, padx=10, pady=5)
                label.grid(row=week_idx+1, column=day_idx)

    # Menjalankan loop Tkinter
    root.mainloop()

# Input tahun dan bulan
year = int(input("Masukkan tahun: "))
month = int(input("Masukkan bulan (1-12): "))

# Membuat template kalender
create_calendar(year, month)
