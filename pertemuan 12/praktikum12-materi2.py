#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#==================================#
# materi 2: Algoritma Bellman Ford #
#==================================#

import heapq 

# representasi graph berbobot dalam bentuk dictionary
graph = { 
    'A': {'B': 4, 'C': 2}, # a terhubung ke b(4), c(2)
    'B': {'D': 5}, # b terhubung ke d(5)
    'C': {'D': 1}, # c terhubung ke d(1)
    'D': {} # d adalah node tujuan (tidak ada keluar)
} 

def bellman_ford(graph, start): 
    # inisialisasi jarak awal: semua node tak hingga kecuali start = 0
    distances = {node: float('inf') for node in graph} 
    distances[start] = 0 

    # relaksasi berulang sebanyak |v|-1 kali untuk semua kemungkinan jalur
    for _ in range(len(graph) - 1): 

        # cek setiap node dalam graf
        for node in graph: 

            # cek setiap tetangga dan bobotnya
            for neighbor, weight in graph[node].items(): 
                
                # kondisi relaksasi: jika jalur lebih pendek, update jarak
                if distances[node] + weight < distances[neighbor]: 
                    distances[neighbor] = distances[node] + weight 

    # kembalikan dictionary jarak terpendek ke semua node
    return distances

# jalankan dijkstra dari node 'a' dan tampilkan hasil
hasil = bellman_ford(graph, 'A') 
print(hasil)