import numpy as np
import pandas as pd

# Target: data tinggi badan ~ Normal(168, 7)
np.random.seed(42)
data = np.random.normal(loc=168, scale=7, size=100)

# Simpan ke Excel
df = pd.DataFrame({'TINGGI_BADAN': data})
df.to_excel("Data_Tinggi_Badan_Normal.xlsx", index=False)
print("File Data_Tinggi_Badan_Normal.xlsx telah dibuat.")
