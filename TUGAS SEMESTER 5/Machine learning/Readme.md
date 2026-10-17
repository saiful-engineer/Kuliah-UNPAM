# Laporan Praktikum Machine Learning

Repositori ini berisi implementasi alur kerja (workflow) *Machine Learning* secara komprehensif menggunakan bahasa pemrograman Python dan pustaka Scikit-Learn,dan lainnya.

**Penulis:** SAIFUL BAHRI   
**Kelas:** 05TPLP022  

---

##  Deskripsi Proyek

Proyek ini bertujuan untuk membangun alur kerja *data science* secara lengkap, mulai dari pemuatan data, pembersihan, analisis eksploratif, hingga pemodelan dan evaluasi. Terdapat dua dataset utama yang digunakan dalam praktikum ini:
1. **Dataset Konsumsi Listrik Rumah Tangga:** Digunakan untuk tugas regresi, klasifikasi, klastering, dan reduksi dimensi.
2. **Dataset Digits (Scikit-Learn):** Digunakan untuk tugas klasifikasi gambar angka tulisan tangan beresolusi rendah ($8 \times 8$ piksel).

##  Library dan Teknologi yang Digunakan

*   **Manipulasi & Analisis Data:** `numpy`, `pandas`
*   **Visualisasi Data:** `matplotlib`, `seaborn`
*   **Machine Learning:** `scikit-learn` (Scikit-Learn)

##  Alur Kerja (Workflow)

1. **Persiapan Data (Data Preparation):** 
   * *Data Loading* dari file CSV.
   * *Data Cleaning* (penanganan *missing value*, penghapusan duplikat, dan penyesuaian tipe data datetime).
   * Transformasi dan standardisasi fitur menggunakan `StandardScaler`.
2. **Analisis Data Eksploratif (EDA & EXDA):** 
   * Visualisasi distribusi data (Histogram), deteksi *outlier* (Boxplot), dan korelasi antar fitur (Heatmap).
   * Analisis tren konsumsi daya listrik berdasarkan jam, bulan, dan hari.
3. **Pembagian Data (Data Splitting):** 
   * Penggunaan `train_test_split` untuk membagi data latih dan data uji.
   * Validasi model menggunakan teknik `StratifiedKFold` *Cross Validation*.
4. **Pemodelan Supervised Learning:** 
   * **Klasifikasi:** *Decision Tree*, *Logistic Regression*, dan *Support Vector Machine* (SVM).
   * **Regresi:** *Linear Regression* dan *Support Vector Regression* (SVR).
5. **Pemodelan Unsupervised Learning:** 
   * **Klastering:** *K-Means* untuk mengelompokkan pola konsumsi listrik.
   * **Reduksi Dimensi:** *Principal Component Analysis* (PCA) untuk visualisasi data multi-dimensi.
6. **Optimasi Model (Hyperparameter Tuning):** 
   * Penggunaan `GridSearchCV` untuk mencari kombinasi parameter terbaik secara otomatis.

##  Hasil dan Kesimpulan Utama

Berdasarkan pengujian beberapa algoritma, didapatkan hasil sebagai berikut:

*   **Klasifikasi Konsumsi Daya Tinggi:** Model **SVM dengan kernel RBF** menghasilkan akurasi tertinggi sebesar **88,45%**. Teknik tuning parameter (*Grid Search*) terbukti dapat meningkatkan stabilitas dan akurasi model (*Cross Validation Score*: 88,50%).
*   **Regresi Prediksi Daya Aktif:** Model **Linear Regression** dan **SVR** memiliki performa yang sebanding, dengan Linear Regression mampu menjelaskan sekitar **77%** variasi daya aktif ($R^{2} = 0,7703$). Hal ini menunjukkan sebagian besar hubungan antar fitur bernilai linear.
*   **Klastering (K-Means):** Data berhasil dikelompokkan menjadi 4 klaster utama yang merepresentasikan pola penggunaan alat elektronik (konsumsi rendah, penggunaan pemanas/AC, aktivitas dapur, dan aktivitas *laundry*).
*   **Klasifikasi Gambar Angka:** Model **SVM** yang dioptimasi dengan *Grid Search* sangat efektif untuk mengklasifikasikan gambar angka berdimensi kecil dengan tingkat akurasi mencapai **98,22%**.

---
