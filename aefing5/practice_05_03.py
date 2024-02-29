# Author: <Andri Benedikt>
# Date: <15-02-2024>
# Project: <practice_05_01>
# Acknowledgements: <>

try:
    filename = input('Filename: ')
    input_file = open(filename, 'r')
    text = ""
    for line in input_file:
        for x in line:
            if x.isspace() == False:
                text += x
                
    print(text)

except:
    print("Invalid filename")

