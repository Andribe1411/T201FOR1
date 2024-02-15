# Author: <Andri Benedikt>
# Date: <14-02-2024>
# Project: <assignment_03_03>
# Acknowledgements: <>

def open_file(filename):
    try:
        return open(filename, 'r')
    except:
        print("File not found")

def close_file(file):
    file.close()


filename_input = input('Filename: ')
input_file = open_file(filename_input)
char_counter = 0
line_counter = 0

for line in input_file:
    splitFile = line.split()
    line_counter +=1
    for x in splitFile:
        if x.isspace() == False:
            for y in x:
                char_counter +=1
close_file(input_file)
print("Lines: ",line_counter,", characters: ",char_counter,sep="")