# Praktikum 2: Eksperimen dengan Shared Reference, Shallow Copy, dan Deep Copy

# Mengimpor modul copy untuk deep copy
import copy

# 1. Contoh Shared Reference (Referensi Bersama)
print("--- Contoh 1: Shared Reference ---")
list_asli_1 = [1, 2, [3, 4]]
list_referensi = list_asli_1  # list_referensi menunjuk ke objek yang sama dengan list_asli_1

print(f"List asli sebelum diubah: {list_asli_1} (id: {id(list_asli_1)})")
print(f"List referensi sebelum diubah: {list_referensi} (id: {id(list_referensi)})")

# Mengubah elemen pada list referensi
list_referensi[2][0] = 99 

print(f"List asli setelah diubah: {list_asli_1} (id: {id(list_asli_1)})")
print(f"List referensi setelah diubah: {list_referensi} (id: {id(list_referensi)})")
print("Kesimpulan: Perubahan pada satu list akan mempengaruhi yang lain karena mereka berbagi memori yang sama.")

# 2. Contoh Shallow Copy (menggunakan .copy() dan slicing)
print("\n--- Contoh 2: Shallow Copy ---")
list_asli_2 = [10, 20, [30, 40]]
list_shallow_1 = list_asli_2.copy() # Membuat shallow copy (salinan satu tingkat)
list_shallow_2 = list_asli_2[:] # Metode lain untuk shallow copy

print(f"List asli sebelum diubah: {list_asli_2} (id: {id(list_asli_2)})")
print(f"Shallow copy 1 (copy()): {list_shallow_1} (id: {id(list_shallow_1)})")
print(f"Shallow copy 2 (slicing): {list_shallow_2} (id: {id(list_shallow_2)})")

# Mengubah elemen di dalam list bersarang (akan mempengaruhi list asli)
list_shallow_1[2][0] = 88

print(f"List asli setelah diubah: {list_asli_2} (id: {id(list_asli_2)})")
print(f"Shallow copy 1 setelah diubah: {list_shallow_1} (id: {id(list_shallow_1)})")
print("Kesimpulan: Shallow copy membuat salinan dari list terluar, tetapi elemen bersarang masih berbagi referensi.")

# 3. Contoh Deep Copy
print("\n--- Contoh 3: Deep Copy ---")
list_asli_3 = [100, 200, [300, 400]]
list_deep = copy.deepcopy(list_asli_3) # Membuat deep copy (salinan total)

print(f"List asli sebelum diubah: {list_asli_3} (id: {id(list_asli_3)})")
print(f"List deep copy sebelum diubah: {list_deep} (id: {id(list_deep)})")

# Mengubah elemen pada list deep copy
list_deep[2][0] = 777

print(f"List asli setelah diubah: {list_asli_3} (id: {id(list_asli_3)})")
print(f"List deep copy setelah diubah: {list_deep} (id: {id(list_deep)})")
print("Kesimpulan: Deep copy membuat salinan independen dari seluruh struktur data, termasuk elemen bersarang.")
