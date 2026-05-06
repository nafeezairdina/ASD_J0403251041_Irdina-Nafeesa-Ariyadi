#========================================#
# Nama: Irdina Nafeesa Ariyadi           #
# NIM: J0403251041                       #
# Kelas: TPL B1                          #
# Praktikum 12 - Graph II: Shortest Path #
#========================================#

#==================================#
# latihan 2: Implementasi Dijkstra #
#==================================#

import heapq 

# representasi graph berbobot dalam bentuk dictionary
graph = { 
    'A': {'B': 4, 'C': 2}, # a terhubung ke b(4), c(2)
    'B': {'D': 5}, # b terhubung ke d(5)
    'C': {'D': 1}, # c terhubung ke d(1)
    'D': {} # d adalah node tujuan (tidak ada keluar)
} 

def dijkstra(graph, start): 
    '''
    fungsi untuk mencari jarak terpendek dari node start 
    ke seluruh node lain menggunakan algoritma Dijkstra. 
    '''
    # semua jarak awal dibuat tak hingga 
    distances = {node: float('inf') for node in graph} 

    # jarak dari start ke start adalah 0 
    distances[start] = 0 

    # priority queue menyimpan pasangan (jarak, node) 
    priority_queue = [(0, start)]

    while priority_queue: 
        current_distance, current_node = heapq.heappop(priority_queue) 
 
        # jika jarak saat ini lebih besar dari jarak yang sudah tercatat, 
        # maka proses dilewati 
        if current_distance > distances[current_node]: 
            continue 
 
        # periksa semua tetangga dari node saat ini 
        for neighbor, weight in graph[current_node].items(): 
            distance = current_distance + weight 
 
            # jika ditemukan jarak yang lebih kecil, perbarui jaraknya 
            if distance < distances[neighbor]: 
                distances[neighbor] = distance 
                heapq.heappush(priority_queue, (distance, neighbor)) 
    
    # kembalikan dictionary jarak terpendek ke semua node
    return distances
 
hasil = dijkstra(graph, 'A') 
print("jarak terpendek dari node A:") 
for node, distance in hasil.items(): 
    print(node, "=", distance)

#=============================#
# jawaban pertanyaan analisis #
#=============================#
'''
1. berapa jarak terpendek dari A ke B? 
   jawaban: 4 (langsung A -> B)

2. berapa jarak terpendek dari A ke C? 
   jawaban: 2 (langsung A -> C)

3. berapa jarak terpendek dari A ke D? 
   jawaban: 3 (A -> C -> D: 2+1)

4. mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B? 
   jawaban: 
   - melalui B: A -> B -> D = 4 + 5 = 9
   - melalui C: A -> C -> D = 2 + 1 = 3
   algoritma dijkstra otomatis memilih jalur dengan total bobot terkecil

5. apa fungsi priority_queue dalam algoritma dijkstra? 
   jawaban: 
   - menyimpan node yang belum diproses dengan urutan jarak terkecil
   - heapq.heappop() selalu ambil node dengan jarak minimum
   - memastikan node diproses secara greedy (jarak terkecil dulu)

6. mengapa dijkstra tidak cocok untuk graph dengan bobot negatif? 
   jawaban: 
   - dijkstra asumsi "sekali diproses, jarak final" (greedy)
   - bobot negatif bisa membuat jarak berubah setelah diproses
   - priority queue tidak bisa handle update negatif dengan benar
   - solusi: gunakan bellman-ford untuk graph dengan edge negatif
'''