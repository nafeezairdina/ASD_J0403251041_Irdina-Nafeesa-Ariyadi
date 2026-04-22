#==============================#
# Nama: Irdina Nafeesa Ariyadi #
# NIM: J0403251041             #
# Kelas: TPL B1                #
#==============================#

#==========================================#
# latihan 6: rotasi kanan pada BST         #
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
def tampil_struktur(root, level=0, posisi="root"):
    if root is not None:
        # cetak node dengan indentasi sesuai kedalamannya
        print("   " * level + f"{posisi}: {root.data}")
        # rekursi ke child kiri dengan level bertambah
        tampil_struktur(root.left, level + 1, "L")
        # rekursi ke child kanan dengan level bertambah
        tampil_struktur(root.right, level + 1, "R")

# fungsi rotasi kanan untuk menyeimbangkan BST yang condong ke kiri
def rotate_right(x):
    y  = x.left # y adalah child kiri x, akan menjadi root baru
    T2 = y.right # subtree kanan milik y disimpan sementara

    # proses rotasi: x turun menjadi child kanan y
    y.right = x # x menjadi child kanan dari y
    x.left = T2 # child kiri x diganti dengan T2

    return y

#===============#
# program utama #
#===============#
root = Node(30)
root.left = Node(20)
root.left.left = Node(10)

print("preorder sebelum rotasi kanan:")
preorder(root)

print("\n\nstruktur sebelum rotasi kanan:")
tampil_struktur(root)

# melakukan rotasi kanan pada root
root = rotate_right(root)

print("\npreorder sesudah rotasi kanan:")
preorder(root)

print("\n\nstruktur sesudah rotasi kanan:")
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

bagian keempat adalah fungsi rotate_right yang jadi inti dari latihan ini. cara kerjanya, 
y diambil dari child kiri x, lalu subtree kanan milik y disimpan sementara di T2. setelah 
itu x turun menjadi child kanan y, dan T2 dipasang sebagai child kiri x. hasilnya y naik 
menjadi root baru.

di program utama, BST dibuat secara manual dengan data 30, 20, 10 yang condong ke kiri. 
setelah rotate_right dipanggil, struktur BST berubah, 20 naik menjadi root baru dengan 10 
sebagai child kiri dan 30 sebagai child kanan, sehingga BST menjadi lebih seimbang.
'''