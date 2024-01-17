# Author: <Andri Benedikt>
# Date: <17.01.24>
# Project: <Æfingarverkefni 1>
# Acknowledgements: <ef þú þáðir eða veittir aðstoð þá á það>
# <að vera tekið fram hér>
import math
x1 = int(input("Point 1, x coordinate:"))
y1 = int(input("Point 1, y coordinate:"))
x2 = int(input("Point 2, x coordinate:"))
y2 = int(input("Point 2, y coordinate:"))
distance = math.sqrt(((x1-x2)**2)+((y1-y2)**2))
print("The distance between ( ",x1," , ",y1," ) and ( ",x2, "," ,y2," ), is",distance)