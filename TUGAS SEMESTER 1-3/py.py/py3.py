import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk membuat titik-titik objek
def generate_object(rx, ry, theta):
    t = np.linspace(0, 2 * np.pi, theta)
    x = rx * np.cos(t)
    y = ry * np.sin(t)
    return x, y

# Fungsi untuk rotasi objek
def rotate(x, y, xp, yp, theta):
    theta_rad = np.radians(theta)
    x_r = xp + (x - xp) * np.cos(theta_rad) - (y - yp) * np.sin(theta_rad)
    y_r = yp + (x - xp) * np.sin(theta_rad) + (y - yp) * np.cos(theta_rad)
    return x_r, y_r

# Parameter objek
rx, ry = 5, 3  # Panjang sumbu semi-mayor dan semi-minor
theta = 360   # Jumlah titik untuk membentuk objek

# Membuat titik-titik objek
x, y = generate_object(rx, ry, theta)

# Titik pusat objek
xp, yp = 0, 0

# Rotasi objek
theta_rotation = 45  # Sudut rotasi dalam derajat
x_r, y_r = rotate(x, y, xp, yp, theta_rotation)

# Menggambar objek
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'g-')  # Objek hijau
plt.scatter(x, y, color='red')  # Titik-titik merah
plt.plot(x_r, y_r, 'b-')  # Objek setelah diputar
plt.scatter(x_r, y_r, color='blue')  # Titik-titik biru setelah diputar
plt.gca().set_aspect('equal', adjustable='box')
plt.show()