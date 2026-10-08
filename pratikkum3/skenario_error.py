import math
import os
import zipimport

print("--- Skenario A ---")
try:
    hasil = math.exp(1000)
    print(hasil)
except OverflowError as e:
    print(f"Ditangkap oleh OverflowError: {e}")
except ArithmeticError as e:
    print(f"Ditangkap oleh ArithmeticError: {e}")
except Exception as e:
    print(f"Ditangkap oleh base Exception: {e}")

print("\n--- Skenario B ---")
nama_file = "test_file.txt"
try:
    with open(nama_file, 'w') as f:
        f.write("Halo")
    
    with open(nama_file, 'x') as f:
        f.write("Ditolak")
except FileExistsError as e:
    print(f"Ditangkap oleh FileExistsError: {e}")
except OSError as e:
    print(f"Ditangkap oleh OSError: {e}")
except Exception as e:
    print(f"Ditangkap oleh base Exception: {e}")
finally:
    if os.path.exists(nama_file):
        os.remove(nama_file)

print("\n--- Skenario C ---")
dummy_file = "dummy_test_zip.txt"
try:
    with open(dummy_file, "w") as f:
        f.write("Bukan file zip")
    
    importer = zipimport.zipimporter(dummy_file)
    importer.load_module("modul_dummy")
except zipimport.ZipImportError as e:
    print(f"Ditangkap oleh ZipImportError: {e}")
except ImportError as e:
    print(f"Ditangkap oleh ImportError: {e}")
except Exception as e:
    print(f"Ditangkap oleh base Exception: {e}")
finally:
    if os.path.exists(dummy_file):
        os.remove(dummy_file)
