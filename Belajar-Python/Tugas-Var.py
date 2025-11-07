print("======= Selamat datang di Toba ======")
barang_1 = "Body Serum"
harga_BS = 27000
barang_2 = "Face Wash"
harga_fC = 20000
barang_3 = "Moisturizer"
harga_M = 25000
barang_4 = 'Sunscreen'
harga_SS = 30000
barang_5 = "Toner"
harga_T = 31000


print("Daftar harga perawatan kulit:")
print("1.%s: Rp.%d" % (barang_1, harga_BS))
print("2.%s: Rp.%d" % (barang_2, harga_fC))
print("3.%s: Rp.%d" % (barang_3, harga_M))
print("4.%s: Rp.%d" % (barang_4, harga_SS))
print("5.%s: Rp.%d" % (barang_5, harga_T))

Total_harga = harga_M + harga_SS + harga_fC
print("Total harga: Rp.%d" % ( Total_harga))
