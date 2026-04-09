#include <iostream>

using namespace std;

int main() {
    // Array 2 Dimensi
    int matriks[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    cout << "Array 2 Dimensi (Matriks 3x3):" << endl;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << matriks[i][j] << " ";
        }
        cout << endl;
    }

    // Array 3 Dimensi
    int citra_rgb[2][2][3] = {
        {
            {255, 0, 0},
            {0, 255, 0}
        },
        {
            {0, 0, 255},
            {255, 255, 0}
        }
    };

    cout << "\nArray 3 Dimensi (Citra RGB 2x2x3):" << endl;
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            cout << "Piksel (" << i << ", " << j << "): ";
            for (int k = 0; k < 3; k++) {
                cout << citra_rgb[i][j][k] << " ";
            }
            cout << endl;
        }
    }

    // Menu untuk memilih array
    int pilihan;
    cout << "\nPilih array yang ingin ditampilkan:" << endl;
    cout << "1. Array 2 Dimensi" << endl;
    cout << "2. Array 3 Dimensi" << endl;
    cin >> pilihan;

    if (pilihan == 1) {
        cout << "Array 2 Dimensi (Matriks 3x3):" << endl;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                cout << matriks[i][j] << " ";
            }
            cout << endl;
        }
    } else if (pilihan == 2) {
        cout << "Array 3 Dimensi (Citra RGB 2x2x3):" << endl;
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                cout << "Piksel (" << i << ", " << j << "): ";
                for (int k = 0; k < 3; k++) {
                    cout << citra_rgb[i][j][k] << " ";
                }
                cout << endl;
            }
        }
    } else {
        cout << "Pilihan tidak valid." << endl;
    }

    return 0;
}