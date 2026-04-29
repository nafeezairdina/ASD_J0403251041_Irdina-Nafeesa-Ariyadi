#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#==========================#
# Implementasi Dasar Graph #
#==========================#

# representasi graph
graph = {
    'A':['B','C'],
    'B':['A','D'],
    'C':['A','D'],
    'D':['B','C']
}

for node in graph:
    print(node, "->", graph[node]) 