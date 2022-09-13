import mysql.connector

kayttaja = input("Käyttäjä: ")
salasana = input("Salasana: ")

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user=kayttaja,
         password=salasana,
         autocommit=True
         )
maakoodi = input("Anna maakoodi: ")
sql = "SELECT type, COUNT(*) from airport WHERE iso_country = '" + maakoodi + "' GROUP BY TYPE"

kursori = yhteys.cursor()
kursori.execute(sql)

tulos = kursori.fetchall()
for rivi in tulos:
    print(f"{rivi[0]}, {rivi[1]}")