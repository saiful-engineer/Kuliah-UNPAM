import java.util.Scanner;

public class ScannerString {
    public static void main(String[] args) {
        try (Scanner masukan = new Scanner(System.in)){

        // Input Nama
        System.out.print("Ketik Nama Anda : ");
        String nama = masukan.nextLine();

        // Input Kode Kelas
        System.out.print("Ketik Kode Kelas : ");
        String kodeKelas = masukan.nextLine();

        // Menampilkan output Nama dan Kode Kelas
        System.out.println("\n--- Data Mahasiswa ---");
        System.out.println("Nama        : " + nama);
        System.out.println("Kode Kelas  : " + kodeKelas);
        System.out.println("Halo " + nama + " dari kelas " + kodeKelas + ", kamu sekarang sudah bisa Java!");

        }
    }
}