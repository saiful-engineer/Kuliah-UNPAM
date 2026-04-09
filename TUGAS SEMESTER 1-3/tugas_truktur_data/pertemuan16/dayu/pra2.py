class Node:
    """Struktur dasar Node untuk Singly Linked List."""
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    """Implementasi Queue menggunakan Singly Linked List."""
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        """Memeriksa apakah Queue kosong."""
        return self.front is None

    def enqueue(self, item):
        """Menambahkan elemen ke belakang (rear). O(1)."""
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        """Menghapus dan mengembalikan elemen dari, depan (front). O(1)."""
        if self.is_empty():
            return None
        dequeued_item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return dequeued_item

    def display(self):
        """Menampilkan semua elemen di Queue."""
        if self.is_empty():
            return "Antrian kosong"
        current = self.front
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        return "Antrian: " + " -> ".join(elements)

def reverse_queue(queue_obj):
    """Membalik urutan Queue menggunakan bantuan Stack."""
    # 1. Gunakan list Python sebagai Stack
    stack = []
    # 2. Pindahkan semua elemen Queue ke Stack (LIFO)
    # Catatan: Kita gunakan dequeue agar stack mendapat elemen dalam urutan FIFO
    temp_queue = Queue()  # Isi temp_queue dengan salinan data asli
    current = queue_obj.front
    while current:
        temp_queue.enqueue(current.data)
        current = current.next
    # Dequeue dari temp_queue dan push ke stack
    while not temp_queue.is_empty():
        item = temp_queue.dequeue()
        stack.append(item)
    # 3. Buat Queue baru yang akan menyimpan elemen terbalik
    reversed_q = Queue()
    # 4. Pop dari Stack dan Enqueue ke Queue baru
    while stack:
        item = stack.pop()
        reversed_q.enqueue(item)
    return reversed_q

if __name__ == "__main__":
    my_queue = Queue()
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    print("Queue Asli (Awal): " + my_queue.display())
    reversed_q = reverse_queue(my_queue)
    print("Queue Hasil Balik: " + reversed_q.display())
    print("Queue Asli (Akhir): " + my_queue.display())  # Memastikan queue asli tidak berubah