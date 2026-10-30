from connectiondb import mydb

print(mydb)

try:
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE kampus1")
except Exception as e:
    print(e)