import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_penjulan2"
)

mycursor = mydb.cursor()
sql = "INSERT INTO Kategori (id, name) VALUES (%s, %s)"
val = ("2","Drinks")
mycursor.execute(sql, val)

mydb.commit()
print(mycursor.rowcount, "Data Berhasil Ditambahkan.")