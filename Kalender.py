import pandas as pd
import calendar
import tkinter as tk
from tkinter import ttk
from datetime import datetime

def konversi_ke_kalender(data_prediksi):
    root = tk.Tk()
    root.title("Kalender Siklus Menstruasi")
    root.geometry("800x600")
    
    frame_calendar = tk.Frame(root)
    frame_calendar.pack(pady=20)

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

    def show_calendar():
        for widget in frame_calendar.winfo_children():
            widget.destroy()

        num_days = calendar.monthrange(year, month)[1]

        month_label = tk.Label(frame_calendar, text=calendar.month_name[month] + " " + str(year), font=("Arial", 16, "bold"))
        month_label.grid(row=0, column=0, columnspan=7, padx=10, pady=10)

        days_labels = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for idx, day_label in enumerate(days_labels):
            label = tk.Label(frame_calendar, text=day_label)
            label.grid(row=1, column=idx, padx=5, pady=5)
            
        first_day = datetime(year, month, 1)
        col_idx = first_day.weekday()
        row_idx = 2

        for day in range(1, num_days + 1):
            if col_idx > 6:
                col_idx = 0
                row_idx += 1

            background_color = "white"
            explanation = ""
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
                    explanation = "Masa Menstruasi"
                    break
                elif tanggal_awal_folik <= datetime(year, month, day) <= tanggal_akhir_folik:
                    background_color = "lightblue"
                    explanation = "Masa Folikular"
                    break
                elif tanggal_awal_ovul <= datetime(year, month, day) <= tanggal_akhir_ovul:
                    background_color = "yellow"
                    explanation = "Masa Ovulasi"
                    break
                elif tanggal_awal_lut <= datetime(year, month, day) <= tanggal_akhir_lut:
                    background_color = "lightgreen"
                    explanation = "Masa Luteal"
                    break
                    
            label = tk.Label(frame_calendar, text=day, bg=background_color, padx=10, pady=5)
            label.grid(row=row_idx, column=col_idx, padx=5, pady=5)

            tooltip = tk.Label(label, text=explanation, bg="white", relief="solid", borderwidth=1)
            tooltip.pack_forget()

            def show_tooltip(event):
                tooltip.pack()

            def hide_tooltip(event):
                tooltip.pack_forget()

            label.bind("<Enter>", show_tooltip)
            label.bind("<Leave>", hide_tooltip)

            col_idx += 1

    today = datetime.now()
    month = today.month
    year = today.year

    show_calendar()

    root.mainloop()
    
data_prediksi = pd.read_csv("siklus_mens.csv", skipinitialspace=True)

konversi_ke_kalender(data_prediksi)
