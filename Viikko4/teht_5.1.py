import random

nopat = int(input("Kuinka monta noppaa haluat heittää? "))
total = 0

for i in range(nopat):
    a = random.randint(1, 6)
    total += a
    print(a)

print(f"Noppien tulos on {total}")