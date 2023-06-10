#INPUT TANGGAL PERTAMA KALI
from datetime import datetime, timedelta

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
    template_csv = '''    tgl awal mens,              tgl akhir mens,             tgl awal folik,             tgl akhir folik,                tgl awal ovul,              tgl akhir ovul,             tgl awal lut,           tgl akhir lut
      {}                   {}                  {}                  {}                     {}                  {}                 {}              {}'''.format(
            hasil[0].strftime('%d-%m-%Y'),
            hasil[1].strftime('%d-%m-%Y'),
            hasil[2].strftime('%d-%m-%Y'),
            hasil[3].strftime('%d-%m-%Y'),
            hasil[4].strftime('%d-%m-%Y'),
            hasil[5].strftime('%d-%m-%Y'),
            hasil[6].strftime('%d-%m-%Y'),
            hasil[7].strftime('%d-%m-%Y')
        )
    file_datamens = open(nama_file, 'w')
    file_datamens.write(template_csv)
    file_datamens.close() 

simpan_ke_csv(hasil)
