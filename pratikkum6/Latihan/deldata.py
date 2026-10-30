from connectiondb import mydb

try:

    mycursor = mydb.cursor()
    sql = "DELETE FROM mahasiswa WHERE nim = %s"
    val = ("456",)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Data berhasil dihapus.")

except Exception as e:
    print(e)

