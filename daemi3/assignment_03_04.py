# Author: <Andri Benedikt>
# Date: <14-02-2024>
# Project: <assignment_03_04>
# Acknowledgements: <GPT hjálpaði mér að skilja hvernig á að greina á milli float og int>

def open_file(filename):
    try:
        return open(filename, 'r')
    except:
        print("File not found")

def close_file(file):
    file.close()

def convert_to_number(value):
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            pass


filename_input = input('Filename: ')
input_file = open_file(filename_input)
for line in input_file:
    splitFile = line.strip()
        #print(splitFile)
    number = convert_to_number(splitFile)
    if number != None:
        print(number)


        
