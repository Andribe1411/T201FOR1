# Author: <Andri Benedikt>
# Date: <09-02-2024>
# Project: <practice_04_01>
# Acknowledgements: <>

def changeString(string):
    newString = string[-1]+string[1:-1]+string[0]
    return newString

print(changeString(input("Write a word: ")))