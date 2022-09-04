nimi = "Python"
salasana = "Rules"

kenttaYks = input("Käyttäjänimi: ")
kenttaKaks = input("Salasana: ")
arvauksia = 1

while arvauksia != 5:
    if kenttaYks == nimi and kenttaKaks == salasana:
        break
    elif kenttaYks != nimi and kenttaKaks == salasana:
        print("Väärä Käyttäjänimi")
    elif kenttaKaks != salasana and kenttaYks == nimi:
        print("Väärä Salasana")
    elif kenttaYks != nimi and kenttaKaks != salasana:
        print("Väärä käyttäjänimi ja salasana")

    kenttaYks = input("Käyttäjänimi: ")
    kenttaKaks = input("Salasana: ")
    arvauksia += 1

if arvauksia == 5:
    print("Pääsy evätty")
else:
    print("Tervetuloa")