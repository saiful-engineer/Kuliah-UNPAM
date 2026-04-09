class Siswa:
    def __init__(self, nama, kelas, nilai):
        self.nama = nama
        self.kelas = kelas
        self.nilai = nilai

    def __str__(self):
        return f"Nama: {self.nama}, Kelas: {self.kelas}, Nilai: {self.nilai}"

    @staticmethod
    def tambah_siswa(daftar_siswa, nama, kelas, nilai):
        """Menambahkan objek siswa baru ke dalam list."""
        siswa_baru = Siswa(nama, kelas, nilai)
        daftar_siswa.append(siswa_baru)
        print(f"Siswa '{nama}' berhasil ditambahkan.")

    @staticmethod
    def tampilkan_siswa(daftar_siswa):
        """Menampilkan semua siswa dalam list."""
        if not daftar_siswa:
            print("Daftar siswa kosong.")
        else:
            print("--- Daftar Siswa ---")
            for i, siswa in enumerate(daftar_siswa, start=1):
                print(f"{i}. {siswa}")

    @staticmethod
    def cari_siswa(daftar_siswa, nama_dicari):
        """Mencari siswa berdasarkan nama dan menampilkan informasinya."""
        print(f"--- Hasil pencarian untuk '{nama_dicari}' ---")
        ditemukan = False
        for siswa in daftar_siswa:
            if siswa.nama.lower() == nama_dicari.lower():
                print(siswa)
                ditemukan = True
                break
        if not ditemukan:
            print(f"Siswa dengan nama '{nama_dicari}' tidak ditemukan.")


# Contoh penggunaan
daftar_siswa = []
Siswa.tambah_siswa(daftar_siswa, "Andi", "10A", 90)
Siswa.tambah_siswa(daftar_siswa, "Budi", "11B", 85)
Siswa.tambah_siswa(daftar_siswa, "Gigi", "10A", 92)

print("\n")
Siswa.tampilkan_siswa(daftar_siswa)

print("\n")
Siswa.cari_siswa(daftar_siswa, "Budi")
Siswa.cari_siswa(daftar_siswa, "Gigi")
Siswa.cari_siswa(daftar_siswa, "Caca")