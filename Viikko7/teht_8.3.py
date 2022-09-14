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
def haeKoodi(icao):
    sql = "SELECT latitude_deg, longitude_deg FROM airport Where ident = '"+ icao +"'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

eka=input("Anna ICAO-koodi: ")
eka=eka.upper()
haeKoodi(eka)
toka=input("Anna ICAO-koodi: ")
toka=toka.upper()
haeKoodi(toka)
print(f"pituus asemien välillä on {geodesic(haeKoodi(eka), haeKoodi(toka)).km} km")