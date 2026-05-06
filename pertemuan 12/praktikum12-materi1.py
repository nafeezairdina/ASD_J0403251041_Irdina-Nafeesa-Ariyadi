#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#==============================#
# materi 1: Algoritma Dijkstra #
#==============================#

import heapq 

# representasi graph berbobot dalam bentuk dictionary
graph = { 
    'A': {'B': 4, 'C': 2}, # a terhubung ke b(4), c(2)
    'B': {'D': 5}, # b terhubung ke d(5)
    'C': {'D': 1}, # c terhubung ke d(1)
    'D': {} # d adalah node tujuan (tidak ada keluar)
} 

def dijkstra(graph, start): 
    # inisialisasi jarak: semua node tak hingga kecuali start
    distances = {node: float('inf') for node in graph} 
 
    # jarak node start = 0
    distances[start] = 0 
 
    # priority queue (min-heap) berisi (jarak, node)
    pq = [(0, start)] 
 
    while pq: 
        # ambil node dengan jarak terkecil dari priority queue
        current_distance, current_node = heapq.heappop(pq) 
 
        # periksa semua tetangga dari current_node
        for neighbor, weight in graph[current_node].items(): 

            # hitung jarak baru melalui current_node
            distance = current_distance + weight 
 
            # jika ditemukan jalur lebih pendek, update jarak
            if distance < distances[neighbor]: 
                distances[neighbor] = distance

                # masukkan ke priority queue dengan jarak baru
                heapq.heappush(pq, (distance, neighbor)) 

    # kembalikan dictionary jarak terpendek ke semua node        
    return distances 
 
# jalankan dijkstra dari node 'a' dan tampilkan hasil
hasil = dijkstra(graph, 'A') 
print(hasil)