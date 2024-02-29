seconds = int(input("How many seconds? "))
print(seconds,"is equal to:")
mi = seconds//60
seconds = seconds%60

hr = mi//60
mi = mi%60


print("Hours:",hr)
print("Minutes:",mi)
print("Seconds:",seconds)