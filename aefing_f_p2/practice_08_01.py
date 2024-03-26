# Author: <Andri Benedikt>
# Date: <21.03.24>
# Project: <practice_08_01>
# Acknowledgements: <>

numbers =[]
while True:
    value = input("")
    try:
        numbers.append(int(value))
    except ValueError:
        break
maxValue = max(numbers)+1
newSet = set(range(1,maxValue))
#print(set(numbers))
#print(newSet)
numbersLeft = newSet - set(numbers)
#print(numbersLeft)
if len(numbersLeft) > 0:
    for x in sorted(numbersLeft):
        print(x)
else:
    print("good job")