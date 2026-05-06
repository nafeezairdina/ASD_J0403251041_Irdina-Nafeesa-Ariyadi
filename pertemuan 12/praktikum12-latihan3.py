#========================================#
# Nama: Irdina Nafeesa Ariyadi           #
# NIM: J0403251041                       #
# Kelas: TPL B1                          #
# Praktikum 12 - Graph II: Shortest Path #
#========================================#

#======================================#
# latihan 3: Implementasi Bellman-Ford #
#======================================#

# representasi graph berbobot dalam bentuk dictionary
graph = { 
    'A': {'B': 4, 'C': 2}, # a terhubung ke b(4), c(2)
    'B': {'D': 5}, # b terhubung ke d(5)
    'C': {'D': 1}, # c terhubung ke d(1)
    'D': {} # d adalah node tujuan (tidak ada keluar)
} 

def bellman_ford(graph, start): 
    ''' 
    Fungsi untuk mencari jarak terpendek dari node start 
    ke seluruh node lain menggunakan algoritma Bellman-Ford. 
    '''
    # semua jarak awal dibuat tak hingga 
    distances = {node: float('inf') for node in graph} 
 
    # jarak dari start ke start adalah 0 
    distances[start] = 0 
 
    # bellman-Ford melakukan relaksasi sebanyak jumlah node - 1 
    for _ in range(len(graph) - 1): 
 
        # periksa semua edge 
        for node in graph: 
            for neighbor, weight in graph[node].items(): 
 
                # jika jarak ke node saat ini sudah diketahui, 
                # dan ditemukan jarak yang lebih kecil ke neighbor, 
                # maka lakukan update jarak 
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]: 
                    distances[neighbor] = distances[node] + weight 

    # kembalikan dictionary jarak terpendek ke semua node
    return distances
 
hasil = bellman_ford(graph, 'A') 
print("jarak terpendek dari node A:") 
for node, distance in hasil.items(): 
    print(node, "=", distance)

#=============================#
# jawaban pertanyaan analisis #
#=============================#
'''
1. berapa bobot langsung dari A ke B? 
   jawaban: 4 (A -> B langsung)

2. berapa total bobot jalur A -> C -> B? 
   jawaban: ~ (tidak ada edge C -> B dalam graph ini)

3. jalur mana yang menghasilkan jarak lebih kecil menuju B? 
   jawaban: A -> B langsung (4) lebih kecil dari jalur lain

4. mengapa bellman-ford dapat digunakan pada graph dengan bobot negatif? 
   jawaban: 
   - melakukan relaksasi berulang |V|-1 kali untuk semua edge
   - bisa memperbaiki jarak meski ada bobot negatif
   - tidak ada asumsi greedy seperti dijkstra

5. apa yang dimaksud dengan proses relaksasi edge? 
   jawaban: 
   proses update jarak ke neighbor jika ditemukan jalur lebih pendek:
   if dist[node] + weight < dist[neighbor]:
       dist[neighbor] = dist[node] + weight

6. apa perbedaan utama bellman-ford dan dijkstra? 
   jawaban:
   - dijkstra: O((V+E)logV), pakai priority queue, tidak bisa bobot negatif
   - bellman-ford: O(VE), relaksasi penuh |V|-1 kali, bisa bobot negatif
'''