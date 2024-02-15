# Author: <Andri Benedikt>
# Date: <09-02-2024>
# Project: <practice_04_02>
# Acknowledgements: <>

def count_case(string):
    upper_count = 0
    lower_count = 0
    for x in string:
        if x.isupper():
            upper_count +=1
        elif x.islower():
            lower_count +=1
    return upper_count,lower_count

upper,lower = count_case(input("Enter a string: "))
print("Upper case count:",upper)
print("Lower case count:",lower)



