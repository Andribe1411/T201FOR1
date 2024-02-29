import math

def findPrime(number):
#number = int(input("Write a number: "))
    isPrime = True
    for i in range(2,number):
        if number % i == 0:
            isPrime = False
    if number ==1:
        isPrime = False
    return isPrime
