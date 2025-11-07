print("===================")
print("Daftar Belanja")
print("===================")
print("1. Beras")
print("2. Shampoo")
print("3. sabun")
print("4. Pasta Gigi")
print("===================")

#Extend
belanja = ["Beras, Shampoo, Sabun, Pasta Gigi"]
belanja.extend(["Hair Oil", "Odol"])
print(belanja)

#remove
belanja = ["Beras", "Shampoo", "Sabun", "Pasta Gigi"]
belanja.remove("Shampoo")
print(belanja)

#short
belanja = ["Beras", "Shampoo", "Sabun", "Pasta Gigi"]
belanja.sort()
print(belanja)

#pop
belanja = ["Beras", "Shampoo", "Sabun", "Pasta Gigi"]
belanja.pop(2)
print(belanja)

#clear
belanja = ["Beras", "Shampoo", "Sabun", "Pasta Gigi"]
belanja.clear()
print(belanja)