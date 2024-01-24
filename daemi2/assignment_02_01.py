# Author: <Andri Benedikt>
# Date: <22-01-2024>
# Project: <nafn á verkefninu>
# Acknowledgements: <>
number1 = int(input("First number: "))
number2 = int(input("Second number: "))
number3 = int(input("Third number: "))

if number1 > number2 and number2 > number3:
    print("The middle number is:",number2)
elif number1 < number2 and number2 < number3:
    print("The middle number is:",number2)

elif number2 > number1 and number1 > number3:
    print("The middle number is:",number1)
elif number2 < number1 and number1 < number3:
    print("The middle number is:",number1)


elif number1 > number3 and number3 > number2:
    print("The middle number is:",number3)
elif number1 < number3 and number3 < number2:
    print("The middle number is:",number3)

else:
    print("The middle number is:",number2)