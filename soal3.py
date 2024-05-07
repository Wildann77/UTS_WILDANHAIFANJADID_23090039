barang = int(input("masukan jumlah barang "))

total = 0

for i in range(barang):
    harga = float(input("masukan harga "))
    total += harga

print("Total harga: ",total)