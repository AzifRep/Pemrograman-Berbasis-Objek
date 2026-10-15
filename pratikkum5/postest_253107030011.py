class Item():
    def __init__(self, Code=0, Title='', Description='', Category='', Picture='', QuantityInStock=0, Price=0):
        self.Code = Code
        self.Title = Title
        self.Description = Description
        self.Category = Category
        self.Picture = Picture
        self.QuantityInStock = QuantityInStock
        self.Price = Price
    
    def viewFullDescription(self):
        pass
    def addToCart():
        pass
    def updateStockLevel():
        pass

class DVD(Item):
    def __init__(self, Director='', Certificate='', ListofActor='', Code=0, Title='', Description='', Category='', Picture='', QuantityInStock=0, Price=0):
        super().__init__(Code, Title, Description, Category, Picture, QuantityInStock, Price)
        self.Director = Director
        self.Certificate = Certificate
        self.ListofActor = ListofActor

class MP3(Item):
    def __init__(self, Duration='', Artist='', Code=0, Title='', Description='', Category='', Picture='', QuantityInStock=0, Price=0):
        super().__init__(Code, Title, Description, Category, Picture, QuantityInStock, Price)
        self.Duration = Duration
        self.Artist = Artist

    def playExtract(self):
        pass
    def download(self):
        pass

class Book(Item):
    def __init__(self, ISBN=0, Author='', Synopsis='', Code=0, Title='', Description='', Category='', Picture='', QuantityInStock=0, Price=0):
        super().__init__(Code, Title, Description, Category, Picture, QuantityInStock, Price)
        self.ISBN = ISBN
        self.Author = Author
        self.Synopsis = Synopsis
    
    def preview(self):
        pass

dvd = DVD(
    'Joko Anwar',
    'Dewasa',
    'Rafi, Joko, Bayu',
    1,
    'PalangKaraya',
    'Kota Terbaik',
    'Kota',
    'GambarKota',
    10,
    15000
)
mp3 = MP3(
    '1 Jam',
    'Joko Kendil',
    2,
    'PalangKaraya',
    'Kota Terbaik',
    'Kota',
    'GambarKota',
    10,
    15000
)
buku = Book(
    1576,
    'Joko Anwar',
    'PalangKaraya Keindahan Alam',
    3,
    'PalangKaraya',
    'Kota Terbaik',
    'Kota',
    'GambarKota',
    10,
    15000
)
