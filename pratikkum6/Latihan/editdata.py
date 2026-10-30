from connectiondb import mydb

try:

    mycursor = mydb.cursor()
    sql = "UPDATE mahasiswa SET nama = %s WHERE nim = %s"
    val = ("Brian", "789", )
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Data Berhasil diupdate.")

except Exception as e:
    print(e)
