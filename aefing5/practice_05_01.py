# Author: <Andri Benedikt>
# Date: <15-02-2024>
# Project: <practice_05_01>
# Acknowledgements: <>

try:
    filename = input('Filename: ')
    input_file = open(filename, 'r')
    print(input_file.read())
    input_file.seek(2)
    print(input_file.read())
except:
    print("File not found")