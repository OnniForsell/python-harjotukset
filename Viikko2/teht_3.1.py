min_pituus = 37
kuhan_pituus = float(input("Kuinka pitkän kuhan nappasit?: "))

if kuhan_pituus < min_pituus:
    print(f"Kuhasi on {min_pituus - kuhan_pituus} cm liian pieni")
else:
    print("Wau mikä vonkale")