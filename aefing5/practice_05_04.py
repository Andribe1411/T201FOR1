# Author: <Andri Benedikt>
# Date: <15-02-2024>
# Project: <practice_05_01>
# Acknowledgements: <>

try:
    filename = input('Filename: ')
    input_file = open(filename, 'r')

    max_number = -1000000000000000000
    min_number = 1000000000000000000000000
    sum_number = 0
    number_number = 0
    for line in input_file:
        number = float(line)
        number_number +=1
        sum_number +=number
        if number >max_number:
            max_number = number
        if number < min_number:
            min_number = number
    print("Maximum:",max_number)
    print("Minimum:",min_number)
    print("Average:",sum_number/number_number)





except:
    print("File not found")

