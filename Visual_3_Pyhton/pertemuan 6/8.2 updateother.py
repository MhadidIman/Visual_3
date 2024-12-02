import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_penjulan2"
)

mycursor = mydb.cursor()
sql = "UPDATE kategori SET name= %s where id = %s"
adr = ("Roiad","3")
mycursor.execute(sql,adr)

mydb.commit()
print(mycursor.rowcount,"record(s) Updated")