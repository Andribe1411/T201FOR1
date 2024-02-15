# Author: <Andri Benedikt>
# Date: <09-02-2024>
# Project: <practice_04_04>
# Acknowledgements: <>

vowels = ["a","i","e","o","u"]
word = input("Write a word: ")

newWord = ""
tempstring = ""
counter = 0

if word[0] in vowels:
    newWord = word+"yay"
else:
    for x in word:
        if x not in vowels:
            tempstring  = tempstring+x
        elif x in vowels:
            newWord = newWord + word[counter:len(word)]
            break
        counter += 1
    newWord += tempstring + "ay"

print(newWord)
