# Author: <Andri Benedikt>
# Date: <19.04.24>
# Project: <Lokapróf D3>


folder = ""
PRICES = "_prices.txt"
SHOPPING_LIST = "_shoppinglist.txt"



def open_prices(filename):
    try:
        file = open(folder+filename+PRICES,"r",encoding="UTF-8")
        data = dict()
        for line in file:
            values = line.split()
            if len(values) == 2:
                data[values[0]] = [values[1],str(0)]
            if len(values) == 3:
                data[values[0]] = [values[1],values[2]]
        return data
    except FileNotFoundError:
        print(f"Cannot find information for {filename}")
    
def open_shopping_list(filename):
    try:
        file = open(folder+filename+SHOPPING_LIST,"r",encoding="UTF-8")
        data = dict()
        shopping_list = []
        for line in file:
            values = line.split()
            in_list = False
            for x in shopping_list:
                if values[1] == x[1]:
                    x[0] = int(x[0]) + int(values[0])
                    in_list = True
            if in_list == False:
                shopping_list.append(values)

        for item in shopping_list:
            data[item[1]] = item[0]

        return data
    except FileNotFoundError:
        return "Cannot find .."

file_to_open = input("Filename: ")
prices_data = open_prices(file_to_open)
shopping_list_data = open_shopping_list(file_to_open)
total_vat = 0
total_cost = 0
for x in sorted(shopping_list_data):
    total = int(prices_data[x][0]) * int(shopping_list_data[x])
    vat = int(prices_data[x][0]) * int(shopping_list_data[x]) * (int(prices_data[x][1])/100)
    total_vat += vat
    total_cost += total+vat
    print(f"{x}: ${prices_data[x][0]} x {shopping_list_data[x]} = ${total}")
print(f"Total VAT = ${round(total_vat)}")
print(f"Total = ${round(total_cost)}")