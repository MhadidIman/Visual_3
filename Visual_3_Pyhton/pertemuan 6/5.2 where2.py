import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_penjulan2"
)

mycursor = mydb.cursor()
sql = "SELECT * FROM kategori where id = %s"
no = ("3",)
mycursor.execute(sql,no)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)