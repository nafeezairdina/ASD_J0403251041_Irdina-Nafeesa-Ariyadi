#========================================#
# Nama: Irdina Nafeesa Ariyadi           #
# NIM: J0403251041                       #
# Kelas: TPL B1                          #
# Praktikum 12 - Graph II: Shortest Path #
#========================================#

#=================================================#
# latihan 1: weighted graph dan perhitungan jalur #
#=================================================#

# representasi graph berbobot dalam bentuk dictionary
graph = { 
    'A': {'B': 4, 'C': 2}, # a terhubung ke b(4), c(2)
    'B': {'D': 5}, # b terhubung ke d(5)
    'C': {'D': 1}, # c terhubung ke d(1)
    'D': {} # d adalah node tujuan (tidak ada keluar)
} 

# menghitung dua kemungkinan jalur dari a ke d secara manual
jalur_1 = graph['A']['B'] + graph['B']['D']  # a->b->d: 4 + 5
jalur_2 = graph['A']['C'] + graph['C']['D']  # a->c->d: 2 + 1

print("jalur 1: A -> B -> D =", jalur_1) 
print("jalur 2: A -> C -> D =", jalur_2)

# bandingkan total bobot, pilih yang terkecil
if jalur_1 < jalur_2: 
    print("jalur terpendek adalah A -> B -> D") 
else: 
    print("jalur terpendek adalah A -> C -> D") 

#=============================#
# jawaban pertanyaan analisis #
#=============================#
'''
1. berapa total bobot jalur A -> B -> D?
   jawaban: 9 (4 + 5)

2. berapa total bobot jalur A -> C -> D?
   jawaban: 3 (2 + 1)

3. jalur mana yang dipilih sebagai jalur terpendek?
   jawaban: A -> C -> D (total bobot 3 < 9)

4. mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?
   jawaban: karena dalam weighted graph, kriteria "terpendek" adalah 
            total bobot (weight) paling kecil, bukan jumlah edge.
            contoh:
            - A -> b -> D: 2 edge, bobot 9
            - A -> C -> D: 2 edge, bobot 3
            meski jumlah edge sama, A -> C -> D lebih pendek karena bobot total lebih kecil.
'''