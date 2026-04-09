import os

# --- 1. Buat, Tulis, dan Cek Berkas data_mahasiswa.txt ---
def kelola_data_mahasiswa():
    nama_file = "data_mahasiswa.txt"
    daftar_nama = ["Budi Santoso", "Siti Aisyah", "Rudi Hartono"]

    # a. Membuka/Membuat File (Mode 'w' akan membuat jika tidak ada, atau menimpa jika ada)
    # Gunakan 'w+' jika ingin memastikan berkas ada lalu menulis, tapi 'w' sudah cukup untuk menulis.
    try:
        with open(nama_file, 'w') as file:
            # c. Tulis tiga nama mahasiswa ke dalam file
            print(f"\n--- Menulis ke {nama_file} ---")
            for nama in daftar_nama:
                file.write(nama + "\n")
            print(f"Berhasil menulis {len(daftar_nama)} nama.")
    except Exception as e:
        print(f"Gagal menulis ke file: {e}")

    # --- 2. Membaca isi data_mahasiswa.txt ---
    try:
        with open(nama_file, 'r') as file:
            print(f"\n--- Membaca dan Menampilkan {nama_file} ---")
            isi_file = file.readlines()
            
            # Tampilkan setiap nama dengan nomor urut
            print("Daftar Mahasiswa:")
            for i, baris in enumerate(isi_file):
                # Menghilangkan karakter newline (\n) di akhir baris
                print(f"{i+1}. {baris.strip()}")
    except FileNotFoundError:
        print(f"Kesalahan: Berkas {nama_file} tidak ditemukan saat mencoba membaca.")
    except Exception as e:
        print(f"Gagal membaca file: {e}")

kelola_data_mahasiswa()