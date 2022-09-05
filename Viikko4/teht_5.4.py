kaupungit = []
kysymyksia = 5

for kysymys in range(kysymyksia):
    userInput = input("Anna kaupungin nimi: ")
    kaupungit.append(userInput)

for k in kaupungit:
    print(k)
