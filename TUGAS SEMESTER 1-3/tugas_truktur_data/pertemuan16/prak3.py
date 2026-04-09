class PrintJob:
    def __init__(self, job_id, pages):
        self.job_id = job_id
        self.pages = pages

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class PrintQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

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

# Contoh Penggunaan
print_q = PrintQueue()
print_q.add_job("Laporan Keuangan", 25)
print_q.add_job("Materi Kuliah", 10)
print_q.add_job("Tugas Akhir", 50)
print_q.display_jobs()
print_q.process_next_job()
print_q.process_next_job()
print_q.display_jobs()