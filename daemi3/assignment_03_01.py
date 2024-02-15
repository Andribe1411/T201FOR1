# Author: <Andri Benedikt>
# Date: <14-02-2024>
# Project: <assignment_03_01>
# Acknowledgements: <>
try:
    filename = input('Filename: ')
    input_file = open(filename, 'r')
    longestWord = ""
    for line in input_file:
        splitFile = line.strip().split(" ")
        for x in splitFile:
            if len(x) > len(longestWord):
                longestWord = x
    input_file.close()
    print(longestWord)
    print(len(longestWord), "letters")
except:
    print("File not found")