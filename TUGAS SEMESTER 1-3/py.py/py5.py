import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk membuat titik-titik objek
def generate_object(rx, ry, theta):
    t = np.linspace(0, 2 * np.pi, theta)
    x = rx * np.cos(t)
    y = ry * np.sin(t)
    z = np.linspace(0, 10, theta)  # Menambahkan dimensi z untuk proyeksi perspektif
    return x, y, z

# Fungsi untuk proyeksi perspektif
def perspective_projection(x, y, z, distance):
    x_p = x / (distance - z)
    y_p = y / (distance - z)
    return x_p, y_p

# Parameter objek
rx, ry = 5, 3  # Panjang sumbu semi-mayor dan semi-minor
theta = 360   # Jumlah titik untuk membentuk objek
distance = 10  # Jarak titik pandang dari bidang proyeksi

# Membuat titik-titik objek
x, y, z = generate_object(rx, ry, theta)

# Proyeksi perspektif
x_pers, y_pers = perspective_projection(x, y, z, distance)

# Menggambar objek
plt.figure(figsize=(8, 6))
plt.plot(x_pers, y_pers, 'r-')
plt.scatter(x_pers, y_pers, color='purple')
plt.title('Proyeksi Perspektif')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()