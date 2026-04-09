def buat_segitiga_berjarak(tinggi):
    """Membuat pola segitiga angka simetris dengan spasi."""
    for i in range(1, tinggi + 1):
        spasi = " " * (tinggi - i)

        kiri = ""
        for j in range(i, 0, -1):
            kiri += str(j)

        kanan = ""
        for k in range(2, i + 1):
            kanan += str(k)
        print(spasi + kiri + kanan)

try:
    tinggi_segitiga = int(input("Masukkan tinggi Segitiga: "))
    if tinggi_segitiga <= 0:
        print("Tinggi Segitiga harus bilangan positif.")
    else:
        buat_segitiga_berjarak(tinggi_segitiga)
except ValueError:
    print("Input yang Anda masukkan bukan bilangan bulat.")