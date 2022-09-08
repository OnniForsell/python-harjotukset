import math

def pizzaLaskin(halk, hin):
    säde = halk / 2
    pinta_ala = math.pi * säde ** 2
    pizzanHinta = hin / pinta_ala
    return pizzanHinta

halkaisija = int(input("Kuinka monta senttiä on pizzan halkaisija? "))
hinta = float(input("Kuinka monta euroa se maksaa? "))
pizzaYks = pizzaLaskin(halkaisija, hinta)

halkaisija = int(input("Kuinka monta senttiä on pizzan halkaisija? "))
hinta = float(input("Kuinka monta euroa se maksaa? "))
pizzaKaks = pizzaLaskin(halkaisija, hinta)

if pizzaYks < pizzaKaks:
    print("Pizza 1 on edullisempi")
else:
    print("Pizza 2 on edullisempi")