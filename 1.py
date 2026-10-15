class Produk():
    def __init__(self, id='', nama='', harga=0):
        self.id_produk = id
        self.nama_produk = nama
        self.harga_produk = harga

class TransaksiPesanan():
    def __init__(self, id_trx='', jml=0, produk=None):
        self.id_transaksi = id_trx
        self.jumlah_produk = jml
        self.produk = produk
    
    def cetak_struk(self):
        print('ID Transaksi:', self.id_transaksi)
        print('Nama Produk:', self.produk.nama_produk)
        print('Jumlah Produk:', self.jumlah_produk)
        print('Total Harga:', self.jumlah_produk * self.produk.harga_produk)
        print('-' * 30)

prod1 = Produk('K001', 'Keyboard', 50000)
prod2 = Produk('M001', 'Mouse', 25000)

trx1 = TransaksiPesanan('TRX001', 2, prod1)
trx2 = TransaksiPesanan('TRX002', 3, prod2)

trx1.cetak_struk()
trx2.cetak_struk()

    