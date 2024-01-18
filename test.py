# Author: <Andri Benedikt>
# Date: <17.01.24>
# Project: <Æfingarverkefni 1>
# Acknowledgements: <ef þú þáðir eða veittir aðstoð þá á það>
# <að vera tekið fram hér>
sec = int(input("How many seconds? "))
print(sec,"is equal to:")

min = sec/60
min = int(min)
sec = sec -60*min
hr = min/60
hr = int(hr)
min = min-60*hr

print("Hours:",hr)
print("Minutes:",min)
print("Seconds:",sec)