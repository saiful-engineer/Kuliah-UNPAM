import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk membuat titik-titik objek
def generate_object(rx, ry, theta):
    t = np.linspace(0, 2 * np.pi, theta)
    x = rx * np.cos(t)
    y = ry * np.sin(t)
    return x, y

# Parameter objek
rx, ry = 5, 3  # Panjang sumbu semi-mayor dan semi-minor
theta = 360   # Jumlah titik untuk membentuk objek

# Membuat titik-titik objek
x, y = generate_object(rx, ry, theta)

# Menggambar objek
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'g-')  # Objek hijau
plt.scatter(x, y, color='red')  # Titik-titik merah
plt.gca().set_aspect('equal', adjustable='box')
plt.show()