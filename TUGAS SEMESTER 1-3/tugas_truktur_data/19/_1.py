def linear_search(arr, target):
    for i in (len(arr)):
        if arr[i]==target:
            return i
        return -1
    

#input data
data = list(map(int,input("masukkan angka (pisahkan dengan spasi):").split()))
target = int(input("cari angka:"))

#pemanggilan fungsi
pos = linear_search(data, target)

if pos != -1:
    print(f"Elemen ditemukan pada indeks{pos}")
else :
    print("Elemen tidak di temukan")