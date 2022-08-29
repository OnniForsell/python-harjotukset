import math

leiviskä = float(input("Anna leiviskä: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))

grammaa = (luoti * 13.3) + (naula * 32 * 13.3) + (leiviskä * 20 * 32 * 13.3)
kilot = math.floor(grammaa/1000)
loput = grammaa - math.floor(kilot * 1000)

print(f"Massa nykymittojen mukaan on {kilot} kiloa ja {loput:0.2f} grammaa.")
