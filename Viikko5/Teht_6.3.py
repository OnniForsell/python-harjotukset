def gallonConverter(gallon):
    result = gallon * 3.785
    return result


gallons = float(input("Kuinka monta gallonaa? "))
while gallons > -1:
    liters = gallonConverter(gallons)
    print(f"{liters:.2f} litraa")
    gallons = float(input("Kuinka monta gallonaa? "))
else:
    print("Negatiivinen gallona määrä")