from datetime import timedelta, datetime
import os
import calendar
import csv
import pandas as pd

df = pd.read_csv('data_input.csv')

tanggal = df['Tanggal'].astype(str)
ratarata = int(df['rata-rata'].values[0])
tanggal = pd.to_datetime(tanggal, format='%d-%m-%Y').iloc[0]

def hitung_siklus_mens(tanggal, ratarata):
        

    tgl_awal_mens_berikutnya = tanggal + timedelta(days=28)
    tgl_akhir_mens_berikutnya = tanggal + timedelta(days=27 + ratarata)

    tgl_awal_folikular_berikutnya = tgl_akhir_mens_berikutnya + timedelta(days=1)
    if ratarata > 5:
        tgl_akhir_folikular_berikutnya = tgl_awal_folikular_berikutnya + timedelta(days=6)
    else:
        tgl_akhir_folikular_berikutnya = tgl_awal_folikular_berikutnya + timedelta(days=8)

    tgl_awal_ovulasi_berikutnya = tgl_akhir_folikular_berikutnya + timedelta(days=1)
    tgl_akhir_ovulasi_berikutnya = tgl_akhir_folikular_berikutnya + timedelta(days=3)

    tgl_awal_luteal_berikutnya = tgl_akhir_ovulasi_berikutnya + timedelta(days=1)
    if ratarata > 5:
        tgl_akhir_luteal_berikutnya = tgl_awal_luteal_berikutnya + timedelta(days=8)
    else:
        tgl_akhir_luteal_berikutnya = tgl_awal_luteal_berikutnya + timedelta(days=10)

    durasi_mens = ratarata
    durasi_folikular = (tgl_akhir_folikular_berikutnya - tgl_awal_folikular_berikutnya  + timedelta(days=1)).days
    durasi_ovulasi = (tgl_akhir_ovulasi_berikutnya - tgl_awal_ovulasi_berikutnya + timedelta(days=1)).days
    durasi_luteal = (tgl_akhir_luteal_berikutnya - tgl_awal_luteal_berikutnya + timedelta(days=1)).days

    hasil = (
        tgl_awal_mens_berikutnya.date(),
        tgl_akhir_mens_berikutnya.date(),
        tgl_awal_folikular_berikutnya.date(),
        tgl_akhir_folikular_berikutnya.date(),
        tgl_awal_ovulasi_berikutnya.date(),
        tgl_akhir_ovulasi_berikutnya.date(),
        tgl_awal_luteal_berikutnya.date(),
        tgl_akhir_luteal_berikutnya.date(),
        durasi_mens,
        durasi_folikular,
        durasi_ovulasi,
        durasi_luteal,
        )
    simpan_ke_csv_1(hasil, 'siklus_mens.csv')
    simpan_ke_csv_2(hasil, 'durasi_siklus.csv')

    return hasil


def simpan_ke_csv_1(hasil, nama_file):
    header = 'tgl awal mens,tgl akhir mens,tgl awal folik,tgl akhir folik,tgl awal ovul,tgl akhir ovul,tgl awal lut,tgl akhir lut'
    template_csv = '\n{},{},{},{},{},{},{},{}'.format(
            hasil[0].strftime('%d-%m-%Y'),
            hasil[1].strftime('%d-%m-%Y'),
            hasil[2].strftime('%d-%m-%Y'),
            hasil[3].strftime('%d-%m-%Y'),
            hasil[4].strftime('%d-%m-%Y'),
            hasil[5].strftime('%d-%m-%Y'),
            hasil[6].strftime('%d-%m-%Y'),
            hasil[7].strftime('%d-%m-%Y'),
        )
    file_datamens = open(nama_file, 'w')
    file_datamens.write(header)
    file_datamens.write(template_csv)
    file_datamens.close()

def simpan_ke_csv_2(hasil, nama_file):
    header = 'Bulan,Durasi Mens,Durasi Folikular,Durasi Ovulasi,Durasi Luteal'
    template_csv ='\n{},{},{},{},{}'.format(
        calendar.month_name[hasil[0].month], 
        hasil[8],
        hasil[9],
        hasil[10],
        hasil[11],
    )
    file_exists = os.path.isfile(nama_file)
    file_datamens = open(nama_file, 'a')
    if not file_exists:
        file_datamens.write(header)
    file_datamens.write(template_csv)
    file_datamens.close()

hasil = hitung_siklus_mens(tanggal, ratarata)
