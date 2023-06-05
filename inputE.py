from datetime import datetime, timedelta
import tkinter as tk
from tkinter import messagebox

def hitung_siklus_mens():
    # Input rata-rata durasi mens user
    rata_waktu_mens = int(input("Masukkan rata-rata durasi menstruasi yang terbaru (dalam hari): "))

    # Input tanggal mens terakhir user
    tgl_terakhir_mens = input("Masukkan tanggal menstruasi terbaru (format: DD-MM-YYYY): ")
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
    nama_file = 'siklus_mens_edit.csv'
    template_csv = '''
            tgl awal mens                            tgl akhir mens                     tgl awal folik                      tgl akhir folik                       tgl awal ovul                    tgl akhir ovul                     tgl awal lut                        tgl akhir lut
         {}                     {}                  {}                  {}                  {}              {}                {}              {}'''.format(hasil[0], hasil[1], hasil[2], hasil[3], hasil[4], hasil[5], hasil[6], hasil[7])
    file_datamens = open(nama_file, 'a')
    file_datamens.write(template_csv)
    file_datamens.close()
        

    messagebox.showinfo("Sukses", "Hasil berhasil disimpan dalam file {}".format(nama_file))

simpan_ke_csv(hasil)