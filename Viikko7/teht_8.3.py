from geopy.distance import geodesic
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
icao1 = input("Anna IACO koodi: ")
sql1 = "SELECT latitude_deg, longitude_deg FROM airport Where ident = '"+ icao1 +"'"

#Suoritetaan kysely
kursori = yhteys.cursor()
kursori.execute(sql1)

#Haetaan ja käsitellään tulosrivit
tulos1 = kursori.fetchall()

icao2 = input("Anna IACO koodi: ")
sql2 = "SELECT longitude_deg, latitude_deg FROM airport Where ident = '"+ icao2 +"'"

#Suoritetaan kysely
kursori = yhteys.cursor()
kursori.execute(sql2)

#Haetaan ja käsitellään tulosrivit
tulos2 = kursori.fetchall()

print(f"pituus asiemien välillä on {geodesic(tulos1, tulos2).km} km")