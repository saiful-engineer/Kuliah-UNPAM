#include <iostream>  // Library standar untuk input dan output

using namespace std;

int main() {
    // -------------------------
    // ARRAY 2 DIMENSI
    // -------------------------
    int array2D[2][3] = {
        {1, 2, 3},
        {4, 5, 6}
    }; 
    // Deklarasi array 2 dimensi berukuran 2x3.
    // Baris pertama: 1, 2, 3
    // Baris kedua: 4, 5, 6

    // Menampilkan array 2 dimensi
    cout << "Isi array 2 dimensi:\n";
    for (int i = 0; i < 2; i++) {              // Loop baris
        for (int j = 0; j < 3; j++) {          // Loop kolom
            cout << array2D[i][j] << " ";      // Cetak elemen
        }
        cout << endl;                          // Pindah baris
    }

    cout << endl;  // Baris kosong sebagai pemisah

    // -------------------------
    // ARRAY 3 DIMENSI
    // -------------------------
    int array3D[2][2][3] = {
        {
            {1, 2, 3},
            {4, 5, 6}
        },
        {
            {7, 8, 9},
            {10, 11, 12}
        }
    };
    // Deklarasi array 3 dimensi berukuran 2x2x3.
    // Terdiri dari 2 blok (depth), masing-masing berisi 2 baris dan 3 kolom.

    // Menampilkan array 3 dimensi
    cout << "Isi array 3 dimensi:\n";
    for (int i = 0; i < 2; i++) {                 // Loop blok (depth)
        cout << "Blok ke-" << i + 1 << ":\n";     // Tampilkan blok ke-i
        for (int j = 0; j < 2; j++) {             // Loop baris dalam blok
            for (int k = 0; k < 3; k++) {         // Loop kolom
                cout << array3D[i][j][k] << " ";  // Cetak elemen
            }
            cout << endl;                         // Pindah baris
        }
        cout << endl;  // Pemisah antar blok
    }

    return 0;  // Program selesai
}