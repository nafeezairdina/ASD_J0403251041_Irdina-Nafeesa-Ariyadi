#=========================================#
# Nama: Irdina Nafeesa Ariyadi            #
# NIM: J0403251041                        #
# Kelas: TPL B1                           #
# Praktikum 13 - Graph III: Spanning Tree #
#=========================================#

#===========================================#
# latihan 2: Implementasi Algoritma Kruskal #
#===========================================#

# daftar edge dengan format:
# (bobot, node1, node2)
edges = [
    (1, 'C', 'D'), # edge dari C ke D dengan bobot 1
    (2, 'A', 'C'), # edge dari A ke C dengan bobot 2
    (3, 'B', 'D'), # edge dari B ke D dengan bobot 3
    (4, 'A', 'B'), # edge dari A ke B dengan bobot 4
    (5, 'A', 'D') # edge dari A ke D dengan bobot 5
]

# mengurutkan edge berdasarkan bobot terkecil
edges.sort()

# list untuk menyimpan edge yang masuk ke MST
mst = []

# variabel untuk menyimpan total bobot MST
total_weight = 0

# set untuk menyimpan node yang sudah terhubung
connected = set()

# melakukan perulangan untuk setiap edge
for weight, u, v in edges:

    # memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:

        # menambahkan edge ke MST
        mst.append((u, v, weight))

        # menambahkan bobot edge ke total bobot
        total_weight += weight

        # menandai node sudah terhubung
        connected.add(u)
        connected.add(v)

# menampilkan hasil MST
print("Minimum Spanning Tree: ")

# perulangan untuk menampilkan setiap edge pada MST
for edge in mst:
    print(edge)

# menampilkan total bobot MST
print("Total bobot = ", total_weight)

#=============================#
# jawaban pertanyaan analisis #
#=============================#
'''
1. Edge mana yang dipilih pertama kali? 
edge ('C', 'D') dengan bobot 1 karena memiliki bobot paling kecil.

2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu? 
karena algoritma kruskal bekerja dengan memilih edge
berbobot minimum terlebih dahulu agar total bobot MST 
menjadi sekecil mungkin.

3. Berapa total bobot MST yang dihasilkan?
total bobot MST yang dihasilkan adalah 6.

4. Mengapa edge tertentu tidak dipilih? 
karena edge tersebut dapat membentuk cycle atau 
node-node nya sudah terhubung melalui edge lain.
'''