# Author: <Andri Benedikt>
# Date: <22.3.24>
# Project: <Midterm 2>

def print_list(the_list, list_type):
    if len(the_list) > 0:
        if list_type == 'int':
            print('Integers: ',end="" )
        if list_type == 'float':
            print('Floats: ',end="")
        for value in sorted(the_list):
            print(value,end=" ")
        print()

integer_list = []
float_list = []
value_list = []
while True:
    value = input("Input: ")
    if value == "quit":
        break
    else:
        value_list.append(value)
for number in value_list:
    try:
        if float(number) == int(number):
            integer_list.append(int(number))
    except ValueError:
        try:
            float_list.append(float(number))
        except ValueError:
            continue

print_list(integer_list,'int')
print_list(float_list,'float')

