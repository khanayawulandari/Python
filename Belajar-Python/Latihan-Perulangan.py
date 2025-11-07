n = int(input("Masukkan angka "))

for kata in ["ke-1", "ke-2", "ke-3", "ke-4", "ke-5"][:n]:
    angka = int(input(f"Masukkan angka {kata}:"))

angka = (3, 4, 2, 6, 5)
total = 0
for a in angka:
    total += a
print(f"Jumlah total = {total}")

