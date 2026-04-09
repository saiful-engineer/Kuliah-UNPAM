import csv # Untuk mengilustrasikan File I/O lebih lanjut

# --- 1. KONSEP OOP (BAB 4 & 5) ---
class Siswa:
    """Kelas untuk merepresentasikan data siswa."""
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    def cek_kelulusan(self):
        # Struktur Pemilihan (Selection - Bab 1)
        if self.nilai >= 70:
            return "LULUS"
        else:
            return "TIDAK LULUS"
    
    def tampilkan_info(self):
        # Menggunakan format string untuk output
        return f"Nama: {self.nama}, Nilai: {self.nilai}, Status: {self.cek_kelulusan()}"

# --- 2. MANAJEMEN LIST DAN FUNGSI (BAB 2) ---
# List global untuk menyimpan objek siswa
daftar_siswa = []

def tambah_siswa(nama, nilai):
    """Menambahkan objek Siswa ke dalam list."""
    siswa_baru = Siswa(nama, nilai)
    daftar_siswa.append(siswa_baru)

def hitung_rata_rata(list_siswa):
    """Menghitung rata-rata nilai, menangani list kosong."""
    if not list_siswa:
        return 0
    # Menggunakan list comprehension untuk mendapatkan semua nilai
    total_nilai = sum(siswa.nilai for siswa in list_siswa)
    return total_nilai / len(list_siswa)

# --- 3. PENGURUTAN (BAB 11) ---
def urutkan_siswa_nilai_insertion(arr):
    """Mengurutkan siswa berdasarkan nilai (Descending) menggunakan Insertion Sort."""
    n = len(arr)
    # Looping menggunakan Struktur Perulangan (Iteration - Bab 1)
    for i in range(1, n):
        key = arr[i] # Siswa yang akan disisipkan
        j = i - 1
        
        # Bandingkan dan geser elemen yang lebih kecil ke kanan
        while j >= 0 and key.nilai > arr[j].nilai: # key.nilai > arr[j].nilai untuk descending
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# --- 4. AKSES FILE I/O (BAB 3) ---
def simpan_data_ke_file(list_siswa, nama_file="data_siswa.txt"):
    """Menulis data siswa ke file teks."""
    try:
        # Menggunakan 'w' (write) untuk menulis dari awal 
        with open(nama_file, 'w') as file:
            file.write("LAPORAN DATA NILAI SISWA\n")
            file.write("--------------------------\n")
            # Iterasi menggunakan Struktur Perulangan (Iteration - Bab 1)
            for siswa in list_siswa:
                # Menulis ke file (File I/O)
                file.write(f"{siswa.nama}; {siswa.nilai}; {siswa.cek_kelulusan()}\n")
        print(f"\nData berhasil disimpan ke {nama_file}")
    except Exception as e: # Konsep Exception Handling (Bab 15, meskipun tidak lengkap, ini praktik yang baik)
        print(f"Terjadi error saat menulis file: {e}")


# --- EKSEKUSI PROGRAM UTAMA ---
if __name__ == "__main__":
    # Menambahkan data awal
    tambah_siswa("Budi", 85)
    tambah_siswa("Sari", 68)
    tambah_siswa("Andi", 92)
    tambah_siswa("Rina", 70)
    
    print("--- DATA AWAL SISWA ---")
    for siswa in daftar_siswa:
        print(siswa.tampilkan_info())
        
    # Hitung dan tampilkan rata-rata
    rata_rata = hitung_rata_rata(daftar_siswa)
    print(f"\nRata-rata Nilai Semua Siswa: {rata_rata:.2f}")

    # Urutkan dan tampilkan
    data_terurut = urutkan_siswa_nilai_insertion(daftar_siswa)
    print("\n--- DATA SISWA TERURUT (NILAI TERTINGGI) ---")
    for siswa in data_terurut:
        print(siswa.tampilkan_info())
        
    # Simpan ke file
    simpan_data_ke_file(data_terurut)