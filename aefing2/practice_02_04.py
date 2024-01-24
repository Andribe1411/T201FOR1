# Author: <Andri Benedikt>
# Date: <22-01-2024>
# Project: <nafn á verkefninu>
# Acknowledgements: <>


value = None
valueList = []
on = True
while on == True:
    value = input("Value: ")
    if value == "done":
        on = False
    else:
        valueList.append(float(value))

print("Max:",max(valueList))
print("Min:",min(valueList))
mean = sum(valueList)/len(valueList)
print("Mean:",mean)
    
    