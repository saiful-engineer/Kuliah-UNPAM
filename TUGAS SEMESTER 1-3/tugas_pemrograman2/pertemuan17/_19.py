
def binary_search(arr, target): 
    """Melakukan pencarian biner terhadap elemen target 
dalam list yang terurut. 
     
    Mengembalikan indeks elemen jika ditemukan, -1 jika 
tidak ditemukan. 
    """ 
    low = 0 
    high = len(arr) - 1 
 
    while low <= high: 
        mid = (low + high) // 2  # Mencari indeks tengah 
        if arr[mid] == target: 
            return mid  # Ditemukan 
        elif arr[mid] < target: 
            low = mid + 1  # Pencarian di bagian kanan 
        else: high = mid - 1  # Pencarian di bagian kiri 
 
    return -1  # Tidak ditemukan 

arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23

result = binary_search(arr, target)
if result != -1:
    print(f"Elemen {target} ditemukan di indeks {result}")
else:
    print(f"Elemen {target} tidak di temukan:")