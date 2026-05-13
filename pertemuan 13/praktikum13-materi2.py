#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#=======================================#
# materi 2: Implementasi Algoritma Prim #
#=======================================#

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

    # menyimpan node yang sudah dikunjungi
    visited = set([start])

    # list untuk menyimpan edge yang akan diproses
    edges = []

    # memasukkan semua edge dari node awal ke priority queue
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    # list untuk menyimpan hasil Minimum Spanning Tree
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

            # menambahkan bobot ke total bobot
            total_weight += weight

            # mengecek semua tetangga dari node v
            for neighbor, w in graph[v].items():

                # jika neighbor belum dikunjungi
                if neighbor not in visited:

                    # masukkan edge ke priority queue
                    heapq.heappush(edges, (w, v, neighbor))

    # mengembalikan hasil MST dan total bobot
    return mst, total_weight

# memanggil fungsi prim dimulai dari node A
mst, total = prim(graph, 'A')

# menampilkan hasil MST
print("Minimum Spanning Tree: ")

# menampilkan setiap edge dalam MST
for edge in mst:
    print(edge)

# menampilkan total bobot MST
print("Total bobot = ", total)