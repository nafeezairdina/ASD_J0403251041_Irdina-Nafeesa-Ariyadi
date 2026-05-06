#========================================#
# Nama: Irdina Nafeesa Ariyadi           #
# NIM: J0403251041                       #
# Kelas: TPL B1                          #
# Praktikum 12 - Graph II: Shortest Path #
#========================================#

#=====================================================#
# latihan 5: Studi Kasus dengan Program Shortest Path #
#=====================================================#

import heapq 

# graph berbobot antar kota (satuan = jam perjalanan)
# format: {kota: {kota_tujuan: waktu}}
graph = { 
    'bogor': {
        'jakarta': 5, # bogor -> jakarta = 5 jam
        'depok': 2 # bogor -> depok = 2 jam
    },
    'depok': {
        'jakarta': 2, # depok -> jakarta = 2 jam
        'bandung': 6 # depok -> bandung = 6 jam
    },
    'jakarta': {
        'bandung': 7 # jakarta -> bandung = 7 jam
    },
    'bandung': {} # bandung = tujuan akhir
} 

def dijkstra(graph, start): 
    ''' 
    algoritma dijkstra untuk mencari jarak terpendek dari start ke semua kota
    '''
    # inisialisasi jarak awal = tak hingga
    distances = {kota: float('inf') for kota in graph} 
    distances[start] = 0 
    
    # priority queue: (jarak, kota)
    priority_queue = [(0, start)] 
    
    while priority_queue: 
        # ambil kota dengan jarak terkecil
        current_distance, current_kota = heapq.heappop(priority_queue) 
        
        # skip jika jarak sudah lebih optimal
        if current_distance > distances[current_kota]: 
            continue 
        
        # cek semua kota tetangga
        for neighbor, weight in graph[current_kota].items():
            distance = current_distance + weight 
            
            # update jika jalur lebih cepat
            if distance < distances[neighbor]: 
                distances[neighbor] = distance 
                heapq.heappush(priority_queue, (distance, neighbor)) 
    
    return distances

# node awal = bogor
node_awal = 'bogor'
hasil = dijkstra(graph, node_awal) 

print(f"jarak terpendek dari {node_awal.upper()}:") 
for kota, jarak in hasil.items(): 
    print(f"{node_awal.capitalize()} -> {kota.capitalize()} = {jarak}") 

#=============================#
# jawaban pertanyaan analisis #
#=============================#
'''
1. node awal yang digunakan apa? 
   jawaban: bogor

2. node mana yang memiliki jarak paling kecil dari node awal? 
   jawaban: depok (2 jam)

3. node mana yang memiliki jarak paling besar dari node awal? 
   jawaban: bandung (8 jam)

4. jelaskan bagaimana algoritma dijkstra bekerja pada kasus yang anda buat.
   jawaban: 
   - mulai dari bogor (jarak = 0)
   - proses depok(2) < jakarta(5) -> update jakarta = 2+2 = 4
   - dari jakarta(4) coba bandung = 4+7 = 11
   - dari depok(2) coba bandung = 2+6 = 8 (lebih kecil)
   - final: bogor = 0, depok = 2, jakarta = 4, bandung = 8
'''