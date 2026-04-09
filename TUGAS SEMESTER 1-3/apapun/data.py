import pandas as pd
import numpy as np

# Buat data dummy
np.random.seed(42)  # agar hasilnya konsisten

# Buat DataFrame
data = {
    "No": range(1, 101),
    "Nama": [f"Siswa_{i}" for i in range(1, 101)],
    "Nilai UTS": np.random.randint(50, 100, size=100),
    "Nilai UAS": np.random.randint(50, 100, size=100)
}

df = pd.DataFrame(data)

# Simpan ke file Excel
df.to_excel("Data_Nilai_Siswa.xlsx", index=False)
print("File Excel berhasil dibuat: Data_Nilai_Siswa.xlsx")
