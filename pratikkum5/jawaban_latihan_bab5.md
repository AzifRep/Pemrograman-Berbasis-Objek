# Latihan Bab 5 - Pewarisan (Inheritance)

**1. Mengapa konsep pewarisan dapat membantu mengurangi penulisan kode yang berulang? Jelaskan.**

Pewarisan (*inheritance*) menerapkan prinsip **DRY (Don't Repeat Yourself)** dan *code reusability* dalam pemrograman berorientasi objek:
- **Pemusatan Kode Bersama (*Common Code*):** Atribut dan method yang dimiliki oleh banyak entitas sejenis cukup didefinisikan satu kali di dalam kelas induk (*superclass*).
- **Pemberian Hak Akses ke Subclass:** Semua kelas anak (*subclass*) secara otomatis mewarisi properti dan method tersebut tanpa perlu menulis ulang deklarasi dan logika kode yang sama.
- **Kemudahan Pemeliharaan (*Maintainability*):** Jika terdapat pembaruan logika atau perbaikan *bug*, perubahan cukup dilakukan pada satu tempat (di kelas induk), dan seluruh kelas turunan akan langsung memperoleh pembaruan tersebut.

---

**2. Apa fungsi `super()` pada Python? Jelaskan kapan fungsi tersebut digunakan.**

Fungsi `super()` digunakan untuk merujuk dan mengakses method maupun konstruktor milik kelas induk (*superclass*) dari dalam kelas anak (*subclass*).

*Kapan fungsi tersebut digunakan:*
- **Memanggil Konstruktor Induk:** Digunakan di dalam method `__init__()` milik subclass (`super().__init__(...)`) agar inisialisasi variabel/state pada kelas induk tetap dieksekusi saat objek kelas anak dibuat.
- **Menghindari Hardcoding Nama Kelas Induk:** Mempermudah *refactoring* dan mendukung *multiple inheritance* karena `super()` secara dinamis mengikuti urutan *Method Resolution Order* (MRO) tanpa perlu menyebut nama kelas induk secara eksplisit (misal: menggantikan `Mamalia.__init__(self, nama)`).
- **Memperluas (*Extend*) Perilaku Method:** Saat melakukan *method overriding*, kita bisa memanggil method versi induk terlebih dahulu dengan `super().nama_method()`, lalu menambahkan logika baru di bawahnya.

---

**3. Dalam suatu program, subclass memiliki method yang sama dengan superclass tetapi isi method berbeda. Analisis mengapa overriding diperlukan pada kondisi tersebut!**

*Method overriding* diperlukan karena:
- **Spesialisasi Perilaku:** Meskipun superclass menyediakan perilaku umum (*generic*), setiap subclass sering kali memiliki karakteristik operasional yang spesifik di dunia nyata.
  - *Contoh:* Superclass `Hewan` memiliki method `bergerak()`. Turunan `Burung` bergerak dengan cara terbang, sedangkan `Ikan` bergerak dengan cara berenang. Keduanya memiliki nama aksi yang sama (`bergerak`), namun implementasinya berbeda.
- **Konsistensi Antarmuka (*Polymorphism*):** Program pemanggil (*caller*) dapat memanggil nama method yang sama pada berbagai objek yang berbeda tanpa perlu mengetahui tipe spesifiknya secara mendetail, karena masing-masing objek akan menjalankan implementasi method miliknya sendiri.

---

**4. Menurut Anda, kapan penggunaan inheritance lebih efektif dibandingkan membuat class terpisah? Jelaskan dengan contoh kasus.**

Penggunaan *inheritance* lebih efektif ketika:
- Terdapat hubungan hierarki yang nyata berupa **"is-a"** (adalah sebuah), bukan relasi "has-a" (memiliki/komposisi).
- Terdapat kesamaan atribut dan perilaku yang signifikan antar kelas, di mana kelas-kelas tersebut hanya berbeda pada detail khusus atau implementasi spesifik.

*Contoh Kasus:*
- **Sistem Penggajian Karyawan:**
  - Jika membuat kelas terpisah: `KaryawanTetap`, `KaryawanKontrak`, dan `KaryawanMagang` dibuat sendiri-sendiri dari nol, maka atribut seperti `id_karyawan`, `nama`, `email`, dan method `presensi()` akan diduplikasi di ketiga kelas.
  - Jika menggunakan *inheritance*: Buat superclass `Karyawan` yang memuat `id_karyawan`, `nama`, `email`, serta `presensi()`. Lalu buat subclass `KaryawanTetap` (ditambah tunjangan) dan `KaryawanKontrak` (berdasarkan durasi kontrak) yang mewarisi `Karyawan` serta meng-override method `hitung_gaji()`. Cara ini jauh lebih rapi, terstruktur, dan mudah dikembangkan.

---

**5. Sistem Informasi Perusahaan Transportasi Berbasis OOP**

### a. Rancangan Diagram Kelas

```
                       +---------------------------------------+
                       |           <<AbstractClass>>           |
                       |               Kendaraan               |
                       +---------------------------------------+
                       | + jumlah_kendaraan: int = 0           |
                       | + nama: str                           |
                       | + kecepatan: int                      |
                       +---------------------------------------+
                       | + __init__(nama: str, kecepatan: int) |
                       | + {abstract} bergerak(): str          |
                       +---------------------------------------+
                                          ^
                                          |
                        +-----------------+-----------------+
                        |                                   |
        +-------------------------------+   +-------------------------------+
        |             Mobil             |   |             Motor             |
        +-------------------------------+   +-------------------------------+
        |                               |   |                               |
        +-------------------------------+   +-------------------------------+
        | + __init__(nama, kecepatan)   |   | + __init__(nama, kecepatan)   |
        | + bergerak(): str             |   | + bergerak(): str             |
        +-------------------------------+   +-------------------------------+
```

### b & c. Implementasi Program Python dan Pembuatan Objek
Implementasi program Python lengkap tersimpan pada file: `latihan5.py`

*Hasil Eksekusi Program:*
```text
Toyota Avanza melaju di jalan raya dengan kecepatan 100 km/jam.
Honda Civic melaju di jalan raya dengan kecepatan 140 km/jam.
Yamaha NMAX meliuk di kemacetan dengan kecepatan 80 km/jam.
Honda Beat meliuk di kemacetan dengan kecepatan 60 km/jam.
Total kendaraan: 4
```

---

## Analisis & Pembahasan Pertanyaan Modul Praktikum 5.1 - 5.5

1. **Perbedaan `issubclass()` dan `isinstance()` (Praktikum 5.1):**
   - `issubclass(ClassA, ClassB)`: Memeriksa relasi hierarki antara **dua kelas** (apakah kelas pertama merupakan turunan dari kelas kedua).
   - `isinstance(obj, ClassA)`: Memeriksa apakah **sebuah objek/instance** dibuat dari kelas tertentu atau dari turunan kelas tersebut.

2. **Kesimpulan Pemanggilan Konstruktor (Praktikum 5.2):**
   - Menggunakan `super().__init__(...)` lebih direkomendasikan dibanding memanggil `NamaKelasInduk.__init__(self, ...)` karena lebih fleksibel, otomatis mengikuti urutan MRO (*Method Resolution Order*), dan tidak terpengaruh jika nama kelas induk diubah saat refactoring.

3. **Penyebab Error pada Praktikum 5.3 (Langkah 7):**
   - Muncul `AttributeError: 'Kucing' object has no attribute 'gigi'` karena konstruktor kelas `Kucing` mendefinisikan `__init__` baru tanpa memanggil konstruktor milik `Mamalia`. Akibatnya, `self.gigi = True` milik `Mamalia` tidak pernah diinisialisasi saat objek `Kucing` dibuat. Solusinya adalah memanggil `super().__init__()` di dalam konstruktor `Kucing`.

4. **Properti yang Terpanggil pada Multiple Inheritance (Praktikum 5.4):**
   - Pada `Campuran(British, Ragdoll)`, atribut/method yang sama (seperti `warna` dan `sifat()`) diambil dari `British` karena `British` berada di urutan pertama (pencarian MRO dari kiri ke kanan).
   - Ketika urutan dibalik menjadi `Campuran(Ragdoll, British)`, atribut/method yang diambil berganti milik `Ragdoll`.

5. **Penyebab TypeError pada Kelas Abstrak (Praktikum 5.5):**
   - Muncul `TypeError: Can't instantiate abstract class ...` karena aturan modul `abc` melarang instansiasi kelas abstrak secara langsung atau kelas turunannya yang belum mengimplementasikan seluruh method yang didekorasi dengan `@abstractmethod`.
