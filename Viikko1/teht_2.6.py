import random

pituus = 0
koodi_yks = 3
koodi_kaks = 4

print("Kolmen numeron koodi:")
while pituus < koodi_yks:
    x = random.randint(0, 9)
    print(x)
    pituus += 1
if pituus >= koodi_yks:
    pituus = 0

print("Neljän numeron koodi:")
while pituus < koodi_kaks:
    x = random.randint(1, 6)
    print(x)
    pituus += 1

