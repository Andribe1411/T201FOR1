number = int(input("Write a 5 digit number: "))
middleThree = number//10
middleThree = middleThree%1000
print("The middle three digits are",middleThree)
middle = number//100
middle = middle%10
print("The middle digit is", middle)