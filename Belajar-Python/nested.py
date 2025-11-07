max = int(input("Jumlah Bintang"))
for i in range(max):
    for s in range(i):
        print(" ", end=" ")
    for j in range(max - i):
        print("*", end=" ")
    print()

#Belajar berhitung
a = int(input("Masukkan angka pertama:"))
b = int(input("Masukkan angka kedua:"))
operator = input("Masukkan operator (+, -, *, /):")

match operator:
    case "+":
        hasil = a + b
        print(f"Hasil dari {a} + {b} = {hasil}")
    case "-":
        hasil = a - b
        print(f"Hasil dari {a} - {b} = {hasil}")
    case "*":
        hasil = a * b
        print(f"Hasil dari {a} * {b} = {hasil}")
    case "/":
        if b != 0:
            hasil = a / b
            print(f"Hasil dari {a} / {b} = {hasil}")
        else:
            print("Error: Pembagian dengan nol tidak bisa")
    case _:
        print("Operator tidak dikenal")