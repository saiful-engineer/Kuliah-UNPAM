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

class PrintJob:
    """Kelas untuk merepresentasikan satu pekerjaan cetak."""
    def __init__(self, job_id, pages):
        self.job_id = job_id
        self.pages = pages

    def __str__(self):
        return f"Job ID: {self.job_id}, Halaman: {self.pages}"

class PrintQueue:
    """Simulasi Antrian Cetak menggunakan objek Queue."""
    def __init__(self):
        self.queue = Queue()

    def add_job(self, job_id, pages):
        """Menambahkan PrintJob baru ke antrian."""
        new_job = PrintJob(job_id, pages)
        self.queue.enqueue(new_job)
        print(f"-> Job '{job_id}' ({pages} hlm) ditambahkan.")

    def process_next_job(self):
        """Memproses (Dequeue) PrintJob yang paling depan."""
        processed_job = self.queue.dequeue()
        if processed_job is None:
            print("Antrian cetak kosong. Tidak ada job untuk diproses.")
            return
        print(f"Memproses Job ID: {processed_job.job_id}, Halaman: {processed_job.pages}.")
        return processed_job

    def display_jobs(self):
        """Menampilkan semua job di antrian."""
        if self.queue.is_empty():
            print("Antrian Print kosong.")
            return
        print("\nAntrian Print:")
        current = self.queue.front
        while current:
            # current.data adalah objek PrintJob
            print(f"{current.data}")
            current = current.next

if __name__ == "__main__":
    print_q = PrintQueue()
    print_q.add_job("Laporan Keuangan", 25)
    print_q.add_job("Materi Kuliah", 10)
    print_q.add_job("Tugas Akhir", 50)
    print_q.display_jobs()
    print("\n--- Proses 2 Job Pertama ---")
    print_q.process_next_job()
    print_q.process_next_job()
    print("\n--- Antrian Sisa ---")
    print_q.display_jobs()
    print_q.process_next_job()
    print