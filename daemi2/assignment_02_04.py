# Author: <Andri Benedikt>
# Date: <22-01-2024>
# Project: <nafn á verkefninu>
# Acknowledgements: <>

lastValue = 0
largestValue = 0
secondLargest = 0

while lastValue >=0:
    lastValue = int(input("Value: "))
    if lastValue >= largestValue:
        secondLargest = largestValue
        largestValue = lastValue
    elif lastValue > secondLargest and lastValue < largestValue:
        secondLargest = lastValue

print("Largest:",largestValue)
print("Second largest:", secondLargest)        