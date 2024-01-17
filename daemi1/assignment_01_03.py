# Author: <Andri Benedikt>
# Date: <17.01.24>
# Project: <Æfingarverkefni 1>
# Acknowledgements: <ef þú þáðir eða veittir aðstoð þá á það>
# <að vera tekið fram hér>

mm = int(input("How many mm? "))
print(mm,"mm is equal to:")
km = mm // 1000000
mm = mm%1000000
print(km,"km")
m = mm//1000
mm = mm%1000
print(m,"m")
cm = mm//10
mm = mm%10
print(cm,"cm")
print(mm,"mm")