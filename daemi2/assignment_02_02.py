# Author: <Andri Benedikt>
# Date: <22-01-2024>
# Project: <nafn á verkefninu>
# Acknowledgements: <>

a = int(input("Coefficient a: "))
b = int(input("Coefficient b: "))
c = int(input("Coefficient c: "))
d = (b**2)-4*a*c
if d >0:
    print("Two roots")
elif d == 0:
    print("Single root")
else:
    print("No root")