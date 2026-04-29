#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#=========================================#
# Implementasi BFS (Breadth-First Search) #
#=========================================#

# struktur data untuk membuat antrian, kita gunakan dari library collections bawaan phyton
from collections import deque

# representasi graph
graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':[],
    'E':[],
    'F':[],
    'G':[]
}

# fungsi untuk melakukan penelusuran graph dengan BFS
def bfs(graph, start): # graph: dict yang menyimpan struktur dari graph # start: node awal penelusuran
    # queue digunsksn untuk menyimpan node yang akan diproses/dibaca
    queue = deque() 
    
    # var yang digunakan untuk menyimpan node yang sudah diproses/dikunjungi
    visited = set() 

    # masukkan node awal ke queue
    queue.append(start) 

    # tandai node awal sebagai node yang sudah dikunjungi
    visited.add(start) 

    while queue:
        # mengambil node paling depan dari queue
        node = queue.popleft()
        # tampilkan node yang sedang di kunjungi
        print(node, end=" ")
        # periksa semua tetangga dari node yang diambil
        for neighbor in graph[node]:
            # jika tetangga belum dikunjungi
            if neighbor not in visited:
                # tandai sebagai sudah dikunjungi
                visited.add(neighbor)
                # masukkan tetangga ke queue untuk diproses nanti
                queue.append(neighbor)

# menjalankan BFS dari node A
bfs(graph, 'A')