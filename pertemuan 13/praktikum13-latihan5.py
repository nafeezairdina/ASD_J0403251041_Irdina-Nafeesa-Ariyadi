#=========================================#
# Nama: Irdina Nafeesa Ariyadi            #
# NIM: J0403251041                        #
# Kelas: TPL B1                           #
# Praktikum 13 - Graph III: Spanning Tree #
#=========================================#

#==============================================================#
# latihan 5: Tugas Mandiri: Buat Program MST dengan Kasus Baru #
# kasus 2: Jaringan Komputer                                   #
#==============================================================#

# daftar edge dengan format: (bobot, router1, router2)
edges = [
    (3, 'RouterA', 'RouterB'), # koneksi RouterA ke RouterB
    (2, 'RouterA', 'RouterC'), # koneksi RouterA ke RouterC
    (5, 'RouterB', 'RouterD'), # koneksi RouterB ke RouterD
    (1, 'RouterC', 'RouterD'), # koneksi RouterC ke RouterD
    (4, 'RouterB', 'RouterC') # koneksi RouterB ke RouterC
]

# mengurutkan edge berdasarkan bobot terkecil
edges.sort()

# list untuk menyimpan hasil MST
mst = []

# variabel untuk menyimpan total bobot minimum
total_weight = 0

# set untuk menyimpan node yang sudah terhubung
connected = set()

# proses algoritma Kruskal
for weight, u, v in edges:

    # memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:

        # menambahkan edge ke MST
        mst.append((u, v, weight))

        # menambahkan bobot ke total MST
        total_weight += weight

        # menandai router sudah terhubung
        connected.add(u)
        connected.add(v)

# menampilkan hasil MST
print("Minimum Spanning Tree: ")

# menampilkan edge yang dipilih
for edge in mst:
    print(edge)

# menampilkan total bobot minimum
print("Total bobot minimum = ", total_weight)

#=============================#
# jawaban pertanyaan analisis #
#=============================#
'''
1. Kasus apa yang dipilih?
kasus yang dipilih adalah jaringan komputer.

2. Algoritma apa yang digunakan?
algoritma yang digunakan adalah Kruskal.

3. Edge mana saja yang dipilih dalam MST?
('RouterC', 'RouterD', 1)
('RouterA', 'RouterC', 2)
('RouterA', 'RouterB', 3)

4. Berapa total bobot MST?
total bobot MST adalah 6.

5. Mengapa edge tertentu tidak dipilih?
karena edge tersebut memiliki bobot lebih besar
atau dapat membentuk cycle sehingga tidak efisien
untuk MST.
'''