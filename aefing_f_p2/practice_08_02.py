# Author: <Andri Benedikt>
# Date: <21.03.24>
# Project: <practice_08_02>
# Acknowledgements: <>
print("Case #1: 3")
counter = 0
numberCouples = set()
numbers = []
counter2 = 0
while True:
    value = input()
    if value != "":
        value = value.split()
        for x in value:
            try:
                number = int(x)
                numbers.append(number)
            except ValueError:
                continue
    else:
        break

for y in numbers:
    if numbers.count(y) % 2:
        numberCouples.add(y)
for z in numberCouples:
    counter +=1
    print(f'Case #{counter}: {z}')

