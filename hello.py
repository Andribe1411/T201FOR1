import re
import csv

# þessi kóði kemur frá:
#https://stackoverflow.com/questions/65840793/how-to-get-all-possible-combinations-of-characters-in-a-string
def permutations(remaining, candidate="",skilar = []):
    if len(remaining) == 0:
        #print(candidate)
        skilar.append(candidate)
        #print(skilar,'-skilar')
    for i in range(len(remaining)):
        newCandidate = candidate + remaining[i]
        newRemaining = remaining[0:i] + remaining[i+1:]
        permutations(newRemaining, newCandidate)
    return skilar


gogn = []
stytt_gogn = []
with open('BIN_ordalisti.csv', 'r',encoding='UTF-8', newline='') as file:
    for line in csv.reader(file):
        gogn.append(line)
        #stytt_gogn.append(line)

for x in gogn:
    str1 = ""
    for ele in x:
        str1 += ele
        temp =str1.split(";")
        stytt_gogn.append(temp[0])

#print(stytt_gogn)
prufa =[]
on = True
while on == True:
    val = int(input("Val: "))
    if val == 1:
        letters = "abcdef"
        test = permutations(letters)
        #print(test,"-skilar")
        #teljari = 0
        for i in test:
            for y in stytt_gogn:
                if y == i:
                    print("bætt við lista")
                    prufa.append(y)
                #elif y!=i and teljari%10==0:
                    #print("ekki bætt á lista")
            #teljari = teljari+1
        print(prufa)


    elif val == 2:
        break
    elif val == 3:
        print("Vali hætt")
        on = False
