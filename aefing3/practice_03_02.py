# Author: <Andri Benedikt>
# Date: <31-01-2024>
# Project: <nafn á verkefninu>
# Acknowledgements: <>

upperRange = int(input("Upper number for the range: "))


for x in range(1,upperRange+1):
    summa = 0
    for y in range(1,x):
        if x % y == 0:
            #print(x," - ", y)
            summa += y
    if x == summa:
        print(x)