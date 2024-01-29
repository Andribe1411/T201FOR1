THE_BOX_SYMBOL = '#'

size_of_the_box = int(input('Size of the box? '))
center = 2*size_of_the_box + 5

for k in range(size_of_the_box):
    for j in range(k+1):
        for l in range(center-j):
            print(' ', end='')

        for i in range(2*j+1):
            print(THE_BOX_SYMBOL, end='')
        print()

print()


