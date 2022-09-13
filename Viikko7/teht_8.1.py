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

#Määritellään kysely
icao = input("Anna IACO koodi: ")
sql = "SELECT name, municipality FROM airport Where ident = '"+ icao +"'"
print(sql)

#Suoritetaan kysely
kursori = yhteys.cursor()
kursori.execute(sql)

#Haetaan ja käsitellään tulosrivit
tulos = kursori.fetchall()
for rivi in tulos:
    print(f"{rivi[0]}, {rivi[1]}")