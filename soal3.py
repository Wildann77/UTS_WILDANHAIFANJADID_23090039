barang = int(input("masukan jumlah barang "))

total = 0

for i in range(barang):
    harga = int(input("masukan harga "))
    total += harga

print("Total harga: ",total)