def linear_search(arr,target):
    """melakukan pencarian linier pada sebuah list.
    
    args:
    arr (list): List data yang akan di cari.
    target: Nilai yang ingin di cari.
    
    Returns:
    int: Indeks dari target jika di temukan, -1 jika tidak ditemukan."""
    
    for i in range(len(arr)):
        if arr[i] == target:
            return i #mengembalikan indeks jika di temukan return -1 #mengembalikan -1 jika tidak di temukan
        #contoh penggunaan
        data_angka = [15,22,10,30,5,88,7]
        nilai_dicari_1 = 30
        nilai_dicari_2 = 100

        indeks_1 = linear_search(data_angka,nilai_dicari_1)
        indeks_2 = linear_search(data_angka,nilai_dicari_2)

        if indeks_1 != -1:
            print(f"Nilai{nilai_dicari_1} ditemukan pada indeks: {indeks_1}")
        else:
            print(f"Nilai{nilai_dicari_1} tidak di temukan.")
            if indeks_2 != -1:
                print(f"Nilai{nilai_dicari_2} ditemukan pada indeks: {indeks_2}")
            else:
                print(f"Nilai{nilai_dicari_2} tidak di temukan.")
        #contoh lain: mencari string
        daftar_buah = ["apel","keruk","mangga","pisang","anggur"]
        buah_dicari_1 = "mangga"
        buah_dicari_2 = "semangka"

        indeks_buah_1 = linear_search(daftar_buah,buah_dicari_1)
        indeks_buah_2 = linear_search(daftar_buah,buah_dicari_2)

        if indeks_buah_1 !=-1:
            print(f"buah'{buah_dicari_1}' di temukan pada indeks: {indeks_buah_1}")
        else:
            print(f"buah'{buah_dicari_1}' tidak di temukan")

        if indeks_buah_2 !=-1:
            print(f"buah'{buah_dicari_2}' di temukan pada indeks : {indeks_buah_2}")
        else:
            print(f"buah'{buah_dicari_2}' tidak di temukan.")
