import os
# --- 3. Program Python untuk log.txt ---
def kelola_log():
    nama_log = "log.txt"
    
    # a. Mengecek apakah log.txt ada
    if os.path.exists(nama_log):
        # b. Jika ya, tampilkan isinya
        try:
            with open(nama_log, 'r') as file:
                print(f"\n--- Berkas {nama_log} Ditemukan ---")
                print("Isi Log:")
                print(file.read().strip())
        except Exception as e:
            print(f"Gagal membaca log.txt: {e}")
    else:
        # c. Jika tidak, buat file baru dan tulis "Log dimulai"
        try:
            with open(nama_log, 'w') as file:
                file.write("Log dimulai\n")
                print(f"\n--- Berkas {nama_log} Tidak Ditemukan ---")
                print("Berkas baru dibuat dan 'Log dimulai' telah ditulis.")
        except Exception as e:
            print(f"Gagal membuat dan menulis log.txt: {e}")

kelola_log()