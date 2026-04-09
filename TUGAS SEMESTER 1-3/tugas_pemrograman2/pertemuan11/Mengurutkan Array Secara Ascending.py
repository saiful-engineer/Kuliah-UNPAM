def insertion_sort_ascending(arr):
    """
    Mengurutkan list menggunakan Insertion Sort secara ascending.
    
    Args:
        arr: List angka yang akan diurutkan.
    
    Returns:
        List yang sudah terurut secara ascending.
    """
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]  # Elemen yang akan disisipkan
        j = i - 1
        
        # Geser elemen yang lebih besar dari key
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
        print(f"Iterasi {i}: {arr}")  # Menampilkan hasil setiap iterasi
    
    return arr

# --- Contoh Penggunaan ---
data_asc = [8, 2, 5, 1, 6]
print("=== Insertion Sort Ascending ===")
print(f"Data Awal: {data_asc}")
data_asc_sorted = insertion_sort_ascending(data_asc)
print(f"Data Terurut (Ascending): {data_asc_sorted}")
