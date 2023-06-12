from datetime import datetime, timedelta
import os
import calendar

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
    tgl_akhir_ovulasi_berikutnya = tgl_akhir_folikular_berikutnya + timedelta(days=4)

    tgl_awal_luteal_berikutnya = tgl_akhir_ovulasi_berikutnya + timedelta(days=1)
    if rata_waktu_mens > 5:
        tgl_akhir_luteal_berikutnya = tgl_awal_luteal_berikutnya + timedelta(days=9)
    else:
        tgl_akhir_luteal_berikutnya = tgl_awal_luteal_berikutnya + timedelta(days=11)

    durasi_mens = rata_waktu_mens
    durasi_folikular = (tgl_akhir_folikular_berikutnya - tgl_awal_folikular_berikutnya).days
    durasi_ovulasi = (tgl_akhir_ovulasi_berikutnya - tgl_awal_ovulasi_berikutnya).days
    durasi_luteal = (tgl_akhir_luteal_berikutnya - tgl_awal_luteal_berikutnya).days
    return (
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

hasil = hitung_siklus_mens()

def simpan_ke_csv_1(hasil, nama_file):
    header = '    tgl awal mens,              tgl akhir mens,             tgl awal folik,             tgl akhir folik,                tgl awal ovul,              tgl akhir ovul,             tgl awal lut,           tgl akhir lut,'
    template_csv = '''    
      {},                  {},                 {},                 {},                    {},                 {},                 {},             {},          '''.format(
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


simpan_ke_csv_1(hasil, 'siklus_mens.csv')

def simpan_ke_csv_2(hasil, nama_file):
    header = '     Bulan,      Durasi Mens,      Durasi Folikular,     Durasi Ovulasi,   Durasi Luteal,'
    template_csv = ''' 
      {},            {},                  {},                    {},              {},'''.format(
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

simpan_ke_csv_2(hasil, 'durasi_siklus.csv')
