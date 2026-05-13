#=========================================#
# Nama: Irdina Nafeesa Ariyadi            #
# NIM: J0403251041                        #
# Kelas: TPL B1                           #
# Praktikum 13 - Graph III: Spanning Tree #
#=========================================#

#========================================#
# latihan 3: Implementasi Algoritma Prim #
#========================================#

# import library heapq untuk membuat priority queue
import heapq

# representasi weighted graph menggunakan dictionary
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5}, # node A terhubung ke B, C, dan D
    'B': {'A': 4, 'D': 3}, # node B terhubung ke A dan D
    'C': {'A': 2, 'D': 1}, # node C terhubung ke A dan D
    'D': {'A': 5, 'B': 3, 'C': 1} # node D terhubung ke A, B, dan C
}

# fungsi algoritma Prim
def prim(graph, start):

    # set untuk menyimpan node yang sudah dikunjungi
    visited = set([start])

    # list untuk menyimpan edge yang akan diproses
    edges = []

    # memasukkan semua edge dari node awal ke priority queue
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    # list untuk menyimpan hasil MST
    mst = []

    # variabel untuk menyimpan total bobot MST
    total_weight = 0

    # perulangan selama masih ada edge
    while edges:

        # mengambil edge dengan bobot terkecil
        weight, u, v = heapq.heappop(edges)

        # mengecek apakah node tujuan belum dikunjungi
        if v not in visited:

            # menandai node sudah dikunjungi
            visited.add(v)

            # menambahkan edge ke MST
            mst.append((u, v, weight))

            # menambahkan bobot edge ke total
            total_weight += weight

            # mengecek semua tetangga node v
            for neighbor, w in graph[v].items():

                # jika neighbor belum dikunjungi
                if neighbor not in visited:

                    # memasukkan edge baru ke priority queue
                    heapq.heappush(edges, (w, v, neighbor))

    # mengembalikan hasil MST dan total bobot
    return mst, total_weight


# memanggil fungsi Prim dimulai dari node A
mst, total = prim(graph, 'A')

# menampilkan hasil MST
print("Minimum Spanning Tree: ")

# menampilkan setiap edge dalam MST
for edge in mst:
    print(edge)

# menampilkan total bobot MST
print("Total bobot = ", total)

#=============================#
# jawaban pertanyaan analisis #
#=============================#
'''
1. Node awal apa yang digunakan?
node awal yang digunakan adalah A.

2. Edge mana yang dipilih pertama kali?
edge pertama yang dipilih adalah ('A', 'C')
karena memiliki bobot paling kecil yaitu 2.

3. Bagaimana Prim menentukan edge berikutnya?
algoritma Prim memilih edge dengan bobot terkecil
yang terhubung ke node yang sudah dikunjungi
tanpa membentuk cycle.

4. Berapa total bobot MST yang dihasilkan?
total bobot MST yang dihasilkan adalah 6.

5. Apa perbedaan pendekatan Prim dan Kruskal?
Prim memulai dari satu node lalu memperluas tree
sedikit demi sedikit berdasarkan edge terkecil.
sedangkan Kruskal langsung memilih edge terkecil
dari seluruh graph tanpa memulai dari node tertentu.
'''