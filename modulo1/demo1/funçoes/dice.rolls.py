
import random

def roll_dice(num_dice):
    dice = (1,2,3,4,5,6)
    rolls = []

    for _ in range(num_dice):
        rolls.append(random.choice(dice))
        
        
    return rolls


num_dice = int(input("Enter the number of dice roll: "))
dice_rolls = roll_dice(num_dice)
total_sum = sum(dice_rolls)
print("dice rolls: ", dice_rolls)
print("total sum: ", total_sum)


