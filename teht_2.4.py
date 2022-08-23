#Syötteet
luku_1 = int(input("Anna kokonaisluku 1: "))
luku_2 = int(input("Anna kokonaisluku 2: "))
luku_3 = int(input("Anna kokonaisluku 3: "))

#Laskutoimitukset
summa = luku_1 + luku_2 + luku_3
tulo = luku_1 * luku_2 * luku_3
ka = summa / 3 #keskiarvo

#Tulostus
print(f"Summa on {summa}")
print(f"Tulo on {tulo}")
print(f"Keskiarvo on {ka}")