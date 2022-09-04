userInput = (input("Anna numero: "))
minvalue = int(userInput)
maxValue = minvalue

while userInput != "":
    userInput = (input("Anna numero: "))
    if userInput == "":
        break
    userInputInt = int(userInput)

    if int(userInput) < minvalue:
        minvalue = userInputInt
    if int(userInput) > maxValue:
        maxValue = userInputInt

    userInput = (input("Anna numero "))
print(f"Pienin numero on {minvalue} ja suurin numero on {maxValue}")