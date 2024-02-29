# Author: <Andri Benedikt>
# Date: <23-02-2024>
# Project: <mt_01_02>
def open_file(file):
    try:
        input_file = open(file, 'r')
        return input_file
    except:
        print(f"Can't open the file {file}")
        return None
    
#def find_precentage(counter,total):
    #return round(counter/total*20)

upper_counter = 0
lower_counter = 0
space_counter = 0
total_counter = 0
testcase = 0
filename = input('Filename: ')
input_file = open_file(filename)
if input_file != None:
    for line in input_file:
        for character in line:
            total_counter+=1
            if character.isupper():
                upper_counter+=1
            elif character.islower():
                lower_counter+=1
            elif character.isspace():
                space_counter+=1
            else:
                testcase+=1
    print(total_counter,"with counter")
    total_counter = upper_counter+lower_counter+space_counter
    print(total_counter,"upper+lower+space",testcase)
    print("Upper:","X"*(round(upper_counter/total_counter*20)))
    print("Lower:","X"*(round(lower_counter/total_counter*20)))
    print(lower_counter/total_counter)
    print("Space:","X"*(round(space_counter/total_counter*20)))
