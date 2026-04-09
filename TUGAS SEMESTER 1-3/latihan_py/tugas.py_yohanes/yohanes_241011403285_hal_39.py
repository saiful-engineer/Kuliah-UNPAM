import time 
mulai=time.time() 
print('ini adalah penggunaan single Quote') 
print("ini contoh penggunaan double Quote") 
#hashtag berfungsi untuk membuat komentar 
""" 
selain menggunakan hashtag 
komentar juga bisa  dibuat dengan tanda triple Quote 
untuk membuat komentar multi line  
""" 
print("triple Quote berfungsi untuk membuat komentar multi line") 
a = int(input("silahkan masukan angka: ")) 
b=int(input("silahkan masukan angka: ")) 
c=a*b 
print('ini adalah hasil perkalian X & Y =',c) 
for i in range(1,10000):
    z=c
print(time.time() - mulai, "detik") 