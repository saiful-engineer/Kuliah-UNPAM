from typing import List, Any

# Fungsi linear_search yang persis menggunakan logika iterasi manual
def linear_search(arr: List[Any], target: Any) -> int:
    """
    Melakukan pencarian linear secara manual pada sebuah list.
    
    Args:
        arr: List data yang akan dicari.
        target: Nilai yang ingin dicari.
        
    Returns:
        Indeks dari target jika ditemukan, -1 jika tidak ditemukan.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Mengembalikan indeks jika ditemukan
    return -1 # Mengembalikan -1 jika tidak ditemukan

def cetak_hasil_uji(data_list: List[Any], target_value: Any, posisi: str):
    """
    Melakukan pencarian dan mencetak hasilnya sesuai format studi kasus.
    """
    indeks = linear_search(data_list, target_value)
    
    if indeks != -1:
        # Output ditemukan
        print(f" Kasus {posisi}: Nilai {target_value} ditemukan pada indeks: {indeks}")
    else:
        # Output tidak ditemukan
        print(f" Kasus {posisi}: Nilai {target_value} tidak ditemukan.")

# =======================================================
# KODE EKSEKUSI UTAMA (DIPAKSA BERJALAN)
# =======================================================

# Studi Kasus: Uji coba mencari angka di awal, tengah, akhir, dan tidak ada.
data_angka: List[int] = [17, 22,  52, 24, 15, 40, 61, 64]

# Penentuan Nilai Uji Coba
target_awal = data_angka[0]
target_akhir = data_angka[-1]
# Mencari nilai di sekitar indeks tengah (misalnya 40)
target_tengah = data_angka[len(data_angka) // 2] 
target_tidak_ada = 100

print("===============================================")
print(" UJI COBA PENCARIAN LINEAR (Linear Search) ")
print("===============================================")
print(f"List Data: {data_angka}\n")

# 1. Mencari di Awal
cetak_hasil_uji(data_angka, target_awal, "Awal")

# 2. Mencari di Tengah
cetak_hasil_uji(data_angka, target_tengah, "Tengah")

# 3. Mencari di Akhir
cetak_hasil_uji(data_angka, target_akhir, "Akhir")

# 4. Mencari yang Tidak Ada
cetak_hasil_uji(data_angka, target_tidak_ada, "Tidak Ditemukan")

print("\n===============================================")