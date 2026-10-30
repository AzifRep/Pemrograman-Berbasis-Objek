from connectiondb import mydb

try:
    mycursor = mydb.cursor()
    sql = "INSERT INTO mahasiswa (nim, nama, jurusan, umur) VALUES (%s, %s, %s, %s)"
    val = [
        ('123', 'budi', 'informatika', 20),
        ('456', 'dola', 'electro', 19),
        ('789', 'susanto', 'mesin', 21)
    ]
    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Data berhaasil ditambahkan..." )
except Exception as e:
    print(e)