 #tanpa menggunakan format string (f"") 
x='#'*50 
y='-'*15 
z='-'*18 
print(x) 
print(y+" Format Data String "+y) 
print(z+" Dzaya : 2022 "+z) 
print(x,'\n') 
#dengan menggunakan format string (f"") 
#pemanggilan variabel dengan menggunakan kurung kurawal { } 
n=65 
n1=65000 
n2=65000.66578 
print(f"format nomor ={n}") 
print(f" format nomor = {n1} = adalah bilangan ribuan") 
print(f"{n2:.3f}= bilangan desimal dengan 3 angka dibelakang koma") 
judul=f"\n{y} Operasi Aritmatika {y}" 
""" 
pemanggilan variabel dalam format string dapat dilakukan dimana saja 
diawal, ditengah serta diakhir  string 
dalam format string dapat juga dilakukan operasi aritmatika atau operasi yang 
lainnya 
""" 
print(judul) 
a=15 
b=10 
f_juml=f"hasil dari perkalian = {a*b}" 
print(f_juml) 
judul1=f"\n{y} Konversi  Bilangan {y}" 
print(judul1) 
desimal=255 
d2bin=bin(desimal) 
d2okt=oct(desimal) 
d2hex=hex(desimal) 
print(f'bilangan desimal :{desimal}') 
print(f'Konversi desimal ke Biner:{d2bin}') 
print(f'Konversi desimal ke Oktal :{d2okt}') 
print(f'Konversi desimal ke Heksadesimal :{d2hex}') 