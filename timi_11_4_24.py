LENGTH_OF_ISBN = 13
POSITIONS_OF_DASHES = [1, 5, 11]

def isbn_is_ok(isbn):
    if len(isbn) != LENGTH_OF_ISBN:
        return False
    for i,c in enumerate(isbn):
        if i in POSITIONS_OF_DASHES:
            if c != '-':
                return False
        else:
            if not c.isdigit():
                return False
    return True


isbn = input('Enter an ISBN: ')
while isbn != 'q':
    if isbn_is_ok(isbn):
        print('Valid format')
    else:
        print('Invalid format')
    
    isbn = input('Enter an ISBN: ')