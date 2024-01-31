# Author: <Andri Benedikt>
# Date: <31-01-2024>
# Project: <nafn á verkefninu>
# Acknowledgements: <>

rows = int(input("Size of board - rows: "))
columns = int(input("Size of board - columns: ")) 
xCord = int(input("x coordinate of player: "))
yCord = int(input("y coordinate of player: "))
if xCord > columns or yCord > rows or xCord < 1 or yCord < 1:
    print("Illegal player coordinates")
else:
    dotString = "."*columns
    print("/","-"*columns,"\u005C",sep="")
    for x in range(rows):
        if x == rows-yCord:
            print("|",dotString[:xCord-1],"@",dotString[xCord:],"|",sep="")
        else:
            print("|",dotString,"|",sep="")
    print("\u005C","-"*columns,"/",sep="")