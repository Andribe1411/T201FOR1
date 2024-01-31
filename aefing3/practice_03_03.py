# Author: <Andri Benedikt>
# Date: <31-01-2024>
# Project: <nafn á verkefninu>
# Acknowledgements: <>
word = input("Write a word: ")
space = " "
for x in range(len(word)):
    print(word[:x+1])
for x in range(len(word)):
    print(space*x,word[x+1:])