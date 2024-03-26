# Author: <Andri Benedikt>
# Date: <22.3.24>
# Project: <Midterm 2>

def open_letter(filename):
    letter_list = []
    the_file = open(filename,'r')
    for line in the_file:
        letter_list.append(line)
    the_file.close()
    return letter_list

def find_file(number):
    if number == 0:
        return zero
    elif number == 1:
        return one
    elif number == 2:
        return two
    elif number == 3:
        return three
    elif number == 4:
        return four
    elif number == 5:
        return five
    elif number == 6:
        return six
    elif number == 7:
        return seven
    elif number == 8:
        return eight
    elif number == 9:
        return nine

def print_letter(number):
    for x in range(5):
        for y in number:
            print(find_file(y)[x].strip('\n'), end="")
        print()



folder = 'prof2/'
#folder = ''
zero = open_letter(folder+'letter_0.txt')
one = open_letter(folder+'letter_1.txt')
two = open_letter(folder+'letter_2.txt')
three = open_letter(folder+'letter_3.txt')
four = open_letter(folder+'letter_4.txt')
five = open_letter(folder+'letter_5.txt')
six = open_letter(folder+'letter_6.txt')
seven = open_letter(folder+'letter_7.txt')
eight = open_letter(folder+'letter_8.txt')
nine = open_letter(folder+'letter_9.txt')

number_set = {0,1,2,3,4,5,6,7,8,9}
while True:
    all_numbers = []
    value = input('Write a number: ')
    try:
        if int(value) <0:
            break
    except ValueError:
        break
    
    for x in value:
        try:
            number = int(x)
            all_numbers.append(number)
        except ValueError:
            break
    print_letter(all_numbers)
    number_set = number_set & set(all_numbers)

print("Always used digits:",end=" ")
print(str(number_set)[1:-1])
#for x in number_set:
#    print(x,end=", ")