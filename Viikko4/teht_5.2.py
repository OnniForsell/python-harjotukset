numbers = []
readingNumbers = True

while readingNumbers:
    strInput = input("Anna numero: ")
    if strInput == "":
        readingNumbers = False
    else:
        numbers.append(int(strInput))
print(numbers)
ordered = numbers.sort(reverse=True)
print(numbers[:5])
for n in numbers[0:5]:
    print(n)