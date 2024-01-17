# Author: <Andri Benedikt>
# Date: <17.01.24>
# Project: <Æfingarverkefni 1>
# Acknowledgements: <ef þú þáðir eða veittir aðstoð þá á það>
# <að vera tekið fram hér>
import math

a = float(input("Side length a: "))
b = float(input("Side length b: "))
c = float(input("Side length c: "))
s=(a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("The area is:",area)