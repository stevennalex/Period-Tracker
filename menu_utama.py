import csv
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import json
import insight
import webbrowser

def main_program():
    while True:
        try:
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

            hasil1 = tk.StringVar()
            hasil2 = tk.StringVar()
            def inputinputan():
                if login_count==1:
                    input_frame = ttk.Frame(window_utama)
                    input_frame.pack(fill='x', padx=70, expand=True)

                    label_tgl_terakhir_mens = ttk.Label(input_frame, text='Tanggal Terakhir Mens Kamu: (DD-MM-YYYY)')
                    label_tgl_terakhir_mens.pack(padx=10, pady=10, fill='x', expand=True)
                    entry_tgl_terakhir_mens = ttk.Entry(input_frame, textvariable=hasil1)
                    entry_tgl_terakhir_mens.pack(padx=10, pady=10, fill='x', expand=True)

                    label_ratarata = ttk.Label(input_frame, text='Rata-Rata Durasi Mens Kamu (Hari):')
                    label_ratarata.pack(padx=10, pady=10, fill='x', expand=True)
                    entry_ratarata = ttk.Entry(input_frame, textvariable=hasil2)
                    entry_ratarata.pack(padx=10, pady=10, fill='x', expand=True)

                    tanggal = hasil1.get()
                    ratarata = hasil2.get()
                    def simpan_data():
                        nama_file = 'data_input.csv'
                        simpan_ke_csv(tanggal, ratarata, nama_file)

                    def cek1():
                        try:
                            if tanggal.isalpha():
                                raise ValueError('Masukkan Sesuai Format!!')
                        except:
                            messagebox.showerror('Error')
                            inputinputan()

                    def cek2():
                        try:
                            if ratarata == int(ratarata):
                                raise ValueError('Masukkan Angka Saja!!')
                        except ValueError:
                            messagebox.showerror('Error')
                            inputinputan()

                    from input_T_dan_Input_E import mens
                    def hitung_mens():
                        simpan_data()
                        mens()
                    button_next = ttk.Button(input_frame, text='Hitung', command=lambda: (hitung_mens, cek1, cek2))
                    button_next.pack()
            inputinputan()
        
            def simpan_ke_csv(tanggal,ratarata, nama_file):
                header = ['Tanggal', 'rata-rata']
                data = [[tanggal, ratarata]]

                with open(nama_file, 'w', newline='') as file_datamens:
                    writer = csv.writer(file_datamens)
                    writer.writerow(header)
                    writer.writerows(data)


            def next_page():
                window_utama.withdraw()
                def closedwindow1():
                    next_window.withdraw()
                    window_utama.deiconify()

                def modulinsight():
                    next_window.withdraw()

                    insight_window = tk.Tk()
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

                        isi_insight = tk.Toplevel()
                        isi_insight.configure(bg='lightpink')
                        isi_insight.geometry('600x600')
                        isi_insight.resizable(False, False)
                        isi_insight.title('Insight')

                        def back():
                            isi_insight.withdraw()
                            insight_window.deiconify()
                            
                        def link_olahraga():
                            youtube_link = "https://www.youtube.com/results?search_query=rekomendasi+olahraga+untuk+menstruasi"
                            webbrowser.open(youtube_link)

                        image = Image.open("bg4.jpg")
                        image = image.resize((isi_insight.winfo_screenwidth(), isi_insight.winfo_screenheight()))
                        image = image.resize((600, 900)) 

                        photo = ImageTk.PhotoImage(image)
                        background_label = ttk.Label(isi_insight, image=photo)
                        background_label.place(x=0, y=0, relwidth=1, relheight=1)

                        hasila = insight.teks_olahraga()
                        text_olahraga = ttk.Label(isi_insight, text=hasila, justify='center', wraplength=450)
                        text_olahraga.pack()

                        button_link = ttk.Button(isi_insight, text='Rekomendasi Olahraga', command=link_olahraga)
                        button_link.pack()

                        button_olahraga = ttk.Button(isi_insight, text='Back', command=back)
                        button_olahraga.pack()

                        isi_insight.mainloop()

                    def modulmakanan():
                        insight_window.withdraw()

                        isi_insight = tk.Toplevel()
                        isi_insight.configure(bg='lightpink')
                        isi_insight.geometry('600x620')
                        isi_insight.resizable(False, False)
                        isi_insight.title('Insight')
                        
                        def back():
                            isi_insight.withdraw()
                            insight_window.deiconify()

                        def link_makanan():
                            youtube_link = "https://youtu.be/V42iKfIMSD8"
                            webbrowser.open(youtube_link)

                        image = Image.open("bg5.jpg")
                        image = image.resize((isi_insight.winfo_screenwidth(), isi_insight.winfo_screenheight()))
                        image = image.resize((600, 900))  

                        photo = ImageTk.PhotoImage(image)
                        background_label = tk.Label(isi_insight, image=photo)
                        background_label.place(x=0, y=0, relwidth=1, relheight=1)

                        hasilb = insight.makanan()
                        text_makanan = ttk.Label(isi_insight, text=hasilb, justify='center', wraplength=450)
                        text_makanan.pack()

                        button_link = ttk.Button(isi_insight, text='Rekomendasi Makanan', command=link_makanan)
                        button_link.pack()

                        button_makanan = ttk.Button(isi_insight, text='Back', command=back)
                        button_makanan.pack()

                        isi_insight.mainloop()

                

                    def modultidur():
                        insight_window.withdraw()

                        isi_insight = tk.Toplevel()
                        isi_insight.configure(bg='lightpink')
                        isi_insight.geometry('600x620')
                        isi_insight.resizable(False, False)
                        isi_insight.title('Insight')
                        
                        def back():
                            isi_insight.withdraw()
                            insight_window.deiconify()

                        def link_tidur():
                            youtube_link = "https://youtu.be/YedavoJ7zhc"
                            webbrowser.open(youtube_link)


                        image = Image.open("bg6.jpg")
                        image = image.resize((isi_insight.winfo_screenwidth(), isi_insight.winfo_screenheight()))
                        image = image.resize((600, 900))  

                        photo = ImageTk.PhotoImage(image)
                        background_label = tk.Label(isi_insight, image=photo)
                        background_label.place(x=0, y=0, relwidth=1, relheight=1)

                        hasilc = insight.tidur()
                        text_tidur = ttk.Label(isi_insight, text=hasilc, justify='center', wraplength=450)
                        text_tidur.pack()

                        button_link = ttk.Button(isi_insight, text='Rekomendasi Posisi Tidur', command=link_tidur)
                        button_link.pack()

                        button_tidur = ttk.Button(isi_insight, text='Back', command=back)
                        button_tidur.pack()

                        isi_insight.mainloop()

                    def modulhaid():
                        from HAID import haid
                        haid()

                    button_olahraga = ttk.Button(button_frame, text='Olahraga Yang Cocok Saat Mens', command=modulolahraga)
                    button_olahraga.pack(padx=60, pady=10, fill='x', expand=True)
                    
                    button_makanan = ttk.Button(button_frame, text='Makanan Yang Menaikkan Mood Kamu', command=modulmakanan)
                    button_makanan.pack(padx=60, pady=10, fill='x', expand=True)
                    
                    button_tidur = ttk.Button(button_frame, text='Nyeri Mens Mengganggu Tidur? Ini Tipsnya', command=modultidur)
                    button_tidur.pack(padx=60, pady=10, fill='x', expand=True)

                    button_haid = ttk.Button(button_frame, text='Haid Kamu Telat?', command=modulhaid)
                    button_haid.pack(padx=60, pady=10, fill='x', expand=True)

                    button_back = ttk.Button(button_frame, text='Back', command= closedwindow2)
                    button_back.pack(padx=60, pady=10, fill='x', expand=True)

                    insight_window.mainloop()
                
                def editperiod():
                    next_window.withdraw()

                    def backedit():
                        window_editperiod.withdraw()
                        next_window.deiconify()

                    window_editperiod = tk.Toplevel()
                    window_editperiod.configure(bg='lightpink')
                    window_editperiod.geometry('750x700')
                    window_editperiod.resizable(False, False)
                    window_editperiod.title('Edit Period')

                    input_frame = ttk.Frame(window_editperiod)
                    input_frame.pack(fill='x', padx=70, expand=True)

                    label_tgl_terakhir_mens = ttk.Label(input_frame, text='Tanggal Terakhir Mens Kamu: (DD-MM-YYYY)')
                    label_tgl_terakhir_mens.pack(padx=10, pady=10, fill='x', expand=True)
                    entry_tgl_terakhir_mens = ttk.Entry(input_frame, textvariable=hasil1)
                    entry_tgl_terakhir_mens.pack(padx=10, pady=10, fill='x', expand=True)

                    label_ratarata = ttk.Label(input_frame, text='Rata-Rata Durasi Mens Kamu (Hari):')
                    label_ratarata.pack(padx=10, pady=10, fill='x', expand=True)
                    entry_ratarata = ttk.Entry(input_frame, textvariable=hasil2)
                    entry_ratarata.pack(padx=10, pady=10, fill='x', expand=True)

                    tanggal = hasil1.get()
                    ratarata = hasil2.get()
                    def simpan_data():
                        nama_file = 'data_input.csv'
                        simpan_ke_csv(tanggal, ratarata, nama_file)

                    def cek1():
                        try:
                            if tanggal.isalpha():
                                raise ValueError('Masukkan Sesuai Format!!')
                        except:
                            messagebox.showerror('Error')
                            editperiod()

                    def cek2():
                        try:
                            if ratarata == int(ratarata):
                                raise ValueError('Masukkan Angka Saja!!')
                        except ValueError:
                            messagebox.showerror('Error')
                            editperiod()

                    from input_T_dan_Input_E import mens
                    def hitung_mens():
                        simpan_data()
                        mens()
                    button_next = ttk.Button(input_frame, text='Hitung', command=lambda: (hitung_mens, cek1, cek2))
                    button_next.pack()

                    button_backedit = ttk.Button(input_frame, text='Back', command= backedit)
                    button_backedit.pack()

                    window_editperiod.mainloop()

                next_window = tk.Toplevel()
                next_window.configure(bg='lightpink')
                next_window.geometry('750x700')
                next_window.resizable(False, False)
                next_window.title('Choose ur destination')

                button_frame = ttk.Frame(next_window)
                button_frame.pack(padx=60, pady=10, fill='x', expand=True)

                from Kalender import kalender
                modul_kalender = kalender
                button_kalender = ttk.Button(button_frame, text='Kalender', command=modul_kalender)
                button_kalender.pack(padx=60, pady=10, fill='x', expand=True)
                
                button_insight = ttk.Button(button_frame, text='Insight', command=modulinsight)
                button_insight.pack(padx=60, pady=10, fill='x', expand=True)

                button_editperiod = ttk.Button(button_frame, text='Edit Period', command=editperiod)
                button_editperiod.pack(padx=60, pady=10, fill='x', expand=True)

                button_back = ttk.Button(button_frame, text='Back', command= closedwindow1)
                button_back.pack(padx=60, pady=10, fill='x', expand=True)

                next_window.mainloop()
                
            button_next = ttk.Button(window_utama, text='Next', command=next_page)
            button_next.pack(fill='x', pady=10, expand=True)

            window_utama.mainloop()
            break
        finally:
            window_utama.destroy()
            main_program()
main_program()  
