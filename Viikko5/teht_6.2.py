import random


def dicethrower(dMax):
    dice_result = random.randint(1, dMax)
    return dice_result

diceSize = int(input("Kuinka monta sivua nopassasi on? "))

while True:
    dice_result = dicethrower(diceSize)
    print(dice_result)
    if dice_result == diceSize:
        break
