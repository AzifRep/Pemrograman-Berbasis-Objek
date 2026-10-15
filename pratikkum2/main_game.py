from game.Sound import load as loadSound
from game.Sound import pause
from game.Sound import play
from game.Level import load as loadLevel
from game.Level import over
from game.Level import start
from game.Image import open
from game.Image import close
from game.Image import change

def konfirmasi():
    while True:
        pilihan = input("Apakah anda ingin lanjut? (y/n): ")
        if pilihan == 'y':
            return True
        elif pilihan == 'n':
            return False
        else:
            print("Pilihan tidak ada")

while True:
    print("1. loadSound")
    print("2. pause")
    print("3. play")
    print("4. over")
    print("5. start")
    print("6. open")
    print("7. close")
    print("8. change")
    
    pilihan = input("Masukkan angka: ")
    print()
    if pilihan == '1':
        print(loadSound.info())
        konfirmasi()
        print()
    elif pilihan == '2':
        print(pause.info())
        konfirmasi()
        print()
    elif pilihan == '3':
        print(play.info())
        konfirmasi()
        print()
    elif pilihan == '4':
        print(over.info())
        konfirmasi()
        print()
    elif pilihan == '5':
        print(start.info())
        konfirmasi()
        print()
    elif pilihan == '6':
        print(open.info())
        konfirmasi()
        print()
    elif pilihan == '7':
        print(close.info())
        konfirmasi()
        print()
    elif pilihan == '8':
        print(change.info())
        konfirmasi()
        print()
    else:
        print("Pilihan tidak ada")
