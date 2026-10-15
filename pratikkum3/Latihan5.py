class SaldoTidakMencukupiError(Exception):
    pass

class NominalTidakValidError(Exception):
    pass

saldo = 500000
print("--- ATM Sederhana ---")

while True:
    print(f"\nSaldo saat ini: Rp{saldo}")
    nominal_input = input("Masukkan nominal tarik tunai (ketik 'keluar' untuk selesai): ")
    
    if nominal_input.strip().lower() in ['keluar', 'exit', 'q']:
        print("Terima kasih telah menggunakan ATM.")
        break
        
    try:
        try:
            nominal = int(nominal_input)
        except ValueError:
            raise ValueError("Nominal yang dimasukkan bukan angka.")
            
        if nominal <= 0:
            raise NominalTidakValidError("Nominal kurang dari atau sama dengan 0.")
            
        if nominal > saldo:
            raise SaldoTidakMencukupiError("Saldo tidak mencukupi.")
            
        saldo -= nominal
        print(f"Tarik tunai berhasil. Sisa saldo: Rp{saldo}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except NominalTidakValidError as e:
        print(f"Error: {e}")
    except SaldoTidakMencukupiError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error tak terduga: {e}")
