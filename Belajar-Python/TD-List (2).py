list_1 = [2, 4, 8, 16]
print(list_1[0])

list_2 = ["grayson", "jason", "tim", "damian"]
print(list_2[2])

list_3 = [24, False, "Hello python"]
print(list_3[1])

#Append
buah = ["pisang, durian, manggis"]
buah.append("rambutan")
print(buah)

#Extend
buah = ["pisang, durian, manggis"]
buah.extend(["apple", "kiwi"])
print(buah)

#Insert
angka = [1, 2, 3]
angka.insert(3, 4)
print(angka)

#pop
buah = ["apel", "pisang", "durian", "nanas", "manggis"]
buah.pop(2)
print(buah)

#sort
angka = [5, 2, 9, 1, 4, 7]
angka.sort()
print(angka)

#reverse
angka = [5, 2, 9, 1, 4, 7]
angka.sort(reverse=True)
print(angka)

#clear
data = [5, 2, 9, 1, 4, 7]
angka.clear()
print(data)

#remove
buah = ["apel", "pisang", "durian", "nanas", "manggis"]
buah.remove("pisang")
print(buah)

#index
nama = ["Khay", "Gaon", "Kalle", "Naren"]
nama.index
print(nama.index("Kalle"))

#reverse
warna = ["merah", "kuning", "hijau", 'biru']
warna.reverse()
print(warna)

#coubt
angka = [1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,  3, 3, 3]
print(angka.count(3))