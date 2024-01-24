# Author: <Andri Benedikt>
# Date: <22-01-2024>
# Project: <nafn á verkefninu>
# Acknowledgements: <>

isNegative = False

number = int(input("Write a number: "))
isPrime = True
for i in range(2,number):
    if number % i == 0:
        isPrime = False
if number <0:
    isNegative = True

if isPrime == False and isNegative == False:
    print(number,"is not a prime number")
elif isNegative == False:
    print(number,"is a prime number")
elif isNegative == True:
    print("Illegal input")