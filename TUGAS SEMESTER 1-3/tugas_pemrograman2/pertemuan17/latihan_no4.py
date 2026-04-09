#mencari huruf kapital dan memiliki min 3 karakter
import re

def cari_kata_khusus(teks):
    """
    Fungsi Mencari kata yang di awali huruf Kapital dan panjang minimal 3
    """

#pola: mulai dengan kapital(a-z) diikuti 2 atau lebih kata (\w{2,})
    pola_regex = r"\b[A-Z]\w{2,}\b"

    hasil = re.findall(pola_regex,teks)
    return hasil, pola_regex


#---conoth penggunaan---
contoh_teks = "Hari ini, Saya pergi ke bandung. Kata 'A', 'Di', dan'Ah'(2 huruf) tidak termasuk"

kata_ditemukan, pola = cari_kata_khusus(contoh_teks)

print("\n---Hasil soal 4 ---")
print(f"teks input:{contoh_teks}")
print(f"pola REGEX ({pola}):{kata_ditemukan}")

