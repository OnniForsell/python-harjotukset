from flask import Flask, Response
import mysql.connector
import json

# salasana = input("Salasana: ")

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='gutpo80',
         autocommit=True
         )

app = Flask(__name__)
@app.route('/kenttä/<ident>')
def kenttä(ident):
    try:
        def get_name(icao):
            sql = "SELECT name FROM airport Where ident = '" + icao + "'"
            kursori = yhteys.cursor()
            kursori.execute(sql)
            tulos = kursori.fetchall()
            return tulos[0]

        def get_municipality(icao):
            sql = "SELECT municipality FROM airport Where ident = '" + icao + "'"
            kursori = yhteys.cursor()
            kursori.execute(sql)
            tulos = kursori.fetchall()
            return tulos[0]

        tilakoodi = 200
        vastaus = {
            "status": tilakoodi,
            "ICAO": ident,
            "Name": get_name(ident)[0],
            "Municipality": get_municipality(ident)[0]
        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen ICAO koodi"
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status" : "404",
        "teksti" : "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)