class kendaraan:
    
    def __init__(self):
        self.__jenis = ''
        self.__merk = ''
        self.__nama = ''
        self.__warna = ''
    
    def set_atribut(self, jenis='', merk='', nama='', warna=''):
        self.__jenis = jenis
        self.__merk = merk
        self.__nama = nama
        self.__warna = warna

    def get_atribut(self):
        print("\nJenis :", self.__jenis,
              "\nMerk :", self.__merk,
              "\nNama :", self.__nama,
              "\nWarna :", self.__warna)

brio = kendaraan()
brio.set_atribut(jenis='Mobil', warna='Merah')
brio.get_atribut()

vario = kendaraan()
vario.set_atribut(merk='Honda', warna='Hitam')
vario.get_atribut()