# Author: <Andri Benedikt>
# Date: <22-01-2024>
# Project: <nafn á verkefninu>
# Acknowledgements: <>

def isPrime(number):
    prime = True
    for i in range(2,number):
        if number % i == 0:
            prime = False
    return prime

n = int(input("Write a positive integer n: "))
if n < 0:
    print("positive integer only please")
else:
    nPow2 = n**2
    nPlus1Pow2 = (n+1)**2
    print("Prime numbers between ",nPow2," and ",nPlus1Pow2,":", sep="")
    for x in range(nPow2,nPlus1Pow2):
        if isPrime(x):
            print(x)