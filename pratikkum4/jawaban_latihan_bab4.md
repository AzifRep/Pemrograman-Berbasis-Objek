# Latihan Bab 4 - Kelas dan Objek

**1. Jika terdapat sebuah data tentang kendaraan, maka apa saja properti yang mungkin melekat pada kelas kendaraan tersebut?**
Properti yang melekat pada kelas kendaraan umumnya mencakup identitas fisik, spesifikasi teknis, serta status kepemilikan dan operasional kendaraan:
- **Merk / Pabrikan (`merk`)**: Nama merek atau pabrikan pembuat kendaraan (misal: Toyota, Honda, Yamaha).
- **Model / Tipe (`model`)**: Tipe atau seri kendaraan (misal: Avanza, Civic, NMAX).
- **Tahun Pembuatan (`tahun`)**: Tahun kendaraan tersebut diproduksi.
- **Warna (`warna`)**: Warna fisik kendaraan.
- **Bahan Bakar (`bahan_bakar`)**: Jenis bahan bakar yang digunakan (misal: Bensin, Solar, Listrik).
- **Nomor Polisi / Plat Nomor (`nomor_polisi`)**: Tanda nomor kendaraan bermotor resmi.
- **Nomor Rangka (`nomor_rangka`)**: Nomor identifikasi unik kendaraan (*Vehicle Identification Number* / VIN).
- **Kapasitas Mesin (`kapasitas_mesin`)**: Kapasitas silinder mesin dalam satuan cc.
- **Kecepatan Maksimum (`kecepatan_maks`)**: Batas kecepatan maksimal kendaraan (km/jam).
- **Status Mesin (`mesin_menyala`)**: Status kondisi mesin apakah sedang hidup atau mati (*boolean*).

**2. Modelkan rancangan kelas pada no 1 diatas dalam rancangan diagram kelas! Lengkapi pula akses modifier pada masing-masing properti!**
Akses modifier dalam diagram kelas UML disimbolkan dengan:
- `+` : Public (dapat diakses langsung dari luar kelas)
- `-` : Private (hanya dapat diakses di dalam kelas tersebut)
- `#` : Protected (dapat diakses di dalam kelas dan kelas turunannya)

Berikut adalah rancangan diagram kelas `Kendaraan`:

```
+-------------------------------------------------------------+
|                          Kendaraan                          |
+-------------------------------------------------------------+
| + merk: str                                                 |
| + model: str                                                |
| + tahun: int                                                |
| + warna: str                                                |
| + bahan_bakar: str                                          |
| - nomor_polisi: str                                         |
| - nomor_rangka: str                                         |
| - kapasitas_mesin: int                                      |
| - kecepatan_maks: int                                       |
| - mesin_menyala: bool                                       |
+-------------------------------------------------------------+
| + __init__(merk, model, tahun, warna, bahan_bakar, ...)     |
| + get_nomor_polisi(): str                                   |
| + set_nomor_polisi(nomor: str): void                        |
| + get_nomor_rangka(): str                                   |
| + nyalakan_mesin(): void                                    |
| + matikan_mesin(): void                                     |
| + info_kendaraan(): void                                    |
+-------------------------------------------------------------+
```

*Penjelasan Akses Modifier:*
- Properti **Public (`+`)** seperti `merk`, `model`, `tahun`, `warna`, dan `bahan_bakar` bersifat terbuka karena merupakan data umum yang aman untuk dibaca langsung dari luar objek.
- Properti **Private (`-`)** seperti `nomor_polisi`, `nomor_rangka`, `kapasitas_mesin`, `kecepatan_maks`, dan `mesin_menyala` (pada Python menggunakan awalan dua garis bawah `__`) dilindungi agar integritas data tetap terjaga dan tidak dapat dimodifikasi sembarangan dari luar tanpa melalui method/prosedur yang sah (enkapsulasi).

**3. Diketahui kelas berikut ini:**
```python
class Siswa:
    nama = "Andi"
```
Gunakan fungsi hasattr() untuk memeriksa:
a. apakah atribut nama tersedia
b. apakah atribut kelas tersedia

*Implementasi kode program dapat dilihat pada file:* `Latihan3.py`

Hasil eksekusi:
- `hasattr(Siswa, 'nama')` mengembalikan nilai `True` karena atribut `nama` terdapat di dalam kelas `Siswa`.
- `hasattr(Siswa, 'kelas')` mengembalikan nilai `False` karena atribut `kelas` tidak didefinisikan di dalam kelas `Siswa`.

**4. Buat kelas AkunBank yang dilengkapi dengan properti:**
- a. atribut public: nama
- b. atribut private: __saldo
- c. method public: lihat_saldo() dan setor_uang()
Kemudian tampilkan bagaimana atribut private tidak dapat diakses langsung dari luar kelas.

*Implementasi kode program dapat dilihat pada file:* `Latihan4.py`

Pada saat mencoba mengakses atribut private secara langsung melalui `akun.__saldo`, Python akan menghasilkan error:
`AttributeError: 'AkunBank' object has no attribute '__saldo'`
Hal ini membuktikan bahwa atribut private terenkapsulasi dan terlindungi dari akses langsung dari luar kelas.

**5. Buat kelas Hitung yang memiliki method jumlah() untuk menjumlahkan 2 dan 3 angka dengan menggunakan konsep method overloading!**

*Implementasi kode program dapat dilihat pada file:* `Latihan5.py`

Pada bahasa Python, konsep *method overloading* dapat diimplementasikan dengan memanfaatkan *default parameter* (sebagaimana diajarkan di Praktikum 4.6). Dengan demikian, satu method `jumlah()` yang sama dapat dipanggil baik dengan 2 argumen maupun dengan 3 argumen:
- `h.jumlah(2, 3)` menghasilkan `5`
- `h.jumlah(2, 3, 4)` menghasilkan `9`
