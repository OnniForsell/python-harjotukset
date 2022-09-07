import random


def dicethrower():
    dice_value = random.randint(1, 6)
    return dice_value

while True:
    dice_result = dicethrower()
    print(dice_result)
    if dice_result == 6:
        break
