/**
 * Program Kalkulator Operasi Aritmatika dan Perbandingan
 * Deskripsi: Menghitung operasi penjumlahan, pengurangan, perkalian, 
 * pembagian, dan perbandingan berdasarkan nilai variabel yang ditentukan.
 */
public class OperasiMatematika {

    public static void main(String[] args) {
        // 1. Inisialisasi variabel sesuai ketentuan tugas
        int A = 10;
        int B = 25;
        int C = 40;

        System.out.println("=== Hasil Perhitungan Program ===");
        System.out.println("Nilai A = " + A + ", B = " + B + ", C = " + C);
        System.out.println("---------------------------------");

        // 2. Operasi Penjumlahan (a. A + B + C)
        int hasilPenjumlahan = A + B + C;
        System.out.println("a. Hasil A + B + C     : " + hasilPenjumlahan);

        // 3. Operasi Pengurangan (b. C - A)
        int hasilPengurangan = C - A;
        System.out.println("b. Hasil C - A         : " + hasilPengurangan);

        // 4. Operasi Perkalian (c. C * B)
        int hasilPerkalian = C * B;
        System.out.println("c. Hasil C * B         : " + hasilPerkalian);

        // 5. Operasi Pembagian (d. B + A / 3)
        // Menggunakan double agar hasil pembagian lebih presisi
        double hasilPembagian = B + (double) A / 3;
        System.out.printf("d. Hasil B + A / 3     : %.2f\n", hasilPembagian);

        // 6. Operasi Perbandingan Nilai (e. C == B)
        // Menghasilkan nilai boolean (true/false)
        boolean isSamaDengan = (C == B);
        System.out.println("e. Apakah C == B?      : " + isSamaDengan);
        
        System.out.println("---------------------------------");
    }
}