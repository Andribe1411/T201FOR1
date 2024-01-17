# Author: <Andri Benedikt>
# Date: <17.01.24>
# Project: <Æfingarverkefni 1>
# Acknowledgements: <ef þú þáðir eða veittir aðstoð þá á það>
# <að vera tekið fram hér>
tala = int(input("Write a 5 digit number: "))
þrjar_tolur = tala // 10
þrjar_tolur = þrjar_tolur % 1000
ein_tala = tala // 100
ein_tala = ein_tala % 10
print("The middle three digits are",þrjar_tolur)
print("The middle digit is",ein_tala)