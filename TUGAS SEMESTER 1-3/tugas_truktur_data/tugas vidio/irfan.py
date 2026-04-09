class CircularQueue:
    def __init__(self, kapasitas):  # ✅ dua underscore di depan & belakang
        self.kapasitas = kapasitas
        self.tempat_parkir = [None] * kapasitas
        self.depan = 0
        self.belakang = 0
        self.ukuran = 0

    def isFull(self):
        return self.ukuran == self.kapasitas

    def isEmpty(self):
        return self.ukuran == 0

    def masuk(self, mobil):
        if self.isFull():
            print("Tempat parkir penuh. Mobil tidak dapat masuk.")
            return
        self.tempat_parkir[self.belakang] = mobil
        self.belakang = (self.belakang + 1) % self.kapasitas
        self.ukuran += 1
        print(f"Mobil {mobil} masuk ke tempat parkir.")

    def keluar(self):
        if self.isEmpty():
            print("Tempat parkir kosong. Tidak ada mobil yang dapat keluar.")
            return
        mobil = self.tempat_parkir[self.depan]
        self.tempat_parkir[self.depan] = None
        self.depan = (self.depan + 1) % self.kapasitas
        self.ukuran -= 1
        print(f"Mobil {mobil} keluar dari tempat parkir.")

    def tampilkan(self):
        if self.isEmpty():
            print("Tempat parkir kosong.")
            return
        print("Daftar mobil di tempat parkir:")
        indeks = self.depan
        for _ in range(self.ukuran):
            print(self.tempat_parkir[indeks])
            indeks = (indeks + 1) % self.kapasitas


# ✅ Membuat objek CircularQueue dengan kapasitas 5
tempat_parkir = CircularQueue(5)

while True:
    print("\nMenu:")
    print("1. Masuk ke tempat parkir")
    print("2. Keluar dari tempat parkir")
    print("3. Tampilkan daftar mobil")
    print("4. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        mobil = input("Masukkan plat nomor mobil: ")
        tempat_parkir.masuk(mobil)
    elif pilihan == "2":
        tempat_parkir.keluar()
    elif pilihan == "3":
        tempat_parkir.tampilkan()
    elif pilihan == "4":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid.")
