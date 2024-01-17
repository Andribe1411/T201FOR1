# Author: <Andri Benedikt>
# Date: <17.01.24>
# Project: <Æfingarverkefni 1>
# Acknowledgements: <ef þú þáðir eða veittir aðstoð þá á það>
# <að vera tekið fram hér>
sec = int(input("How many seconds?"))
min = sec//60
sec = sec %60
hr = min//60
min = min%60
print("Hours:",hr)
print("Minutes:",min)
print("Seconds:",sec)