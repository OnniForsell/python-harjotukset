import random

sisalla = 0
i = 0
num = int(input("Kuinka monta pistettä pitäisi arvata? "))

while i <= num:
    x = random.randint(-1, 1)
    y = random.randint(-1, 1)
    if (x ^ 2 + y ^ 2) <= 1:
        sisalla += 1
    i += 1

pi = 4 * sisalla / num
print(f"Piin likiarvo on noin {pi}")
