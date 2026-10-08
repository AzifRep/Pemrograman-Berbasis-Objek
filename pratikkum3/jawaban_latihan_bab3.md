# Latihan Bab 3 - Eksepsi

**1. Mengapa sebuah program perlu memiliki mekanisme penanganan error? Jelaskan dampaknya jika error tidak ditangani dengan baik!**
Mekanisme penanganan error (*exception handling*) diperlukan agar program tidak berhenti secara mendadak (*crash*) saat terjadi kesalahan yang tidak terduga pada saat *runtime* (seperti kesalahan input pengguna, file tidak ditemukan, atau pembagian dengan nol). 
Dampak jika error tidak ditangani dengan baik:
- Program langsung berhenti (*force close*), menyebabkan proses terhenti di tengah jalan dan data yang sedang diproses berisiko hilang/rusak.
- Menurunkan *User Experience* (UX) karena pengguna dihadapkan pada pesan kesalahan teknis yang membingungkan.
- Potensi celah keamanan (*security risk*), di mana *traceback* atau pesan sistem internal yang bocor dapat dimanfaatkan oleh pihak yang tidak bertanggung jawab untuk mencari celah sistem.

**2. Jelaskan keuntungan penggunaan custom exception dibandingkan hanya menggunakan exception bawaan Python!**
Keuntungan menggunakan *custom exception*:
- **Lebih Spesifik & Deskriptif:** Nama kelas eksepsi dapat disesuaikan dengan logika bisnis/domain aplikasi (misal `SaldoTidakMencukupiError` lebih mudah dipahami maksudnya dibandingkan sekadar `ValueError`).
- **Pemisahan Penanganan Error:** Memudahkan pembuatan blok penanganan error terpisah untuk skenario khusus tanpa khawatir tercampur dengan penanganan error bawaan yang serupa.
- **Dapat Membawa Data Tambahan:** *Custom exception* dapat menyimpan atribut tambahan (misal nilai saldo saat ini, jumlah yang diminta, kode status) untuk mempermudah debugging dan logging.

**3. Jelaskan cara kerja blok try, except, dan finally dalam penanganan error pada Python!**
- `try`: Blok ini digunakan untuk menempatkan kode program yang berpotensi menghasilkan error/eksepsi. Python akan mencoba mengeksekusi kode di dalam blok ini.
- `except`: Jika terjadi error pada blok `try`, aliran program langsung melompat ke blok `except` yang sesuai untuk menangani kesalahan tersebut sehingga program tetap berjalan.
- `finally`: Blok yang **pasti dieksekusi**, baik terjadi error ataupun tidak pada blok `try`. Biasanya digunakan untuk operasi pembersihan resource (seperti menutup file, menutup koneksi database, atau menghapus temporary file).

**4. Buat skenario kesalahan berikut ini dalam sebuah program dan tangkap kesalahan tersebut menggunakan kelas eksepsi yang sesuai. Buat kelas eksekusi yang bertahap dari khusus ke baseException:**
- a. `OverflowError` > `ArithmeticError` > `Exception`
- b. `FileExistsError` > `OSError` > `Exception`
- c. `ZipImporterError` > `ImportError` > `Exception`

*Implementasi kode program dapat dilihat pada file:* `skenario_error.py`

**5. Buat program sederhana ATM dengan fitur tarik tunai yang mampu menangani kesalahan untuk kondisi berikut:**
- a. Nominal yang dimasukkan bukan angka
- b. Saldo tidak mencukupi
- c. Nominal kurang dari atau sama dengan 0

*Implementasi kode program dapat dilihat pada file:* `Latihan5.py`
