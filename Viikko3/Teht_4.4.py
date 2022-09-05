import random

num = random.randint(1, 10)
arvaus = int(input("Arvaa numero 1 ja 10 välillä: "))

while arvaus != num:
    if arvaus < num:
        print("Liian pieni")
    else:
        print("Liian suuri")
    arvaus = int(input("Arvaa numero 1 ja 10 välillä: "))

print(f"{arvaus} on oikea vastaus")