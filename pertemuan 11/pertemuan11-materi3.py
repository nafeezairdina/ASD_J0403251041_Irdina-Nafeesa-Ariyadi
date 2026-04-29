#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#=======================================#
# Implementasi DFS (Depth-First Search) #
#=======================================#

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

# fungsi untuk melakukan penelusuran graph dengan DFS
def dfs(graph, node, visited): # graph: dict yang menyimpan struktur dari graph # node: menyimpan node yang sedang dikunjungi # visited: menyimpan node yang sudah dikunjungi
    # tandai node yang sedang dikunjungi
    visited.add(node)

    # tampilkan node yang sedang dikunjungi
    print(node, end=" ")

    # periksa semua tetangga dari node saat ini
    for neighbor in graph[node]:
        # jika tetangga belum pernah dikunjungi 
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# set kosong untuk menyimpan node yang sudah dikunjungi 
visited = set() 
# menjalankan DFS dari node A 
dfs(graph, 'A', visited)