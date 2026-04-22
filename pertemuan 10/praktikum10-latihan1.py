#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#===============================#
# latihan 1: Binary Search Tree #
#===============================#

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

# inisialisasi root kosong
root = None
# data yang akan dimasukkan ke dalam BST
data_list = [50, 30, 70, 20, 40, 60, 80]

for data in data_list:
    root = insert(root, data) # root diperbarui setiap iterasi

print("BST berhasil dibuat")

#==============================#
# latihan 2: traversal inorder #
#==============================#

# membuat traversal inorder: left => root => right
def inorder(root):
    if root is not None:
        inorder(root.left) # left
        print(root.data, end=" ") # root
        inorder(root.right) # right

print("hasil inorder: ")
inorder(root)

#==========================#
# latihan 3: Search di BST #
#==========================#

# fungsi untuk mencari nilai (key) di dalam BST
def search(root, key):
    # base case: node tidak ditemukan
    if root is None:
        return False
    
    # jika nilai node saat ini sama dengan key, data ditemukan
    if root.data == key:
        return True
    # jika key lebih kecil, cari ke subtree kiti
    elif key < root.data:
        return search(root.left, key)
    # jika key lebih besar, cari ke subtree kanan
    else:
        return search(root.right, key)

# uji pencarian
key = 40
if search(root, key):
    print("data ditemukan")
else:
    print("data tidak ditemukan")

# penjelasan
'''
latihan 1 adalah membangun BST. di sini dibuat class node yang jadi cetakan tiap simpul BST, 
di mana setiap simpul punya nilai data, pointer child kiri, dan pointer child kanan. 
fungsi insert bekerja secara rekursif untuk menempatkan data di posisi yang tepat, 
masuk ke subtree kiri kalau lebih kecil dari root dan ke subtree kanan kalau lebih besar. 
data yang dimasukkan adalah [50, 30, 70, 20, 40, 60, 80] dengan 50 sebagai root, 
jadi terbentuk BST yang cukup seimbang dengan tiga tingkatan.

latihan 2 adalah menampilkan isi BST pakai traversal inorder. cara kerjanya sederhana, 
telusuri subtree kiri dulu, cetak nilainya, lalu telusuri subtree kanan, dan ini dilakukan 
secara rekursif di setiap node. karena sifat BST, cara ini selalu menghasilkan urutan dari 
kecil ke besar, jadi outputnya adalah 20 30 40 50 60 70 80.

latihan 3 adalah fitur search. fungsi search menerima root dan nilai yang mau dicari (key), 
lalu mulai menelusurinya dari root. di tiap node, kalau key lebih kecil lanjut ke subtree kiri, 
kalau lebih besar lanjut ke subtree kanan, kalau sama berarti data ditemukan. kalau BST sudah habis 
ditelusuri tapi tidak ketemu, fungsi mengembalikan false. di pengujiannya dicari nilai 40, 
dan karena 40 memang ada di BST, outputnya adalah "data ditemukan".
'''