import java.util.Scanner;

public class Kasir_Minimarket {
    public static void main(String[] args) {
        try (Scanner input = new Scanner(System.in)) {
            int pilihan, jumlah;
            double harga, total, diskon = 0, bayar;
            String namaBarang;

            System.out.println("=== Selamat Datang di Minimarket Saiful ===");
            System.out.println("1. Minyak Goreng 1L - Rp 20.000");
            System.out.println("2. Beras 5kg        - Rp 75.000");
            System.out.println("3. Gula Pasir 1kg   - Rp 15.000");
            System.out.println("4. Mie Instan (Box) - Rp 110.000");
            System.out.println("5. Sabun Cuci 800ml - Rp 18.000");
            System.out.print("Pilih nomor produk: ");

            if (input.hasNextInt()) {
                pilihan = input.nextInt();
            } else {
                System.out.println("Error: Input harus berupa angka!");
                return;
            }

            switch (pilihan) {
                case 1 -> {
                    namaBarang = "Minyak Goreng 1L";
                    harga = 20000;
                }
                case 2 -> {
                    namaBarang = "Beras 5kg";
                    harga = 75000;
                }
                case 3 -> {
                    namaBarang = "Gula Pasir 1kg";
                    harga = 15000;
                }
                case 4 -> {
                    namaBarang = "Mie Instan (Box)";
                    harga = 110000;
                }
                case 5 -> {
                    namaBarang = "Sabun Cuci 800ml";
                    harga = 18000;
                }
                default -> {
                    System.out.println("Produk tidak tersedia dalam menu.");
                    return;
                }
            }

            System.out.print("Masukkan jumlah barang: ");
            if (input.hasNextInt()) {
                jumlah = input.nextInt();
            } else {
                System.out.println("Error: Jumlah harus angka!");
                return;
            }

            total = harga * jumlah;
            if (total >= 100000) {
                diskon = total * 0.10;
            }
            bayar = total - diskon;

            System.out.println("\n----------------------------------");
            System.out.println("         STRUK PEMBAYARAN         ");
            System.out.println("----------------------------------");
            System.out.println("Barang : " + namaBarang);
            System.out.println("Harga  : Rp " + harga);
            System.out.println("Jumlah : " + jumlah);
            System.out.println("----------------------------------");
            System.out.println("Total  : Rp " + total);
            System.out.println("Diskon : Rp " + diskon);
            System.out.println("TOTAL  : Rp " + bayar);
            System.out.println("----------------------------------");
            System.out.println("   Terima Kasih Telah Berbelanja  ");
        }
    }
}
