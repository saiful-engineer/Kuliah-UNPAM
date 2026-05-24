mysql> create database Koperasi;
Query OK, 1 row affected (0.115 sec)

mysql> use Koperasi;
Database changed
mysql> create table anggota (
    -> NIK CHAR(16) NOT NULL,
    -> Nama VARCHAR(50),
    -> Alamat VARCHAR(100),
    -> Telepon VACHAR(15),
    -> PRIMARY KEY (NIK)
    -> );

mysql> create table anggota (
    ->     -> NIK CHAR(16) NOT NULL,
    ->     -> Nama VARCHAR(50),
    ->     -> Alamat VARCHAR(100),
    ->     -> Telepon VACHAR(15),
    ->     -> PRIMARY KEY (NIK)
    ->  );

mysql> CREATE TABLE Anggota (
    -> NIK CHAR(16) NOT NULL,
    -> Nama VARCHAR(50),
    -> Alamat VARCHAR(100),
    -> Telpon VARCHAR(15),
    -> PRIMARY KEY (NIK)
    -> );
Query OK, 0 rows affected (0.358 sec)

mysql> CREATE TABLE Pengurus (
    -> IDPengurus INT NOT NULL,
    -> NIK CHAR(16) NOT NULL,
    -> Jabatan VARCHAR(20),
    -> PRIMARY KEY (IDPengurus)
    -> );
Query OK, 0 rows affected (0.486 sec)

mysql> desc Anggota;
+--------+--------------+------+-----+---------+-------+
| Field  | Type         | Null | Key | Default | Extra |
+--------+--------------+------+-----+---------+-------+
| NIK    | char(16)     | NO   | PRI | NULL    |       |
| Nama   | varchar(50)  | YES  |     | NULL    |       |
| Alamat | varchar(100) | YES  |     | NULL    |       |
| Telpon | varchar(15)  | YES  |     | NULL    |       |
+--------+--------------+------+-----+---------+-------+
4 rows in set (0.452 sec)

mysql> desc Pengurus;
+------------+-------------+------+-----+---------+-------+
| Field      | Type        | Null | Key | Default | Extra |
+------------+-------------+------+-----+---------+-------+
| IDPengurus | int         | NO   | PRI | NULL    |       |
| NIK        | char(16)    | NO   |     | NULL    |       |
| Jabatan    | varchar(20) | YES  |     | NULL    |       |
+------------+-------------+------+-----+---------+-------+
3 rows in set (0.028 sec)

mysql> ALTER TABLE Anggota ADD Email VARCHAR(50);
Query OK, 0 rows affected (1.146 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> ALTER TABLE Pengurus MODIFY Jabatan VARCHAR(15);
Query OK, 0 rows affected (1.096 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> DESC Pengurus;
+------------+-------------+------+-----+---------+-------+
| Field      | Type        | Null | Key | Default | Extra |
+------------+-------------+------+-----+---------+-------+
| IDPengurus | int         | NO   | PRI | NULL    |       |
| NIK        | char(16)    | NO   |     | NULL    |       |
| Jabatan    | varchar(15) | YES  |     | NULL    |       |
+------------+-------------+------+-----+---------+-------+
3 rows in set (0.029 sec)

mysql> ALTER TABLE Anggota CHANGE Telpon NoHP VARCHAR(15);
Query OK, 0 rows affected (0.329 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> DESC Anggota;
+--------+--------------+------+-----+---------+-------+
| Field  | Type         | Null | Key | Default | Extra |
+--------+--------------+------+-----+---------+-------+
| NIK    | char(16)     | NO   | PRI | NULL    |       |
| Nama   | varchar(50)  | YES  |     | NULL    |       |
| Alamat | varchar(100) | YES  |     | NULL    |       |
| NoHP   | varchar(15)  | YES  |     | NULL    |       |
| Email  | varchar(50)  | YES  |     | NULL    |       |
+--------+--------------+------+-----+---------+-------+
5 rows in set (0.043 sec)

mysql>
