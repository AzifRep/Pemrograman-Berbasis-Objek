import datetime
from user import User
from barang import Barang

def greeting():
    print("-" * 40)
    print("SELAMAT DATANG DI APLIKASI KASIR APOTEK")
    print("-" * 40)

def menu_admin():
    print("\n>> Menu Admin")
    print("1) Lihat data user\n2) Tambah data user\n3) Edit data user\n4) Delete data user\n5) Logout")

def menu_kasir():
    print("\n>> Menu Kasir")
    print("1) Lihat data barang\n2) Tambah data barang\n3) Edit data barang\n4) Delete data barang\n5) Logout")

def login():
    print("\nSilahkan masukkan username dan password")
    usernamelogin = input("Username : ")
    passwordlogin = input("Password : ")
    level_login = usr.login(usernamelogin, passwordlogin)
    return level_login, usernamelogin

usr = User()
brg = Barang()
greeting()

try:
    level_login, current_user = login()
    usr.log(datetime.datetime.now(), current_user, "Login")
    menu_berlanjut = True

    while menu_berlanjut:
        if level_login == "Admin":
            menu_admin()
            menu = int(input("Masukkan menu yang Anda inginkan: "))
            if menu == 1:
                usr.select_data()
                usr.log(datetime.datetime.now(), current_user, "Melihat data user")
            elif menu == 2:
                nama_baru = input("Masukkan nama : ")
                username_baru = input("Masukkan username : ")
                password_baru = input("Masukkan password : ")
                level_baru = input("Masukkan level : ")
                usr.insert_data(nama_baru, username_baru, password_baru, level_baru)
                usr.log(datetime.datetime.now(), current_user, f"Menambahkan user baru {username_baru}")
                usr.select_data()
            elif menu == 3:
                username = input("Masukkan username data yang akan diganti : ")
                nama_baru = input("Masukkan nama : ")
                password_baru = input("Masukkan password : ")
                level_baru = input("Masukkan level : ")
                usr.update_data(nama_baru, password_baru, level_baru, username)
                usr.log(datetime.datetime.now(), current_user, f"Mengubah data user {username}")
                usr.select_data()
            elif menu == 4:
                username = input("Masukkan username data yang akan dihapus : ")
                usr.log(datetime.datetime.now(), current_user, f"Menghapus data user {username}")
                usr.delete_data(username)
                usr.select_data()
            elif menu == 5:
                usr.log(datetime.datetime.now(), current_user, "Logout")
                level_login, current_user = login()
                usr.log(datetime.datetime.now(), current_user, "Login")
            else:
                menu_berlanjut = False

        elif level_login == "Kasir":
            menu_kasir()
            menu = int(input("Masukkan menu yang Anda inginkan: "))
            if menu == 1:
                brg.select_data()
                brg.log(datetime.datetime.now(), current_user, "Melihat data barang")
            elif menu == 2:
                id_baru = input("Masukkan id : ")
                nama_baru = input("Masukkan nama : ")
                stok_baru = input("Masukkan stok : ")
                harga_baru = input("Masukkan harga : ")
                kategori_baru = input("Masukkan kategori : ")
                brg.insert_data(id_baru, nama_baru, stok_baru, harga_baru, kategori_baru)
                brg.log(datetime.datetime.now(), current_user, f"Menambahkan data barang baru {nama_baru} ID {id_baru}")
                brg.select_data()
            elif menu == 3:
                id = input("Masukkan id data yang akan diganti : ")
                nama_baru = input("Masukkan nama : ")
                stok_baru = input("Masukkan stok : ")
                harga_baru = input("Masukkan harga : ")
                kategori_baru = input("Masukkan kategori : ")
                brg.update_data(nama_baru, stok_baru, harga_baru, kategori_baru, id)
                brg.log(datetime.datetime.now(), current_user, f"Mengubah data barang dengan ID {id} menjadi {nama_baru}")
                brg.select_data()
            elif menu == 4:
                id = input("Masukkan id data yang akan dihapus : ")
                brg.log(datetime.datetime.now(), current_user, f"Menghapus data barang ID {id}")
                brg.delete_data(id)
                brg.select_data()
            elif menu == 5:
                brg.log(datetime.datetime.now(), current_user, "Logout")
                level_login, current_user = login()
                brg.log(datetime.datetime.now(), current_user, "Login")
            else:
                menu_berlanjut = False

except Exception as e:
    print(e)
