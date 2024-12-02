import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_penjulan2"
)

mycursor = mydb.cursor()
sql = "INSERT INTO Kategori (id, name) VALUES (%s, %s)"
val = ("5","Roti")
mycursor.execute(sql, val)

mydb.commit()
print(mycursor.rowcount, "1 record insert, ID:", mycursor.lastrowid)