# Author: <Andri Benedikt>
# Date: <09-02-2024>
# Project: <practice_04_03>
# Acknowledgements: <>

def findDigits(string):
    newString = ""
    for x in string:
        if x.isdigit():
            newString += x
    return newString


inputString = input("Input: ")
print(findDigits(inputString))
