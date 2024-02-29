# Author: <Andri Benedikt>
# Date: <15-02-2024>
# Project: <practice_05_01>
# Acknowledgements: <>

try:
    filename = input('Filename: ')
    word = input("Word: ")
    input_file = open(filename, 'r')
    line_counter = 0
    word_counter = 0
    for line in input_file:
        line_counter +=1
    
        if word.lower() in line.lower():
            word_counter +=1
    print("Lines:",line_counter)
    print(f'Lines containing the word "{word.lower()}": {word_counter}')




except:
    print("Invalid filename")

