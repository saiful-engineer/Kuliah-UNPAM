from collections import deque

class AntrianPelanggan:
    def _init_(self):
        self.vip = deque()
        self.biasa = deque()

    def tambah_vip(self, nama):
        self.vip.appendleft(nama)
        print(f"Pelanggan VIP {nama} telah ditambahkan ke antrian.")

    def tambah_biasa(self, nama):
        self.biasa.append(nama)
        print(f"Pelanggan biasa {nama} telah ditambahkan ke antrian.")

    def layani_pelanggan(self):
        if self.vip:
            nama = self.vip.popleft()
            print(f"Pelanggan VIP {nama} telah dilayani.")
        elif self.biasa:
            nama = self.biasa.popleft()
            print(f"Pelanggan biasa {nama} telah dilayani.")
        else:
            print("Antrian kosong.")

    def tampilkan_antrian(self):
        antrian = list(self.vip) + list(self.biasa)
        print(f"Antrian saat ini: {antrian}")

# Buat objek antrian
antrian = AntrianPelanggan()

# Tambah pelanggan VIP dan biasa
antrian.tambah_vip("Rina")
antrian.tambah_biasa("Dodi")
antrian.tambah_vip("Sinta")

# Layani satu pelanggan
antrian.layani_pelanggan()

# Tampilkan antrian saat ini
antrian.tampilkan_antrian()