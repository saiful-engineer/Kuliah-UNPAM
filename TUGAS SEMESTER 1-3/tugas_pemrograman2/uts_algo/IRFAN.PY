# Membuat tiga kelas dengan metode yang sama (sound)
class TV:
    def sound(self):
        print("Suara TV: Volume tinggi dengan bass kuat.")

class Handphone:
    def sound(self):
        print("Suara Handphone: Nada dering lembut dan jernih.")

class Radio:
    def sound(self):
        print("Suara Radio: Siaran berita dengan suara statis kecil.")

# Membuat objek dari masing-masing kelas
tv = TV()
hp = Handphone()
radio = Radio()

# Memanggil metode sound() dari masing-masing objek
tv.sound()
hp.sound()
radio.sound()

# penggunaan polymorphism dengan perulangan
print("\n=== Contoh Polymorphism ===")
for device in (tv, hp, radio):
    device.sound()
    
#Suara dari TV: Volume bass dan treble seimbang.
#Suara dari Handphone: Volume kecil tapi jernih.
#Suara dari Radio: Ada sedikit noise tapi khas siaran FM.