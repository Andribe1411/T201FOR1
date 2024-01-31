# Author: <Andri Benedikt>
# Date: <31-01-2024>
# Project: <nafn á verkefninu>
# Acknowledgements: <>

sentance = input("Write a sentence: ")

for x, y in enumerate(sentance):
    if y == "e":
        print(x)