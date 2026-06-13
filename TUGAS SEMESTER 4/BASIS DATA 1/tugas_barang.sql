create table barang (
KD_Barang VARCHAR(10) PRIMARY KEY,
Nama VARCHAR(50),
Satuan VARCHAR(20),
Harga_satuan INT,
Stok INT);

insert into barang (KD_Barang, Nama, Satuan, Harga_satuan, Stok) VALUES
('11001', 'sabun', 'bungkus', 3000, 1010),
('11002', 'deterjen', 'bungkus', 10000, 1044),
('11003', 'shampo', 'botol', 7000, 567);

select * from barang;

select Nama, (Stok / 10) AS Hasil_Pembagian from barang;

select Nama, (Harga_satuan + 500) as 'Harga Jual' from barang;

select * from barang where Stok > 1000 and Harga_satuan < 10000;

select * from barang where Satuan = 'Bungkus' or Stok < 700;

select * from barang where Stok >= 600;

select * from barang where Satuan != 'Bungkus';

select * from barang where Harga_satuan > 8000 or Stok > 1000;

