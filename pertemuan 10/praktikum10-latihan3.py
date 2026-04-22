#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#==========================================#
# latihan 5: rotasi kiri pada BST          #
#==========================================#

# mendefinisikan class Node untuk menyimpan data BST
class Node:
    def __init__(self, data):
        self.data = data # nilai pada node
        self.left = None # child kiri
        self.right = None # child kanan

# membuat traversal preorder: root => left => right
def preorder(root):
    if root is not None:
        print(root.data, end=" ") # root
        preorder(root.left) # left
        preorder(root.right) # right

# fungsi rekursif untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        # cetak node dengan indentasi sesuai kedalamannya
        print("   " * level + f"{posisi}: {root.data}")
        # rekursi ke child kiri dengan level bertambah
        tampil_struktur(root.left, level + 1, "L")
        # rekursi ke child kanan dengan level bertambah
        tampil_struktur(root.right, level + 1, "R")

# fungsi rotasi kiri untuk menyeimbangkan BST yang condong ke kanan
def rotate_left(x):
    y  = x.right # y adalah child kanan x, akan menjadi root baru
    T2 = y.left # subtree kiri milik y disimpan sementara

    # proses rotasi: x turun menjadi child kiri y
    y.left  = x # x menjadi child kiri dari y
    x.right = T2 # child kanan x diganti dengan T2

    return y

#===============#
# program utama #
#===============#
root = Node(10)
root.right = Node(20)
root.right.right = Node(30)

print("preorder sebelum rotasi kiri:")
preorder(root)

print("\n\nstruktur sebelum rotasi kiri:")
tampil_struktur(root)

# melakukan rotasi kiri pada root
root = rotate_left(root)

print("\npreorder sesudah rotasi kiri:")
preorder(root)

print("\n\nstruktur sesudah rotasi kiri:")
tampil_struktur(root)

# penjelasan
'''
bagian pertama adalah class node, setiap simpul punya nilai data, pointer child kiri, 
dan pointer child kanan.

bagian kedua adalah traversal preorder yang menelusuri BST dengan pola root dulu, lalu 
subtree kiri, lalu subtree kanan secara rekursif. fungsi ini dipakai untuk melihat isi 
BST sebelum dan sesudah rotasi.

bagian ketiga adalah fungsi tampil_struktur yang menampilkan bentuk visual BST. fungsi 
ini mencetak setiap node dengan indentasi berdasarkan kedalamannya, lalu rekursi ke 
child kiri (L) dan child kanan (R).

bagian keempat adalah fungsi rotate_left yang jadi inti dari latihan ini. cara kerjanya, 
y diambil dari child kanan x, lalu subtree kiri milik y disimpan sementara di T2. setelah 
itu x turun menjadi child kiri y, dan T2 dipasang sebagai child kanan x. hasilnya y naik 
menjadi root baru.

di program utama, BST dibuat secara manual dengan data 10, 20, 30 yang condong ke kanan. 
setelah rotate_left dipanggil, struktur BST berubah, 20 naik menjadi root baru dengan 10 
sebagai child kiri dan 30 sebagai child kanan, sehingga BST menjadi lebih seimbang.
'''