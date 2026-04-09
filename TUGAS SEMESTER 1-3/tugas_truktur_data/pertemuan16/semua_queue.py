class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" -> " if temp.next else "")
            temp = temp.next
        print()

class PriorityQueue(Queue):
    def enqueue_priority(self, item, priority=False):
        new_node = Node(item)
        if priority:
            new_node.next = self.front
            self.front = new_node
            if self.rear is None:
                self.rear = new_node
        else:
            if self.is_empty():
                self.front = new_node
                self.rear = new_node
            else:
                self.rear.next = new_node
                self.rear = new_node

def reverse_queue(queue_obj):
    stack = []
    temp_queue = Queue()
    temp = queue_obj.front
    while temp:
        stack.append(temp.data)
        temp = temp.next
    while stack:
        temp_queue.enqueue(stack.pop())
    return temp_queue


class PrintJob:
    def __init__(self, job_id, pages):
        self.job_id = job_id
        self.pages = pages

class PrintQueue(Queue):
    def add_job(self, job_id, pages):
        new_node = Node(PrintJob(job_id, pages))
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def process_next_job(self):
        if self.is_empty():
            print("Antrian kosong")
            return
        job = self.front.data
        print(f"Memproses Job ID: {job.job_id}, Halaman: {job.pages}.")
        self.front = self.front.next
        if self.front is None:
            self.rear = None

    def display_jobs(self):
        temp = self.front
        print("Antrian Print:")
        while temp:
            job = temp.data
            print(f"Job ID: {job.job_id}, Halaman: {job.pages}")
            temp = temp.next

def main():
    print("Praktikum 1: Implementasi Prioritas pada Enqueue")
    pq = PriorityQueue()
    pq.enqueue_priority("Tugas Biasa 1", False)
    pq.enqueue_priority("Tugas Mendesak 1", True)
    pq.enqueue_priority("Tugas Biasa 2", False)
    pq.enqueue_priority("Tugas Mendesak 2", True)
    print("Antrian:")
    pq.display()

    print("\nPraktikum 2: Membalik Antrian")
    my_queue = Queue()
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    print("Antrian Asli:")
    my_queue.display()
    reversed_q = reverse_queue(my_queue)
    print("Antrian Terbalik:")
    reversed_q.display()
    print("Antrian Asli (tidak berubah):") 
    my_queue.display (Queue())

    print("\nPraktikum 3: Simulasi Antrian Dokumen Print")
    print_q = PrintQueue()
    print_q.add_job("Laporan Keuangan", 25)
    print_q.add_job("Materi Kuliah", 10)
    print_q.add_job("Tugas Akhir", 50)
    print_q.display_jobs()
    print_q.process_next_job()
    print_q.process_next_job()
    print_q.display_jobs()

if __name__ == "__main__":
    main()