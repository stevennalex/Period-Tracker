from datetime import datetime, timedelta

def hitung_telat_haid(tgl_terakhir_mens, rata_waktu_mens):
    tgl_sekarang = datetime.today().date()
    tgl_terakhir_mens = datetime.strptime(tgl_terakhir_mens, '%d-%m-%Y').date()
    durasi_siklus = timedelta(days=rata_waktu_mens)
    tgl_menstruasi_selanjutnya = tgl_terakhir_mens + durasi_siklus
    telat_haid = (tgl_sekarang - tgl_menstruasi_selanjutnya).days

    return telat_haid

# Input tanggal menstruasi terakhir
tgl_terakhir_mens = input("Masukkan tanggal menstruasi terakhir (format: DD-MM-YYYY): ")

# Input rata-rata durasi siklus menstruasi
rata_waktu_mens = int(input("Masukkan rata-rata durasi siklus menstruasi (dalam hari): "))

# Hitung keterlambatan haid
telat_haid = hitung_telat_haid(tgl_terakhir_mens, rata_waktu_mens)

# Tampilkan hasil
if telat_haid > 0:
    print(f"Telat haid selama {telat_haid} hari")
elif telat_haid == 0:
    print("Tidak ada keterlambatan haid")
else:
    print(f"Haid lebih awal {abs(telat_haid)} hari")
