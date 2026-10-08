class AkunBank:
    def __init__(self, nama, saldo=0):
        self.nama = nama
        self.__saldo = saldo

    def lihat_saldo(self):
        print(f"Saldo {self.nama}: Rp {self.__saldo}")

    def setor_uang(self, nominal):
        if nominal > 0:
            self.__saldo += nominal
            print(f"Berhasil setor: Rp {nominal}. Saldo sekarang: Rp {self.__saldo}")
        else:
            print("Nominal setor harus lebih dari 0!")

akun = AkunBank("Budi", 500000)
print("Nama pemilik akun (public):", akun.nama)
akun.lihat_saldo()
akun.setor_uang(200000)

try:
    print(akun.__saldo)
except AttributeError as e:
    print("Atribut private tidak dapat diakses langsung:", e)
