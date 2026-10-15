# try:
#     bil1 = int(input("masukkan angka 1: "))
#     bil2 = int(input("masukkan angka 2: "))
    
#     hasil = bil1 /bil2
#     print("Hasilnya: ", hasil)

# except ZeroDivisionError:
#     print("Tidak bisa pembagian dengan nol (ZeroDivisionError)")
# except ValueError:
#     print("Input harus berupa angka bulat, bukan huruf (ValueError)")
# except Exception as e:
#     print("Terjadi kesalahan yang lain: ", e)

# print("<< End Program >>")

angka = [10,20,30,40,50]
try:
    idx = int(input("Masukkan Index = "))
    print(angka[idx])

except IndexError:
    print("Index yang anda masukkan melebihi batas (IndexError)")
except ValueError:
    print("Input harus berupa angka bulat, bukan huruf (ValueError)")
except Exception as e:
    print("Terjadi kesalahan yang lain: ", e)

print("<< End Program >>")