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
        """Menghapus dan mengembalikan elemen dari depan (front). O(1)."""
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

class PriorityQueue(Queue):
    """Queue yang mendukung penambahan elemen di depan jika prioritas True."""
    def enqueue_priority(self, item, priority=False):
        new_node = Node(item)
        if priority:
            # Jika Prioritas TINGGI (masuk ke depan/front)
            if self.is_empty():
                self.front = new_node
                self.rear = new_node
            else:
                new_node.next = self.front
                self.front = new_node
            print(f"'{item}' ditambahkan ke DEPAN (Prioritas Tinggi).")
        else:
            # Jika Prioritas RENDAH (masuk ke belakang/rear) - Logika Enqueue biasa
            if self.is_empty():
                self.front = new_node
                self.rear = new_node
            else:
                self.rear.next = new_node
                self.rear = new_node
            print(f"'{item}' ditambahkan ke BELAKANG (Prioritas Rendah).")
        self.size += 1

if __name__ == "__main__":
    pq = PriorityQueue()
    pq.enqueue_priority("Tugas Biasa 1", False)
    pq.enqueue_priority("Tugas Mendesak 1", True)
    pq.enqueue_priority("Tugas Biasa 2", False)
    pq.enqueue_priority("Tugas Mendesak 2", True)
    print("Hasil Antrian: " + pq.display())