# Membuat class Node
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Membuat class Doubly Linked List
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Fungsi menambah data di depan
    def tambah_depan(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Fungsi menambah data di belakang
    def tambah_belakang(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    # Fungsi menghapus node di depan
    def hapus_depan(self):
        if self.head is None:
            print("List kosong, tidak ada yang bisa dihapus.")
        else:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None

    # Fungsi menghapus node di belakang
    def hapus_belakang(self):
        if self.head is None:
            print("List kosong, tidak ada yang bisa dihapus.")
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            if temp.prev is not None:
                temp.prev.next = None
            else:
                self.head = None

    # Menampilkan isi linked list
    def tampil(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

# --- Program utama ---
print("\n------------------------------------------")
print("          Doubly Linked List             ")
print("------------------------------------------")

print("\nDoubly Linked List dengan tambah depan:")
dll = DoublyLinkedList()
print("Data awal:")
dll.tampil()
dll.tambah_depan("30")
dll.tambah_depan("20")
dll.tambah_depan("10")
print("Isi Doubly Linked List setelah tambah depan:")
dll.tampil()

print("\n------------------------------------------")

print("\nDoubly Linked List dengan tambah belakang:")
dll2 = DoublyLinkedList()
print("Data awal:")
dll2.tampil()
dll2.tambah_belakang("10")
dll2.tambah_belakang("20")
dll2.tambah_belakang("30")
dll2.tambah_belakang("40")
print("Isi Doubly Linked List setelah tambah belakang:")
dll2.tampil()

print("\nMenghapus node di depan...")
dll2.hapus_depan()
print("Isi Doubly Linked List setelah hapus depan:")
dll2.tampil()

print("\nMenghapus node di belakang...")
dll2.hapus_belakang()
print("Isi Doubly Linked List setelah hapus belakang:")
dll2.tampil()

print("\n==========================================")
