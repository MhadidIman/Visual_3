import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_penjulan2"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM kategori")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)