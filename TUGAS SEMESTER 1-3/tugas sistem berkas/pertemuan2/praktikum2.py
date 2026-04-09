#praktikum 2 : Array dengan modul array dan library numpy

#bagian 1: menggunakan modul array 
#==============================
import array

a = array.array('i', [1,2,3]) #buat array integer
a.append(4) #nambah elemen 4
print("array dari modul array: ") #tampilan elemen array
print(list(a))


#bagian 2: menggunakan library numpy
#=============================
import numpy as np

b = np.array([[1,2], [3,4]]) # buat array 2D
print("\nArray Numpy sebelum di ubah: ") # array sebelum di ubah
print(b)

b[1,0] = 99 # membuat elemen baris ke 1 dan kolom ke 0 menjadi 99
print("\nArray Numpy setelah di ubah: ") # array setelah di ubah
print(b)