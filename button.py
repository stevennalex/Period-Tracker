import tkinter as tk
import olahragaa

# Fungsi yang dijalankan saat tombol pertama diklik
def on_button1_click():
    # Isi dengan tindakan yang ingin dilakukan saat tombol 1 diklik
    print("Tombol 1 diklik")

# Fungsi yang dijalankan saat tombol kedua diklik
def on_button2_click():
    # Isi dengan tindakan yang ingin dilakukan saat tombol 2 diklik
    print("Tombol 2 diklik")

# Fungsi yang dijalankan saat tombol ketiga diklik
def on_button3_click():
    # Isi dengan tindakan yang ingin dilakukan saat tombol 3 diklik
    print("Tombol 3 diklik")

# Membuat jendela Tkinter
window = tk.Tk()

# Membuat variabel untuk menyimpan teks tombol
button1_text = tk.StringVar()
button2_text = tk.StringVar()
button3_text = tk.StringVar()

# Inisialisasi teks tombol
button1_text.set("Olahraga")
button2_text.set("Makanan")
button3_text.set("Tidur")

# Membuat tombol pertama dengan teks yang dapat dikustomisasi
button1 = tk.Button(window, textvariable=button1_text, command=olahragaa.open_youtube_link)
button1.pack()

# Membuat tombol kedua dengan teks yang dapat dikustomisasi
button2 = tk.Button(window, textvariable=button2_text, command=on_button2_click)
button2.pack()

# Membuat tombol ketiga dengan teks yang dapat dikustomisasi
button3 = tk.Button(window, textvariable=button3_text, command=on_button3_click)
button3.pack()

# Menjalankan event loop Tkinter
window.mainloop()



