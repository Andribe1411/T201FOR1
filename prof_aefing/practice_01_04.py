import math
x1= float(input("Point 1, x coordinate: "))
y1= float(input("Point 1, y coordinate: "))
x2= float(input("Point 2, x coordinate: "))
y2= float(input("Point 2, y coordinate: "))

distance = math.sqrt(((x1-x2)**2)+((y1-y2)**2))

print(f"The distance between ( {x1} , {y1} ) and ( {x2} , {y2} ) is {distance}")