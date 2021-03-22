import mysql.connector
cnx = mysql.connector.connect(
    user='root',
    password='Welkom01',
    host='172.17.0.3',
    database='pad')

cursor = cnx.cursor()

query = """SELECT naam, wachtwoord
    FROM Speler
    WHERE naam = %(naam)s"""

cursor.execute(query,{"naam": "klaas"})

for id_Naam, Wachtwoord in cursor:
    print("Naam:", id_Naam, "\nWachtwoord:", Wachtwoord)

cnx.commit()
cursor.close
cnx.close()