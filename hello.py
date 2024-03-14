import csv
stafir = ['a','b','c','d','e','f','g']
afrit = []
oll_ord = []
with open('BIN_ordalisti.csv', 'r',encoding='UTF-8', newline='') as file:
    gogn = csv.DictReader(file, delimiter=';')
    for line in gogn:
        #print(line["orð"])
        oll_ord.append(line["orð"])
        
'''
afrit = stafir.copy()
for ord in oll_ord:
    teljari = 0
    for letter in ord:

        if letter in afrit:
            afrit.remove(letter)
            teljari += 1
        else:
            afrit = stafir.copy()
            break
        if teljari == len(ord):
            print(ord,"Þetta orð er í orðalistanum")
            break
'''

'''
prufu_strengur = "aðal"
prufu_ord = ['aðalaðdráttarafl','aðalatburður','aðalatkvæ','eitthvað','annað','baðallð']
for ord in oll_ord:
    if len(ord) > len(prufu_strengur):
        for x in range(len(prufu_strengur)):
            if ord[x] != prufu_strengur[x]:
                break
            if prufu_strengur[:x+1] == prufu_strengur:
                print(ord)
                break
            #print(prufu_strengur[:x+1])

'''

stafroid = ['a','á','b','d','ð','e','é','f','g','h','i','í','j','k','l','m','n','o','ó','p','r','s','t','u','ú','v','x','y','ý','þ','æ','ö']
prufu_strengur = "ma_ur"
prufu_ord = ['maður','aðalatburður','magur','eitthvað','annað','baðallð']
for ord in oll_ord:
    for stafur in stafroid:
        if len(ord) == len(prufu_strengur):
            if prufu_strengur.replace('_',stafur) == ord:
                print(ord)
                break
        