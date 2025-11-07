#Praktik Python
#NO.1 Sekuensial
nama = input("Masukkan nama anda:")
Usia = input("Masukkan usia anada:")
Hobi = input("Masukkan hobi anda:")
warna_fav = input("Masukkan warna favorit anda:")

print('Halo nama saya', nama, 'Usia saya adalah', Usia, 'Tahun,', 'Saya memiliki hobi yaitu', Hobi, 'Dan Warna kesukaan saya adalah', warna_fav)

#No.2 Percabangn (if_elif_else)
nilai = int(input("Masukkan nilai anda:"))
if nilai >= 90:
    print("Nilai anda bagus")
elif nilai >= 70:
    print("Nilai anda cukup, tingkatkan lagi!")
else:
    print("Nilai anda kurang, belajar yang rajin ya!")

#No.3 Perulangan For
i =  5
while i <= 17:
    print(i)
    i +=1

#While menghasilkan angka dari 5 sampai 17, sesuai dengan i yang ditetapkan.

#No.4 Perulangan While
i =  5
while i <= 17:
    print(i)
    i +=1

#No.5 Tipe data list extend
hewan = ['kelinci', 'ayam', 'gajah']
hewan.extend(['Harimau', 'Burung'])
print(hewan)

