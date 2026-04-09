from typing import List, Any

def linear_search(arr: List[Any], target: Any) -> int:
    # ... (Definisi fungsi linear_search) ...
    pass 

def cetak_hasil_uji(data_list: List[Any], target_value: Any, posisi: str):
    # ... (Definisi fungsi cetak_hasil_uji) ...
    pass

# --- KODE EKSEKUSI UTAMA DIMULAI DI SINI (TANPA INDENTASI) ---

# Studi Kasus: Uji coba mencari angka di awal, tengah, akhir, dan tidak ada.
data_angka: List[int] = [17, 22, 24, 15, 40, 52, 61, 64] 

# Penentuan Nilai Uji Coba
target_awal = data_angka[0]
target_akhir = data_angka[-1]
target_tengah = data_angka[len(data_angka) // 2]
target_tidak_ada = 100

print("===============================================")
print(" UJI COBA PENCARIAN LINEAR (Linear Search) ")
print("===============================================")
print(f"Data List: {data_angka}\n")

# 1. Mencari di Awal
cetak_hasil_uji(data_angka, target_awal, "Awal")

# 2. Mencari di Tengah
cetak_hasil_uji(data_angka, target_tengah, "Tengah")

# 3. Mencari di Akhir
cetak_hasil_uji(data_angka, target_akhir, "Akhir")

# 4. Mencari yang Tidak Ada
cetak_hasil_uji(data_angka, target_tidak_ada, "Tidak Ditemukan")

print("\n===============================================")