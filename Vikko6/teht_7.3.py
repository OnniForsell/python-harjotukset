def valitse():
    print("1 - Syötä uusi")
    print("2 - Haku")
    print("0 - Lopetus")
    valinta = -1
    while valinta < 0 or valinta > 2:
        valinta = int(input("Valitse: "))
        return valinta

def lisaaUusi(asema):
    icao = input("Aseman ICAO koodi: ")
    nimi = input("Aseman nimi: ")
    asema[icao] = nimi

def hae(asema):
    icao = input("Aseman ICAO koodi: ")
    if icao in asema:
        print(asema[icao])
    else:
        print("Tuntematon ICAO koodi")

lentoasemat = {}
valinta = valitse()
while valinta != 0:
    if valinta == 1:
        lisaaUusi(lentoasemat)
    elif valinta == 2:
        hae(lentoasemat)
    valinta = valitse()