from HitungBangun.luas.persegi import *
from HitungBangun.luas.lingkaran import *
from HitungBangun.volume.kubus import *
from HitungBangun.volume.tabung import *

def main():
    while True:
        print("1. Luas Persegi")
        print("2. Luas Lingkaran")
        print("3. Volume Kubus")
        print("4. Volume Tabung")
        print("5. Keluar")
        pilihan = input("Masukkan pilihan: ")
        print()
        if pilihan == "1":
            persegi()
            print()
        elif pilihan == "2":
            lingkaran()
            print()
        elif pilihan == "3":
            kubus()
            print()
        elif pilihan == "4":
            tabung()
            print()
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak ada")

main()