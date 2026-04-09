class Queue:
    def __init__(self):
        self.antrian = []

    def enqueue(self, pelanggan):
        self.antrian.append(pelanggan)
        print(f"Pelanggan {pelanggan} ditambahkan ke dalam antrian.")

    def dequeue(self):
        if len(self.antrian) == 0:
            print("Antrian kosong.")
            return
        pelanggan = self.antrian.pop(0)
        print(f"Pelanggan {pelanggan} dilayani.")

    def tampilkanAntrian(self):
        if len(self.antrian) == 0:
            print("Antrian kosong.")
            return
        print("Antrian:")
        for i, pelanggan in enumerate(self.antrian):
            print(f"{i+1}. {pelanggan}")

# Membuat objek Queue
antrian = Queue()

while True:
    print("\nMenu:")
    print("1. Tambah pelanggan ke antrian")
    print("2. Panggil pelanggan")
    print("3. Tampilkan antrian")
    print("4. Keluar")
    
    pilihan = input("Pilih menu: ")
    
    if pilihan == "1":
        pelanggan = input("Masukkan nama pelanggan: ")
        antrian.enqueue(pelanggan)
    elif pilihan == "2":
        antrian.dequeue()
    elif pilihan == "3":
        antrian.tampilkanAntrian()
    elif pilihan == "4":
        break
    else:
        print("Pilihan tidak valid.")