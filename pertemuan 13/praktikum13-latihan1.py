#=========================================#
# Nama: Irdina Nafeesa Ariyadi            #
# NIM: J0403251041                        #
# Kelas: TPL B1                           #
# Praktikum 13 - Graph III: Spanning Tree #
#=========================================#

#==========================================#
# latihan 1: Memahami Konsep Spanning Tree #
#==========================================#

# daftar edge pada graph
# setiap tuple menunjukkan hubungan antar node
edges = [
    ('A', 'B'), # edge antara A dan B
    ('A', 'C'), # edge antara A dan C
    ('A', 'D'), # edge antara A dan D
    ('C', 'D'), # edge antara C dan D
    ('B', 'D') # edge antara B dan D
]

# contoh spanning tree dari graph
# spanning tree harus menghubungkan semua node, tanpa membentuk cycle
spanning_tree = [
    ('A', 'C'), # edge A ke C
    ('C', 'D'), # edge C ke D
    ('D', 'B') # edge D ke B
]

# menampilkan semua edge pada graph
print("Edge pada graph: ")

# perulangan untuk mencetak setiap edge
for edge in edges:
    print(edge)

# menampilkan judul spanning tree
print("\nSpanning Tree: ")

# perulangan untuk mencetak edge pada spanning tree
for edge in spanning_tree:
    print(edge)

# menampilkan jumlah edge pada graph asli
print("\nJumlah edge graph = ", len(edges))

# menampilkan jumlah edge pada spanning tree
print("Jumlah edge spanning tree = ", len(spanning_tree))

#=============================#
# jawaban pertanyaan analisis #
#=============================#
'''
1. Apa perbedaan graph awal dan spanning tree? 
graph awal memiliki lebih banyak edge dan dapat memiliki cycle,
sedangkan spanning tree hanya mengambil edge penting untuk
menghubungkan semua node tanpa cycle.

2. Mengapa spanning tree tidak boleh memiliki cycle? 
karena jika terdapat cycle maka jalur menjadi berputar
dan tidak memenuhi konsep tree yang harus bebas cycle.

3. Mengapa jumlah edge spanning tree selalu lebih sedikit? 
karena spanning tree hanya menggunakan edge minimum
untuk menghubungkan semua node.
jumlah edge pada spanning tree selalu = jumlah vertex - 1.
'''