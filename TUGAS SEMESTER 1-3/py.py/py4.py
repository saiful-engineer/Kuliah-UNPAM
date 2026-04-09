import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk membuat titik-titik objek
def generate_object(rx, ry, theta):
    t = np.linspace(0, 2 * np.pi, theta)
    x = rx * np.cos(t)
    y = ry * np.sin(t)
    return x, y

# Fungsi untuk proyeksi ortografik
def orthographic_projection(x, y):
    return x, y

# Fungsi untuk proyeksi aksanometrik
def axonometric_projection(x, y, angle):
    x_a = x * np.cos(np.radians(angle)) - y * np.sin(np.radians(angle))
    y_a = x * np.sin(np.radians(angle)) + y * np.cos(np.radians(angle))
    return x_a, y_a

# Parameter objek
rx, ry = 5, 3  # Panjang sumbu semi-mayor dan semi-minor
theta = 360   # Jumlah titik untuk membentuk objek

# Membuat titik-titik objek
x, y = generate_object(rx, ry, theta)

# Proyeksi ortografik
x_ortho, y_ortho = orthographic_projection(x, y)

# Proyeksi aksanometrik
angle = 30  # Sudut proyeksi aksanometrik
x_axon, y_axon = axonometric_projection(x, y, angle)

# Menggambar objek
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(x_ortho, y_ortho, 'g-')
plt.scatter(x_ortho, y_ortho, color='red')
plt.title('Proyeksi Ortografik')
plt.gca().set_aspect('equal', adjustable='box')

plt.subplot(1, 2, 2)
plt.plot(x_axon, y_axon, 'b-')
plt.scatter(x_axon, y_axon, color='blue')
plt.title('Proyeksi Aksanometrik')
plt.gca().set_aspect('equal', adjustable='box')

plt.show()