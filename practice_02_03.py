# Author: <Norbert Maksymilian Kania>
# Date: <23.01.24>
# Project: <Æfingaverkefni 02>
# Acknowledgements: <ef þú þáðir eða veittir aðstoð þá á það>
# <Github Copilot autocompletions>

n = int(input("Write a positive integer n: "))

if n < 0:
    print("positive integer only please")
else:
    a = n**2
    b = (n+1)**2
    print(f"Prime numbers between {a} and {b}:")
    while a <= b+1:
        if a == 1 or a == 2 or a == 3 or a == 5 or a == 7 or a == 11 or a == 13 or a == 17 or a == 19 or a == 23 or a == 29 or a == 31 or a == 37 or a == 41 or a == 43 or a == 47 or a == 53 or a == 59 or a == 61 or a == 67 or a == 71 or a == 73 or a == 79 or a == 83 or a == 89 or a == 97 or a == 101 or a == 103 or a == 107 or a == 109 or a == 113 or a == 127 or a == 131 or a == 137 or a == 139 or a == 149 or a == 151 or a == 157 or a == 163 or a == 167 or a == 173 or a == 179 or a == 181 or a == 191 or a == 193 or a == 197 or a == 199 or a == 211 or a == 223 or a == 227 or a == 229 or a == 233 or a == 239 or a == 241 or a == 251 or a == 257 or a == 263 or a == 269 or a == 271:
            print(a)
            a = a + 1
        elif (a % 2 != 0) and (a % 3 != 0) and (a % 5 != 0) and (a % 7 != 0) and (a % 11 != 0) and (a % 13 != 0) and (a % n != 0) and (a % 17 != 0) and (a % 19 != 0) and (a % 23 != 0) and (a % 29 != 0) and (a % 31 != 0) and (a % 37 != 0) and (a % 41 != 0) and (a % 43 != 0) and (a % 47 != 0) and (a % 53 != 0) and (a % 59 != 0) and (a % 61 != 0) and (a % 67 != 0) and (a % 71 != 0) and (a % 73 != 0) and (a % 79 != 0) and (a % 83 != 0) and (a % 89 != 0) and (a % 97 != 0) and (a % 101 != 0) and (a % 103 != 0) and (a % 107 != 0) and (a % 109 != 0) and (a % 113 != 0) and (a % 127 != 0) and (a % 131 != 0) and (a % 137 != 0) and (a % 139 != 0) and (a % 149 != 0) and (a % 151 != 0) and (a % 157 != 0) and (a % 163 != 0) and (a % 167 != 0) and (a % 173 != 0) and (a % 179 != 0) and (a % 181 != 0) and (a % 191 != 0) and (a % 193 != 0) and (a % 197 != 0) and (a % 199 != 0) and (a % 211 != 0) and (a % 223 != 0) and (a % 227 != 0) and (a % 229 != 0) and (a % 233 != 0) and (a % 239 != 0) and (a % 241 != 0) and (a % 251 != 0) and (a % 257 != 0) and (a % 263 != 0):
            print(a)
            a = a + 1
        else:
            a = a + 1 


