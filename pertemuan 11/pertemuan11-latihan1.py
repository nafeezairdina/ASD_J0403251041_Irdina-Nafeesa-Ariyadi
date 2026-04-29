#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#====================================================#
# latihan 1: Studi Kasus BFS (Jalur Terdekat Lokasi) #
#====================================================#

# struktur data untuk membuat antrian, kita gunakan dari library collections bawaan python
from collections import deque

# representasi graph 
graph = { 
    'Rumah': ['Sekolah', 'Toko'], 
    'Sekolah': ['Perpustakaan'], 
    'Toko': ['Pasar'], 
    'Perpustakaan': [], 
    'Pasar': [] 
}

# fungsi untuk melakukan penelusuran graph dengan BFS
def bfs(graph, start): # graph: dict yang menyimpan struktur dari graph # start: node awal penelusuran
    # queue digunakan untuk menyimpan node yang akan diproses/dibaca 
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

# menjalankan BFS dari node 'Rumah'
print("urutan kunjungan BFS dari Rumah: ")
bfs(graph, 'Rumah')

#=============================#
# Jawaban Pertanyaan Analisis #
#=============================#
'''
1. node yang dikunjungi pertama adalah 'Rumah' karena merupakan node start 
yang langsung dimasukkan ke queue dan diproses terlebih dahulu.

2. BFS cocok untuk mencari jalur terdekat karena:
- menggunakan prinsip FIFO (First In First Out) melalui queue
- mengeksplorasi node secara level demi level dari start node
- node pertama kali ditemukan pasti berada di level terdekat
- menjamin shortest path (jalur dengan jumlah edge minimum) 
pada graph yang tidak memiliki bobot pada edge

3. urutan BFS akan berubah jika:
a. urutan tetangga dalam list adjacency diubah:
graph = {'Rumah': ['Toko', 'Sekolah'], ...}
Output: Rumah Toko Sekolah Pasar Perpustakaan

b. struktur koneksi ditambah/hapus:
graph['Toko'] = ['Pasar', 'Perpustakaan']
output: Rumah Sekolah Toko Perpustakaan Pasar

c. node start berbeda:
bfs(graph, 'Sekolah')
output: Sekolah Perpustakaan
'''
