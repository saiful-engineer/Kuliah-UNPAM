import java.io.*;

public class Pernyataanifelse1 {
    public static void main(String args[]) {
        BufferedReader dataIn = new BufferedReader(new InputStreamReader(System.in));
        
        // variabel untuk menyimpan input string
        String tugasStr = "", utsStr = "", uasStr = "";
        
        // variabel untuk nilai numerik
        double nilaiTugas = 0, nilaiUts = 0, nilaiUas = 0, rataRata = 0;

        try {
            // Input Nilai Tugas
            System.out.print("Masukkan Nilai Tugas: ");
            tugasStr = dataIn.readLine();
            nilaiTugas = Double.parseDouble(tugasStr);

            // Input Nilai UTS
            System.out.print("Masukkan Nilai UTS  : ");
            utsStr = dataIn.readLine();
            nilaiUts = Double.parseDouble(utsStr);

            // Input Nilai UAS
            System.out.print("Masukkan Nilai UAS  : ");
            uasStr = dataIn.readLine();
            nilaiUas = Double.parseDouble(uasStr);

            // Menghitung Rata-rata
            rataRata = (nilaiTugas + nilaiUts + nilaiUas) / 3;

            // Menampilkan hasil rata-rata
            System.out.println("Rata-rata Nilai Anda: " + rataRata);

            //IF-ELSE
            if (rataRata > 80) {
                System.out.println("Selamat Anda Lulus");
            } else {
                System.out.println("Maaf Anda Belum Lulus !");
            }

        } catch (IOException e) {
            System.out.println("Terjadi kesalahan pada input!");
        } catch (NumberFormatException e) {
            System.out.println("Kesalahan: Masukkan harus berupa angka!");
        }
    }
}
