def _init_ (self,nama,kelas, nilaclass siswa):
def _init_  (self, nama, kelas, nilai):
    """
    inisialisasi objek siswa.
    """
    self.nama = nama
    self.kelas = kelas
    self.nilai = nilai

def tampilkan_info(self):
    """
    menampiklkan informasi lengkap tentang siswa.
    """
    print(f"nama: {self.nama}")
    print(f"kelas: {self.kelas}")
    print(f"nilai: {self.nilai}")

#subkelas siswa ti yang mewarisi dari kelas siswa
class siswaIT(siswa):
i, (program_studi):
"""
inisialisasi objek siswaIT.
meningkatkan atribut program_pstudi
"""
#memanggil konstruktor daari kelas induk(siswa)
super(). _init_ (nama,kelas,nilai)
self.program_studi = program_studi

def tampilkan_info(self):
    """
    menimpa (overide) metode tampilkan_info() dari kelas induk
    untuk menampilkan informasi tambahan.
    """

    #memanggilkan metode dari kelas induk untuk menampilkan info dasar
    super().tampilkan_info()
    print (f"program studi : {self.program_studi}")

#contoh penggunaan nama siswa IT
    siswa_it = siswaIT ("rizki", "12c", 95, "teknik informatika")

#memanggil metode tampilkan_info () dari subkelas
    print("info siswa IT : ")
    siswa_it.tampilkan_info()