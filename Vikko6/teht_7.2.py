nimet = {"Erkki", "Eero", "Patrik"}

while True:
    nimi = input("Anna Nimi: ")
    if nimi == "":
        break
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
        nimet.add(nimi)
    else:
        print("Uusi Nimi")
        nimet.add(nimi)

for nimi in nimet:
    print(nimi)