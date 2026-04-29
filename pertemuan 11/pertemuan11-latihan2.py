#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#================================================#
# latihan 2:  Studi Kasus DFS (Eksplorasi Jalur) #
#================================================#

#=========================================#
# Implementasi DFS (Depth-First Search)   #
#=========================================#

# representasi graph - jalur eksplorasi
graph = { 
    'A': ['B', 'C'], 
    'B': ['D', 'E'], 
    'C': ['F'], 
    'D': [], 
    'E': [], 
    'F': [] 
}

# fungsi untuk melakukan penelusuran graph dengan DFS (REKURSIF)
def dfs(graph, node, visited): # graph: dict struktur graph # node: node saat ini # visited: set node yang sudah dikunjungi
    # tandai node saat ini sebagai sudah dikunjungi
    visited.add(node) 
    
    # tampilkan node yang sedang dikunjungi
    print(node, end=" ") 
    
    # eksplorasi semua tetangga secara rekursif
    for neighbor in graph[node]: 
        # jika tetangga belum dikunjungi, lakukan DFS rekursif
        if neighbor not in visited: 
            dfs(graph, neighbor, visited) 

# set kosong untuk menyimpan node yang sudah dikunjungi 
visited = set()
print("DFS dari A:")
dfs(graph, 'A', visited)

#=============================#
# Jawaban Pertanyaan Analisis #
#=============================#
'''
1. DFS masuk ke vertex terdalam terlebih dahulu karena:
- DFS menggunakan prinsip rekursi yang bekerja seperti Stack (LIFO)
- setiap kali menemukan neighbor yang belum dikunjungi,
DFS langsung memanggil dirinya sendiri (rekursif) untuk menelusuri
neighbor tersebut tanpa menunggu neighbor lain di level yang sama
- proses ini berlanjut terus menerus sampai menemukan vertex yang
tidak memiliki neighbor baru (dead end), baru kemudian backtrack
ke vertex sebelumnya untuk mencoba jalur lain
- berbeda dengan BFS yang menggunakan Queue (FIFO) dan menelusuri
semua neighbor per level sebelum masuk ke level berikutnya
- contoh pada graph ini, dari A langsung masuk ke B, lalu D (dead end),
backtrack ke B, lanjut ke E (dead end), backtrack ke A, lanjut ke C,
lalu F (dead end) -> output: A B D E C F

2. jika urutan neighbor diubah, jalur penelusuran DFS akan berubah karena
DFS selalu memilih neighbor pertama yang tersedia untuk ditelusuri lebih dulu:
a. urutan neighbor asli: graph = {'A': ['B', 'C'], 'B': ['D', 'E'], ...}
output DFS: A B D E C F
(DFS masuk ke B dulu karena B adalah neighbor pertama A)
b. urutan neighbor dibalik: graph = {'A': ['C', 'B'], 'B': ['E', 'D'], ...}
output DFS: A C F B E D
(DFS masuk ke C dulu karena C menjadi neighbor pertama A)
kesimpulan: urutan neighbor dalam adjacency list menentukan urutan
cabang (path) mana yang akan dieksplorasi terlebih dahulu oleh DFS

3. perbandingan DFS vs BFS pada graph yang sama:
DFS output : A B D E C F -> masuk sedalam mungkin per cabang (rekursi/stack)
BFS output : A B C D E F -> menelusuri semua neighbor per level (queue)

- perbedaan utama berdasarkan materi modul:
a. struktur data yang digunakan:
DFS -> Stack / rekursi dengan prinsip LIFO (Last In First Out)
BFS -> Queue dengan prinsip FIFO (First In First Out)
b. cara menelusuri graph:
DFS -> masuk sedalam mungkin pada satu jalur/cabang dulu (depth-first)
BFS -> kunjungi semua tetangga satu level dulu sebelum ke level berikutnya
c. kegunaan sesuai modul:
DFS -> eksplorasi semua jalur, backtracking, deteksi siklus (cycle),
penelusuran struktur seperti folder, maze, atau jaringan hubungan
BFS -> mencari jalur terpendek (shortest path) pada graph tidak berbobot,
menelusuri jaringan per level, simulasi penyebaran informasi
d. penggunaan visited:
keduanya sama-sama membutuhkan visited (set) untuk mencatat vertex
yang sudah dikunjungi agar tidak diproses ulang, terutama jika graph
memiliki siklus (cycle) yang dapat menyebabkan penelusuran tanpa akhir
'''