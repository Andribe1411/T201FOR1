# Author: <Andri Benedikt>
# Date: <14-02-2024>
# Project: <assignment_03_02>
# Acknowledgements: <>
def is_even(number):
    if number % 2:
        return False
    else:
        return True

def more_less(odd,even):
    if odd > even:
        print("More odd than even numbers")
    elif odd < even:
        print("More even than odd numbers")
    else:
        print("Equal number of odd and even numbers")

try:
    evenCounter = 0
    oddCounter = 0
    filename = input('Filename: ')
    input_file = open(filename, 'r')
    for line in input_file:
        if is_even(int(line)):
            evenCounter +=1
        else:
            oddCounter +=1
    input_file.close()
    more_less(oddCounter,evenCounter)

except:
    print("Can't open the file",filename)