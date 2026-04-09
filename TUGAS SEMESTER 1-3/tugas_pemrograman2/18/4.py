import os
import shutil

# --- 4. Program untuk Folder Arsip dan Pemindahan Berkas ---
def arsipkan_berkas():
    nama_folder_arsip = "arsip"
    nama_file_dipindah = "data_mahasiswa.txt"
    
    # a. Membuat folder arsip
    if not os.path.exists(nama_folder_arsip):
        try:
            os.mkdir(nama_folder_arsip)
            print(f"\n--- Operasi Arsip ---")
            print(f"Folder '{nama_folder_arsip}' berhasil dibuat.")
        except Exception as e:
            print(f"Gagal membuat folder: {e}")
            return # Hentikan fungsi jika gagal buat folder
    else:
        print(f"\n--- Operasi Arsip ---")
        print(f"Folder '{nama_folder_arsip}' sudah ada.")

    # b. Memindahkan file data_mahasiswa.txt ke folder tersebut
    sumber = nama_file_dipindah
    tujuan = os.path.join(nama_folder_arsip, nama_file_dipindah)
    
    if os.path.exists(sumber):
        try:
            # shutil.move digunakan untuk memindahkan (rename across filesystems)
            shutil.move(sumber, tujuan)
            print(f"Berkas '{nama_file_dipindah}' berhasil dipindahkan ke folder '{nama_folder_arsip}'.")
        except Exception as e:
            print(f"Gagal memindahkan berkas: {e}")
    else:
        print(f"Berkas '{nama_file_dipindah}' tidak ditemukan untuk dipindahkan.")

arsipkan_berkas()