import mysql.connector
cnx = mysql.connector.connect(
    user='root',
    password='Welkom01',
    host='172.17.0.3',
    database='pad')

cursor = cnx.cursor()

query = """SELECT username, password
    FROM Speler
    WHERE username = %(username)s"""

cursor.execute(query,{"username": "test"})

for id_Username, password in cursor:
    print("Username:", id_Username, "\nPassword:", password)

cnx.commit()
cursor.close
cnx.close()