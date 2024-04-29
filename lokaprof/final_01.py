# Author: <Andri Benedikt>
# Date: <19.04.24>
# Project: <Lokapróf D1>

on = True
numbers = []
while on:
    value = input("Number: ")
    if value == "quit":
        on = False
    try:
        number = int(value)
        numbers.append(number)
    except:
        continue

numbers.sort()
print("All: ",end="")
for loc,num in enumerate(numbers):
    if loc == len(numbers)-1:
        print(num)
    else:
        print(num,end=", ")

print("Unique: ",end="")
unique_numbers = list(set(numbers))
unique_numbers.sort()
for loc,num in enumerate(unique_numbers):
    if loc == len(unique_numbers)-1:
        print(num)
    else:
        print(num,end=", ")

