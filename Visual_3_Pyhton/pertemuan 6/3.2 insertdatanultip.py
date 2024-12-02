import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_penjulan2"
)

mycursor = mydb.cursor()
sql = "INSERT INTO KATEGORI (id, name) VALUES (%s, %s)"
val = [("3","Drinks"),("4","Tepung")]
mycursor.executemany(sql, val)

mydb.commit()
print(mycursor.rowcount, "DATA BERHASIL DITAMBAHKAN.")
