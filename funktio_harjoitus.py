#def toinenFunktio():
 #   print("Ollaan toisessa funktiossa")


#def tervehdi(henkilöNimi):
 #   print(f"Moi {henkilöNimi}!")
  #  print("Tämä on tervehdys funktiosta.")
   # toinenFunktio()
    #return


def laskeKolmionAla(kanta, korkeus):
    a = (kanta * korkeus) / 2
    #print(f"Kolmion ala on {a:.2f}")
    return a


ka = float(input("Anna kolmion kanta "))
ko = float(input("Anna kolmion korkeus "))
pintaAla = laskeKolmionAla(ka, ko)
print(f"Kolmion ala on {pintaAla:.2f}")

#nimi = input("Mikä on nimesi? ")
#tervehdi(nimi)

#print("Ollaan pääohjelmassa")
#tervehdi(nimi)
#print("Ollaan takaisin pääohjelmassa")
#tervehdi(nimi)
#tervehdi(nimi)
#print("ebin, ohjelma loppu :DD")
