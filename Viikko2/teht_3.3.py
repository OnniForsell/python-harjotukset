# Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

gender = input("Sukupuolesi (nainen/mies)? ")

if gender == "nainen":
    hg_value = int(input("Hemoglobiinisi (g/l)? "))
    # testataan arojen järkevyys
    if not (5 < hg_value < 300):
        print("Virellinen hg-arvo!")
    #Testataan naisen ohjearvoja vastaan
    elif hg_value < 117:
        print("Hemoglobiiniarvo on alhainen")
    elif hg_value <= 175:
        print("Hemoglobiiniarvo normaali")
    else:
        print("Hemoglobiiniarvo on korkea")
        
elif gender == "mies":
    hg_value = int(input("Hemoglobiinisi (g/l)? "))
    #Testataan miehen ohjearvoja vastaan
    if hg_value < 134:
        print("Hemoglobiiniarvo on alhainen")
    elif hg_value <= 195:
        print("Hemoglobiiniarvo normaali")
    else:
        print("Hemoglobiiniarvo on korkea")