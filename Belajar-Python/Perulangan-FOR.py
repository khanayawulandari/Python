buah = ['Mangga']
print(buah)

buah = ['Apel', 'Durian', 'Manggis', 'Pisang']
print(buah)

#Perulangan dengan for
buah = ['Apel', 'Anggur', 'Melon', 'Durian', 'Rambutan']
print(buah)
for i in buah:
    print(f"i Sebuah {i}")
print('selesai')

#kuadrat
angka = [2, 3, 4, 5, 6]
for i in angka:
    print(f"{i} Kuadrat = {i**4}")

#Modulus
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in angka:
    if i % 2 == 1:
        print(f"i Sekarang {i}")
print("Selesai")

#Jumlah Total
angka = [3, 5,7, 9, 2]
total = 0

for i in angka:
    total += i

print(f"Jumlah total = {total}")

#for
ulangi = 21
for i in range (ulangi):
    print(f"Perulangan ke-{i}")

#while
jawab = 'iya'
hitung = 0

while jawab == 'iya':
    hitung += 3
    jawab = input("Ulangi lagi atau tidak? ")
    if jawab == 'tidak':
        break
print(f"Total pengulangan = {hitung}")