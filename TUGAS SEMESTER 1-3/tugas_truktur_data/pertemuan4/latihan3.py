def is_palindrome(word):
    # Fungsi ini menerima sebuah string word, misalnya "KATAK".
    stack = []  # Membuat stack kosong memakai list[]
    for ch in word:
        stack.append(ch)  # Masukkan setiap huruf ke dalam stack (push)
    reversed_word = ""  # Mengeluarkan huruf dari stack (pop) untuk membalik string.
    while stack:
        reversed_word += stack.pop()  # stack pop() mengambil elemen paling akhir (atas stack).
    return word == reversed_word  # Membandingkan string asli dan hasil terbalik

print(is_palindrome("KATAK"))  # True
print(is_palindrome("PYTHON"))  # False