#Kysytään Tiedot
kanta = float(input("Anna suorakulmion kanta "))
korkeus = float(input("Anna suorakulmion korkeus "))

# laskutoimitukset
A = kanta * korkeus
piiri = (kanta * 2) + (korkeus * 2)

print(f"Ala = {A}")
print(f"Piiri = {piiri}")