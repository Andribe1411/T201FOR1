einkunnir_skil = [81,55,60.5,50,57.5,64.7,57,45,65,66]
medaleinkunn = sum(einkunnir_skil)/len(einkunnir_skil)
#print(medaleinkunn)

hlutaprof = 85

krossaprof = [0,10,10,8,10,0,10,0,0,8,10]
medal_krossaprof = sum(krossaprof)/len(krossaprof)

lokaprof = 45

print(medaleinkunn*0.4+hlutaprof*0.1+medal_krossaprof*00.5+lokaprof*0.45)