# Author: <Andri Benedikt>
# Date: <22-01-2024>
# Project: <nafn á verkefninu>
# Acknowledgements: <>

lose = [2,3,12]
win = [7,11]
dice1 = int(input("Dice 1: "))
dice2 = int(input("Dice 2: "))
sumOfDice = dice1+dice2
if dice1 > 6 or dice2 > 6 or dice1 < 1 or dice2 < 1:
    print("Illegal input")
elif sumOfDice in win:
    print("Winner!")
elif sumOfDice in lose:
    print("Loser!")
else:
    print(sumOfDice)