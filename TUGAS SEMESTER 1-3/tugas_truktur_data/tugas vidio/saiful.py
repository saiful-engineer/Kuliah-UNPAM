class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

class DataMahasiswa:
    def __init__(self):
        self.mahasiswa = []

    def tambah_mahasiswa(self, nama, nim, jurusan):
        self.mahasiswa.append(Mahasiswa(nama, nim, jurusan))

    def hapus_mahasiswa(self, nim):
        for mhs in self.mahasiswa:
            if mhs.nim == nim:
                self.mahasiswa.remove(mhs)
                return

    def tampilkan_mahasiswa(self):
        for mhs in self.mahasiswa:
            print(f"Nama: {mhs.nama}, NIM: {mhs.nim}, Jurusan: {mhs.jurusan}")

data_mahasiswa = DataMahasiswa()

while True:
    print("1. Tambah Mahasiswa")
    print("2. Hapus Mahasiswa")
    print("3. Tampilkan Mahasiswa")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama = input("Masukkan nama: ")
        nim = input("Masukkan NIM: ")
        jurusan = input("Masukkan jurusan: ")
        data_mahasiswa.tambah_mahasiswa(nama, nim, jurusan)
    elif pilihan == "2":
        nim = input("Masukkan NIM mahasiswa yang ingin dihapus: ")
        data_mahasiswa.hapus_mahasiswa(nim)
    elif pilihan == "3":
        data_mahasiswa.tampilkan_mahasiswa()
    elif pilihan == "4":
        break
    else:
        print("Pilihan tidak valid")