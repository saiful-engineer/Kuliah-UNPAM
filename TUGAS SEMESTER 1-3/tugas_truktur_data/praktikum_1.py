# Praktikum 1: Program Manajemen Daftar Belanja Sederhana

# Modul sys digunakan untuk keluar dari program
import sys

# Menginisialisasi sebuah list (array dalam Python) untuk menyimpan daftar belanja
daftar_belanja = []

def tampilkan_menu():
    """Fungsi untuk menampilkan opsi menu kepada pengguna."""
    print("\n--- Menu Daftar Belanja ---")
    print("1. Tambah item")
    print("2. Hapus item")
    print("3. Ubah item")
    print("4. Tampilkan daftar")
    print("5. Keluar")

def tambah_item():
    """Fungsi untuk menambahkan item ke daftar belanja."""
    item_baru = input("Masukkan nama item yang ingin ditambahkan: ")
    if item_baru: # Memastikan input tidak kosong
        daftar_belanja.append(item_baru)
        print(f"'{item_baru}' telah ditambahkan ke daftar.")
    else:
        print("Nama item tidak boleh kosong.")

def hapus_item():
    """Fungsi untuk menghapus item dari daftar belanja."""
    if not daftar_belanja:
        print("Daftar belanja masih kosong, tidak ada item untuk dihapus.")
        return
    
    tampilkan_daftar()
    try:
        indeks = int(input("Masukkan nomor item yang ingin dihapus: ")) - 1
        if 0 <= indeks < len(daftar_belanja):
            item_dihapus = daftar_belanja.pop(indeks)
            print(f"'{item_dihapus}' telah dihapus dari daftar.")
        else:
            print("Nomor item tidak valid. Harap masukkan nomor yang sesuai.")
    except ValueError:
        print("Input tidak valid. Harap masukkan nomor.")

def ubah_item():
    """Fungsi untuk mengubah nama item yang sudah ada."""
    if not daftar_belanja:
        print("Daftar belanja masih kosong, tidak ada item untuk diubah.")
        return
    
    tampilkan_daftar()
    try:
        indeks = int(input("Masukkan nomor item yang ingin diubah: ")) - 1
        if 0 <= indeks < len(daftar_belanja):
            item_lama = daftar_belanja[indeks]
            item_baru = input(f"Masukkan nama baru untuk '{item_lama}': ")
            if item_baru:
                daftar_belanja[indeks] = item_baru
                print(f"'{item_lama}' telah diubah menjadi '{item_baru}'.")
            else:
                print("Nama item tidak boleh kosong.")
        else:
            print("Nomor item tidak valid. Harap masukkan nomor yang sesuai.")
    except ValueError:
        print("Input tidak valid. Harap masukkan nomor.")

def tampilkan_daftar():
    """Fungsi untuk menampilkan semua item di daftar belanja."""
    if not daftar_belanja:
        print("Daftar belanja masih kosong.")
    else:
        print("\n--- Daftar Belanja Anda ---")
        for i, item in enumerate(daftar_belanja, 1):
            print(f"{i}. {item}")

def main():
    """Fungsi utama program."""
    while True:
        tampilkan_menu()
        pilihan = input("Masukkan pilihan Anda (1-5): ")

        if pilihan == '1':
            tambah_item()
        elif pilihan == '2':
            hapus_item()
        elif pilihan == '3':
            ubah_item()
        elif pilihan == '4':
            tampilkan_daftar()
        elif pilihan == '5':
            print("Terima kasih, program selesai.")
            sys.exit()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Jalankan fungsi utama
if __name__ == "__main__":
    main()
