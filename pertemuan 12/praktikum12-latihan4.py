#========================================#
# Nama: Irdina Nafeesa Ariyadi           #
# NIM: J0403251041                       #
# Kelas: TPL B1                          #
# Praktikum 12 - Graph II: Shortest Path #
#========================================#

#====================================================================#
# latihan 4: Studi Kasus Contoh: Jalur Terpendek Antar Lokasi Kampus #
#====================================================================#

import heapq 

# graph lokasi kampus 
# bobot = waktu tempuh dalam menit 
graph = { 
    'gerbang': {'perpustakaan': 6, 'kantin': 2}, # gerbang ke perpustakaan(6), kantin(2)
    'perpustakaan': {'lab': 3}, # perpustakaan ke lab(3)
    'kantin': {'lab': 4, 'aula': 7}, # kantin ke lab(4), aula(7)
    'lab': {'aula': 1},  # lab ke aula(1)
    'aula': {} # aula = tujuan akhir
} 

def dijkstra(graph, start): 
    # inisialisasi semua jarak tak hingga 
    distances = {node: float('inf') for node in graph} 
    distances[start] = 0 
    priority_queue = [(0, start)] 
    
    while priority_queue: 
        # ambil lokasi dengan waktu tempuh terkecil
        current_distance, current_node = heapq.heappop(priority_queue) 
        
        # skip jika jarak sudah lebih optimal
        if current_distance > distances[current_node]: 
            continue 
        
        # cek semua lokasi tetangga
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight 
            
            # update jika jalur lebih cepat
            if distance < distances[neighbor]: 
                distances[neighbor] = distance 
                heapq.heappush(priority_queue, (distance, neighbor)) 

    # kembalikan dictionary jarak terpendek ke semua node
    return distances

# hitung waktu tempuh dari gerbang ke semua lokasi
hasil = dijkstra(graph, 'gerbang') 
print("waktu tempuh terpendek dari gerbang kampus:") 
for lokasi, jarak in hasil.items(): 
    print(f"{lokasi} = {jarak} menit") 

#=============================#
# jawaban pertanyaan analisis #
#=============================#
'''
1. lokasi mana yang paling dekat dari gerbang? 
   jawaban: kantin (2 menit)

2. berapa waktu tempuh terpendek dari gerbang ke aula? 
   jawaban: 9 menit (gerbang -> kantin -> lab -> aula: 2+4+1+2? wait, 2+4+1=7)

3. apakah jalur langsung selalu menghasilkan jarak paling kecil? jelaskan. 
   jawaban: 
   tidak! contoh gerbang -> aula tidak ada jalur langsung
   algoritma cari jalur kombinasi: gerbang->kantin->lab->aula = 7 menit

4. mengapa dijkstra cocok digunakan pada kasus lokasi kampus ini?
   jawaban: 
   - semua bobot positif (waktu tempuh > 0)
   - efisien O((V+E)logV) untuk graph kecil
   - priority queue proses lokasi terdekat dulu (greedy optimal)
'''