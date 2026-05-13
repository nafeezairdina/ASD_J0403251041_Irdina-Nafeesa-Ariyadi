#=========================================#
# Nama: Irdina Nafeesa Ariyadi            #
# NIM: J0403251041                        #
# Kelas: TPL B1                           #
# Praktikum 13 - Graph III: Spanning Tree #
#=========================================#

#=====================================================#
# latihan 4: Studi Kasus: Jaringan Kabel Antar Gedung #
#=====================================================#

# daftar edge dengan format: (bobot, gedung1, gedung2)
edges = [
    (4, 'GedungA', 'GedungB'), # biaya kabel dari GedungA ke GedungB
    (2, 'GedungA', 'GedungC'), # biaya kabel dari GedungA ke GedungC
    (3, 'GedungB', 'GedungD'), # biaya kabel dari GedungB ke GedungD
    (1, 'GedungC', 'GedungD'), # biaya kabel dari GedungC ke GedungD
    (5, 'GedungA', 'GedungD') # biaya kabel dari GedungA ke GedungD
]

# mengurutkan edge berdasarkan bobot terkecil
edges.sort()

# list untuk menyimpan hasil Minimum Spanning Tree
mst = []

# variabel untuk menyimpan total biaya minimum
total_biaya = 0

# set untuk menyimpan node yang sudah terhubung
connected = set()

# proses algoritma Kruskal
for weight, u, v in edges:

    # memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:

        # menambahkan edge ke MST
        mst.append((u, v, weight))

        # menambahkan bobot ke total biaya
        total_biaya += weight

        # menandai node sudah terhubung
        connected.add(u)
        connected.add(v)

# menampilkan hasil jaringan minimum
print("Jaringan Kabel Minimum: ")

# menampilkan edge yang dipilih
for edge in mst:
    print(edge)

# menampilkan total biaya minimum
print("Total biaya minimum = ", total_biaya)

#=============================#
# jawaban pertanyaan analisis #
#=============================#
'''
1. Algoritma apa yang digunakan?
algoritma yang digunakan adalah Kruskal.

2. Edge mana saja yang dipilih?
('GedungC', 'GedungD', 1)
('GedungA', 'GedungC', 2)
('GedungB', 'GedungD', 3)

3. Berapa total biaya minimum?
total biaya minimum yang dihasilkan adalah 6.

4. Mengapa MST cocok digunakan pada kasus ini?
karena MST dapat menghubungkan semua gedung dengan 
total biaya paling minimum tanpa membentuk 
cycle sehingga lebih efisien.
'''