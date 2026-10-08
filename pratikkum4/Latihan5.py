class Hitung:
    def jumlah(self, a, b, c=None):
        if c is not None:
            return a + b + c
        else:
            return a + b

h = Hitung()
print("Penjumlahan 2 angka (5 + 10):", h.jumlah(5, 10))
print("Penjumlahan 3 angka (5 + 10 + 15):", h.jumlah(5, 10, 15))
