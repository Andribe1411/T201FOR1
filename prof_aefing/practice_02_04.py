on = True
largestNumber = -10000000000000000
smallestNumber = 10000000000000000
sum = 0
counter = 0
while on:
    value = input("Value: ")
    if value == "done":
        break
    else:
        value = float(value)
        counter +=1
        sum += value
        if value > largestNumber:
            largestNumber = value
        if value < smallestNumber:
            smallestNumber = value

print("Max:",largestNumber)
print("Min:",smallestNumber)
print("Mean:",sum/counter)