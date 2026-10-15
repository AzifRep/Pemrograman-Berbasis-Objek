from kalkulator import tambah, kurang, kali, bagi

def konfirmasi():
    konfirmasi = input("\nHitung lagi? (y/n): ")
    if konfirmasi == "n":
        exit()
print("=== Kalkulator ===")
while True:
    try:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
    except ValueError:
        print("Error: Input harus berupa angka")
        konfirmasi()
        
    print("\n1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    try:
        operasi = float(input("Pilih operasi: "))
        if operasi == 1:
            print("Hasil: ", tambah(a, b))
            konfirmasi()
        elif operasi == 2:
            print("Hasil: ", kurang(a, b))
            konfirmasi()
        elif operasi == 3:
            print("Hasil: ", kali(a, b))
            konfirmasi()
        elif operasi == 4:
            try:
                print("Hasil: ", bagi(a, b))
            except ZeroDivisionError:
                print("Error: Tidak boleh membagi dengan 0")
            konfirmasi()
        else:
            print("Error: Pilihan operasi tidak tersedia")
            konfirmasi()
    except ValueError:
        print("Error: Pilihan operasi harus berupa angka")
        konfirmasi()