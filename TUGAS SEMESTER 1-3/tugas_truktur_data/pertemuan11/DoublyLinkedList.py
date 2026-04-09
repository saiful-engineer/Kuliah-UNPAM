# Membuat class Node
class Node:
    def __init__(self, data):
        self.data = data  # Menyimpan data node
        self.prev = None  # Pointer ke node sebelumnya
        self.next = None  # Pointer ke node berikutnya

# Membuat class Doubly Linked List
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Saat pertama kali dibuat, DLL masih kosong

    # Fungsi untuk menambah data di depan
    def tambah_depan(self, data):
        new_node = Node(data)  # 1. Buat node baru
        if self.head is None:  # 2. Jika list kosong
            self.head = new_node  # maka node baru jadi head
        else:
            new_node.next = self.head  # 3. Hubungkan node baru ke head lama
            self.head.prev = new_node  # 4. Hubungkan head lama ke node baru
            self.head = new_node  # 5. Update head jadi node baru

    # Menampilkan isi linked list
    def tampil(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    # Mengecek apakah DLL kosong
    def is_empty(self):
        return self.head is None

# --- Program utama ---
dll = DoublyLinkedList()

if dll.is_empty():
    print("Doubly Linked List masih kosong.")
else:
    print("Doubly Linked List sudah memiliki elemen.")

dll.tambah_depan("C")
dll.tambah_depan("B")
dll.tambah_depan("A")

print("Isi Doubly Linked List:")
dll.tampil()

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

    # Fungsi menambah data di belakang
    def tambah_belakang(self, data):
        new_node = Node(data)  # 1. Buat node baru
        if self.head is None:  # 2. Jika list kosong
            self.head = new_node  # node baru jadi head
        else:
            temp = self.head  # 3. Mulai dari head
            while temp.next is not None:  # 4. Bergerak ke node terakhir
                temp = temp.next
            temp.next = new_node  # 5. Hubungkan node terakhir ke node baru
            new_node.prev = temp  # 6. Hubungkan node baru ke node terakhir

    # Menampilkan isi linked list
    def tampil(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

# --- Program utama ---
dll = DoublyLinkedList()
dll.tambah_belakang("A")
dll.tambah_belakang("B")
dll.tambah_belakang("C")
dll.tambah_belakang("D")
dll.tampil()