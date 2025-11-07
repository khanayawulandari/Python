print("Latihan Soal")
print("No.1 materi Input-buatlah program yang menghasilkan pengguna memasukkan nama, umur, hobi, dan tampilan terakhir sapaan")
print("No.2 materi Input number-Buatlah program yang meminta pengguna memasukkan umur, lalu tampilkan umr 2 tahun lagi")
print("No.3 materi perbandingan-Buatlah program yang mengecek apakah umur seseorang antara 10 sampai 17 tahun disebut (remaja)")

print("No.1")
print("Masukkan nama anda")
nama = input()
print("Masukkan umur anda")
umur = int(input())
print("Masukkan hobi anda")
hobi = input()
print(f"halo nama saya {nama}, umur saya {umur} tahun, dan hobi saya adalah {hobi}")

print("No.2")
print("masukan umur anda")
umur = int(input())
umur_2_tahun = umur + 2
print(f"umur anda 2 tahun lagi adalah {umur_2_tahun} tahun")

print("No.3")
print("Masukkan umur anda")
umur = int(input())
remaja = (10 <= umur <= 17)
print(f"apakah anda remaja? {remaja}")

print("Latihan ke-2")
print("1. Buat kode masukan nilai")
print("nilai lebih besar sama dengan 90 nilainya A")
print("nilai lebih besar sama dengan 80 nilainya B")
print("nilai lebih besar sama dengan 70 nilainya C")
print("else nilainya D")

Nilai_akhir = int(input("Masukkan nilai akhir anda:"))
if Nilai_akhir >= 90:
 print("Nilai anda A")
elif Nilai_akhir >= 80:
 print("Nilai anda B")
elif Nilai_akhir >= 70:
 print("Nilai anda C")
else:
 print("Nilai anda D")


print("2. Buat masukan nilai suhu")
print("Jika besar dari 35 suhunya panas banget")
print("Jika besar dari 25 suhunya hangat")
("Jika dibawah 25 suhunya dingin")

Suhu = int(input("Masukkan nilai suhu:"))
if Suhu > 35:
 print("Panas banget")
elif Suhu > 25:
 print("Hangat")
elif Suhu < 25:
 print("Dingin")
else:
 print("Suhu normal")