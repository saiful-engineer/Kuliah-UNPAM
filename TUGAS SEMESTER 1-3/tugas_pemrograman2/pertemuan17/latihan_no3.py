#mencari nomor telepon dan kata mengandung angka(2 pencarian)
import re

#teks input yang kan di uji
data_teks = "Hubungi di 0857-1887-9856. Produk bagus: item_A1. Versi:V2.5. Nomor lain: 0877-1111-2222."

#--bagian 1 : menjari nomor telepon(08xxxxxx)
pola_tel = r"08\d{2}-\d{4}-\d{4}"
nomor_telepon = re.findall(pola_tel,data_teks)

#--bagian2: mancari kata yang mengandung angka
pola_angka = r"\b\w*\d\w*\b"
kata_kerangka = re.findall(pola_angka,data_teks)


print("--- Hasil Soal 3 ---")
print("pola telepon ({pola_tel}):" \
"{nomor_telepon}")
print(f"pola kata berangka ({pola_angka}):{kata_kerangka}")