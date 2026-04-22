#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#============================================#
# latihan 4: membuat BST yang tidak seimbang #
#============================================#

# mendefinisikan class Node untuk menyimpan data BST
class Node:
    def __init__(self, data):
        self.data = data # nilai pada node
        self.left = None # child kiri
        self.right = None # child kanan

# fungsi insert untuk BST
def insert(root, data):
    # jika root kosong, buat node baru
    if root is None:
        return Node(data)

    # jika data lebih kecil, masuk ke subtree kiri
    if data < root.data:
        root.left = insert(root.left, data)

    # jika data lebih besar, masuk ke subtree kanan
    elif data > root.data:
        root.right = insert(root.right, data)

    return root

# membuat traversal preorder: root => left => right
def preorder(root):
    if root is not None:
        print(root.data, end=" ") # root
        preorder(root.left) # left
        preorder(root.right) # right

# fungsi rekursif untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="root"):
    if root is not None:
        # cetak node dengan indentasi sesuai kedalamannya
        print("   " * level + f"{posisi}: {root.data}")
        # rekursi ke child kiri dengan level bertambah
        tampil_struktur(root.left, level + 1, "L")
        # rekursi ke child kanan dengan level bertambah
        tampil_struktur(root.right, level + 1, "R")

#===============# 
# program utama #
#===============#
root = None 
data_list = [10, 20, 30]

for data in data_list: 
    root = insert(root, data) 

print("preorder BST:") 
preorder(root) 

print("\n\nstruktur BST: ") 
tampil_struktur(root) 

# penjelasan
'''
latihan 1 adalah class node, setiap simpul punya nilai data, pointer child kiri, dan pointer child kanan.

latihan 2 adalah fungsi insert yang bekerja secara rekursif. data yang lebih kecil dari root masuk ke 
subtree kiri dan yang lebih besar masuk ke subtree kanan. data yang dimasukkan adalah [10, 20, 30] yang 
nilainya selalu naik, jadi setiap node baru selalu masuk ke subtree kanan terus, sehingga BST yang terbentuk 
tidak seimbang dan condong ke kanan.

latihan 3 adalah traversal preorder yang menelusuri BST dengan pola root dulu, lalu subtree kiri, 
lalu subtree kanan secara rekursif. karena BST-nya condong ke kanan, outputnya adalah 10 20 30 yang 
mencerminkan urutan dari root ke bawah.
'''