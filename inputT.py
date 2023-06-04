#INPUT TANGGAL PERTAMA KALI
from datetime import datetime, timedelta
import csv
import calendar
import tkinter as tk
from tkinter import messagebox

def hitung_siklus_mens():
    rata_waktu_mens = int(input("Masukkan rata-rata durasi menstruasi (dalam hari): "))
    tgl_terakhir_mens = input("Masukkan tanggal terakhir menstruasi (format: DD-MM-YYYY): ")
    tgl_terakhir_mens = datetime.strptime(tgl_terakhir_mens, '%d-%m-%Y')

    tgl_awal_mens_berikutnya = tgl_terakhir_mens + timedelta(days=28)
    tgl_akhir_mens_berikutnya = tgl_terakhir_mens + timedelta(days=28 + rata_waktu_mens)

    tgl_awal_folikular_berikutnya = tgl_akhir_mens_berikutnya + timedelta(days=1)
    if rata_waktu_mens > 5:
        tgl_akhir_folikular_berikutnya = tgl_awal_folikular_berikutnya + timedelta(days=7)
    else:
        tgl_akhir_folikular_berikutnya = tgl_awal_folikular_berikutnya + timedelta(days=9)

    tgl_awal_ovulasi_berikutnya = tgl_akhir_folikular_berikutnya + timedelta(days=1)
    tgl_akhir_ovulasi_berikutnya = tgl_akhir_folikular_berikutnya + timedelta(days=3)

    tgl_awal_luteal_berikutnya = tgl_akhir_ovulasi_berikutnya + timedelta(days=1)
    if rata_waktu_mens > 5:
        tgl_akhir_luteal_berikutnya = tgl_awal_luteal_berikutnya + timedelta(days=9)
    else:
        tgl_akhir_luteal_berikutnya = tgl_awal_luteal_berikutnya + timedelta(days=11)

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