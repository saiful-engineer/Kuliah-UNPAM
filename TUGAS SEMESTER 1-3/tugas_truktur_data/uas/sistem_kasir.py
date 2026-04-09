class Produk:
    """Node untuk menyimpan data produk dalam Hash Table"""
    def __init__(self, id_produk, nama, harga):
        self.id_produk = id_produk
        self.nama = nama
        self.harga = harga
        self.next = None  # Untuk menangani collision (Chaining)

class HashTable:
    """Implementasi Hash Table untuk database produk"""
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def _hash_function(self, key):
        return hash(key) % self.size

    def tambah_produk(self, id_produk, nama, harga):#
        index = self._hash_function(id_produk)
        baru = Produk(id_produk, nama, harga)
        if self.table[index] is None:
            self.table[index] = baru
        else:
            current = self.table[index]
            while current.next:
                if current.id_produk == id_produk:
                    current.nama, current.harga = nama, harga
                    return
                current = current.next
            current.next = baru

    def cari_produk(self, id_produk):
        index = self._hash_function(id_produk)
        current = self.table[index]
        while current:
            if current.id_produk == id_produk:
                return current
            current = current.next
        return None

class StackUndo:
    """Implementasi Stack untuk fitur Undo Transaksi"""
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)#

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0

class KeranjangNode:
    """Node untuk Linked List Keranjang Belanja"""
    def __init__(self, produk, jumlah):#
        self.produk = produk
        self.jumlah = jumlah
        self.next = None

class KasirApp:
    def __init__(self):
        self.db_produk = HashTable()
        self.keranjang_head = None
        self.history_undo = StackUndo()
        self._init_data()

    def _init_data(self):
        # Data awal (Seeding)
        self.db_produk.tambah_produk("P01", "Beras 5kg", 75000)
        self.db_produk.tambah_produk("P02", "Minyak Goreng", 20000)
        self.db_produk.tambah_produk("P03", "Gula Pasir", 15000)

    def tambah_ke_keranjang(self, id_produk, jumlah):
        produk = self.db_produk.cari_produk(id_produk)
        if produk:
            baru = KeranjangNode(produk, jumlah)
            baru.next = self.keranjang_head
            self.keranjang_head = baru
            self.history_undo.push(baru)
            print(f"{produk.nama} berhasil ditambah!")
        else:
            print("Produk tidak ditemukan!")

    def undo_transaksi(self):
        last_item = self.history_undo.pop()
        if last_item and self.keranjang_head:
            # Hapus dari Linked List (Hanya jika item terakhir sama)
            if self.keranjang_head == last_item:
                self.keranjang_head = self.keranjang_head.next
                print(f"Undo berhasil: {last_item.produk.nama} dihapus.")
        else:
            print(" Tidak ada transaksi untuk di-undo.")

    def tampilkan_keranjang(self):
        print("\n--- KERANJANG BELANJA ---")
        current = self.keranjang_head
        total = 0
        if not current:
            print("Keranjang kosong.")
            return
        
        # Traversal Iteratif (Mirip konsep DFS pada list linear)
        while current:
            subtotal = current.produk.harga * current.jumlah
            print(f"- {current.produk.nama} x{current.jumlah}: Rp{subtotal}")
            total += subtotal
            current = current.next
        print(f"TOTAL: Rp{total}")

def menu():
    app = KasirApp()
    while True:
        print("\n=== SISTEM KASIR MINI MARKET ===")
        print("1. Tambah Barang ke Keranjang")
        print("2. Cari Produk (Cek Harga)")
        print("3. Lihat Keranjang")
        print("4. Undo Transaksi Terakhir")
        print("5. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            id_p = input("ID Produk: ")
            qty = int(input("Jumlah: "))
            app.tambah_ke_keranjang(id_p, qty)
        elif pilihan == "2":
            id_p = input("Masukkan ID Produk: ")
            res = app.db_produk.cari_produk(id_p)
            if res: print(f"Ditemukan: {res.nama} - Rp{res.harga}")
            else: print("Produk tidak ada.")
        elif pilihan == "3":
            app.tampilkan_keranjang()
        elif pilihan == "4":
            app.undo_transaksi()
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    menu()
