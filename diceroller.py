import random

dice = [1, 2, 3, 4, 5, 6]
number_of_dice_launched = int(input("Please enter the number of time that you want to launch the dice"))
for i in range(number_of_dice_launched):
    print(random.choice(dice))
    