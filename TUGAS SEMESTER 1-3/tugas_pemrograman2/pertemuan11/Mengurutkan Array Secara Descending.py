def insertion_sort_descending(arr):
    """
    Mengurutkan list menggunakan Insertion Sort secara descending.
    
    Args:
        arr: List angka yang akan diurutkan.
    
    Returns:
        List yang sudah terurut secara descending.
    """
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]  # Elemen yang akan disisipkan
        j = i - 1
        
        # Geser elemen yang lebih kecil dari key
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
        print(f"Iterasi {i}: {arr}")  # Menampilkan hasil setiap iterasi
    
    return arr

# --- Contoh Penggunaan ---
data_desc = [15, 7, 20, 10, 8]
print("\n=== Insertion Sort Descending ===")
print(f"Data Awal: {data_desc}")
data_desc_sorted = insertion_sort_descending(data_desc)
print(f"Data Terurut (Descending): {data_desc_sorted}")
