import java.util.Scanner;

public class ScannerInt {
    public static void main(String[] args) {
        try (Scanner input = new Scanner(System.in)){

        // --- BAGIAN 1: INPUT DATA ---
        System.out.print("Ketik bilangan pertama (Integer): ");
        int bilangan1 = input.nextInt();

        System.out.print("Ketik bilangan kedua (Integer): ");
        int bilangan2 = input.nextInt();

        // --- BAGIAN 2: PROSES DAN KONVERSI TIPE ---
        // Melakukan operasi perkalian
        int hasilInt = bilangan1 * bilangan2;

        // Menerapkan konsep Konversi Tipe (Casting dari int ke double)
        double hasilKonversi = (double) hasilInt;

        // --- BAGIAN 3: OUTPUT ---
        System.out.println("\n--- Hasil Perhitungan ---");
        System.out.println("Hasil asli (int)       : " + hasilInt);
        System.out.println("Hasil konversi (double): " + hasilKonversi);
        
        // Contoh tambahan: pembagian dengan konversi tipe untuk akurasi
        double hasilBagi = (double) bilangan1 / bilangan2;
        System.out.println("Hasil pembagian presisi: " + hasilBagi);
        }
    }
}