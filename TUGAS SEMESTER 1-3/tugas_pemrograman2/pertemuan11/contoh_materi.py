
def insertion_sort_descending(arr): 
    """ 
    Mengurutkan sebuah list (array) menggunakan algoritma Insertion Sort secara descending (dari besar ke kecil). 

    Args: 
    arr: List angka yang akan diurutkan. 

    Returns: 
    List yang sudah terurut secara descending. 
    """ 
    n = len(arr) 
    # Mulai dari elemen kedua, karena elemen pertama dianggap sudah terurut 
    for i in range(1, n): 
        key = arr[i] # Elemen yang akan disisipkan 
        j = i - 1 # Indeks elemen terakhir dari sub-array yang terurut 
        print(f"\n--- Iterasi ke-{i} ---") 
        print(f"Array sebelum proses: {arr}") 
        print(f"Elemen yang akan disisipkan (key): {key}") 
        print(f"Membandingkan {key} dengan elemen di sebelah kirinya (untuk descending)...") 
        # Pindahkan elemen-elemen dari arr[0..i-1], yang lebih kecil dari key, 
        # ke satu posisi di depan posisi mereka saat ini 
        # Kunci di sini adalah 'key > arr[j]' untuk descending 
        while j >= 0 and key > arr[j]: 
            print(f" {key} > {arr[j]}, geser {arr[j]} ke kanan.") 
            arr[j + 1] = arr[j] # Geser elemen ke kanan 
            j -= 1 
        print(f" Array sementara: {arr}") 
        arr[j + 1] = key # Sisipkan key pada posisi yang benar 
        print(f"Sisipkan {key} pada posisi yang benar.") 
        print(f"Array setelah iterasi ke-{i}: {arr}") 
    return arr 

# --- Contoh Penggunaan --- 
data = [4, 7, 3, 9] 
print(f"Data Awal: {data}") 
# Panggil fungsi insertion_sort_descending 
data_terurut_desc = insertion_sort_descending(data) 
print(f"\n--- Proses Selesai ---") 
print(f"Data Terurut (Descending): {data_terurut_desc}") 

# Contoh lain 
print("\n--- Contoh Lain ---") 
data2 = [12, 11, 13, 5, 6] 
print(f"Data Awal: {data2}") 
data2_terurut_desc = insertion_sort_descending(data2) 
print(f"\nData Terurut (Descending): {data2_terurut_desc}")