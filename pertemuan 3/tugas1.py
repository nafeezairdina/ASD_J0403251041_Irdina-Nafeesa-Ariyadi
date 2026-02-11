#=================================================#
# pertemuan 3: Linked List                        #
# latihan 1: menghapus node dengan nilai tertentu #
#=================================================#
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def delete_node(self, key):
        temp = self.head
    
    # jika head adalah node yang ingin dihapus
        if temp and temp.data == key:
            self.head = temp.next #head pindah ke elemen kedua
            temp= None #menghapus referensi lama
            return
    
    
    # cari node yang mau dihapus dan simpan node sebelumnya
        prev = None
        while temp and temp.data != key :
            prev = temp # simpan node sekarang sebagai "sebelumnya"
            temp = temp.next # maju ke node berikutnya
    
    
    # jika data tidak ditemukan sampai akhir list
        if temp is None:
            return    #fungsi langsung berhenti 
    
    # lepaskan node dari list dengan menghubungkan prev ke temp.next
        prev.next = temp.next
        temp = None

#============================================================#
# pertemuan 3: Linked List                                   #
# latihan 3: pencarian pada node tertentu double linked list #
#============================================================#
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None #simpan node terakhir untuk traversing mundur
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def search(self, key):
        if not self.head:
            print("doubly linked list kosong, tidak ada elemen yang bisa dicari")
            return False
        
        temp = self.head
        while temp:
            if temp.data == key:
                print(f"elemen {key} ditemukan dalam doubly linked list")
                return True
            temp = temp.next
        print(f"elemen {key} tidak ditemukan dalam doubly linked list")
        return False
    
# contoh tampilan 1:
# masukkan elemen ke dalam doubly linked list: 2, 6,9, 14, 20
# masukkan elemen yang ingin dicari: 9
# elemen 9 ditemukan dalam doubly linked list
dll = DoublyLinkedList()
for x in [2, 6, 9, 14, 20]:
    dll.insert_at_end(x)

dll.search(9)

#===============================================================================================================#
# pertemuan 3: Linked List                                                                                      #
# latihan 5: tambahkan metode untuk membalik (reverse) sebuah single linked list tanpa membuat linked list baru #
#===============================================================================================================#

class Node:  
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # menambahkan elemen ke akhir linked list 
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:  
            temp = temp.next
        temp.next = new_node

    # menampilkan linked list
    def display(self):  
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    # membalik (reverse) linked list tanpa membuat linked list baru
    def reverse(self):
        prev = None  
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # membuat linked list dari input string
    def create_from_input(self, input_str):
        elements = input_str.split(", ")
        for elem in elements:  
            self.insert_at_end(int(elem.strip()))  

def main():  
    linked_list = LinkedList()
    input_str = input("masukkan elemen untuk Linked List: ")  
    linked_list.create_from_input(input_str)
    print("linked List sebelum dibalik: ", end="")
    linked_list.display() 
    linked_list.reverse()
    print("linked List setelah dibalik: ", end="")
    linked_list.display()

if __name__ == "__main__":  
    main()