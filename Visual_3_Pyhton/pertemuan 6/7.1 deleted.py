import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_penjulan2"
)

mycursor = mydb.cursor()
sql = "SELECT * FROM kategori where id = '2'"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(mycursor.rowcount,"record(s) deleted")