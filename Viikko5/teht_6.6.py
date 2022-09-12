import math
def pizzaLaskin(halk, hin):
    säde = halk / 2
    pinta_ala = math.pi * säde ** 2
    pizzanHinta = hin / pinta_ala
    return pizzanHinta

pizzat = []
pizzaRange = int(input("Kuinka monta pizzaa? "))
for x in range(pizzaRange):
    halkaisija = int(input("Kuinka monta senttiä on pizzan halkaisija? "))
    hinta = float(input("Kuinka monta euroa se maksaa? "))
    pizzat.append(pizzaLaskin(halkaisija, hinta))

arvokkain = 0
for x in range(len(pizzat)):
    if pizzat[arvokkain] > pizzat[x]:
        arvokkain = x

print(f"Edullisin pizza on pizza {arvokkain+1} ")