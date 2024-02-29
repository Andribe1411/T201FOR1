# Author: <Andri Benedikt>
# Date: <23-02-2024>
# Project: <mt_01_01>
on = True
total_dollars = 0

def split_money(doll,wanted):
    final_money = doll//wanted
    remaining_money = doll%wanted
    return final_money,remaining_money

while on == True:
    value = input("Amount ($): ")
    if value == "quit":
        on = False
    else:
        
        dollars = int(value)
        total_dollars+=dollars
        
        hundred_dollars,dollars = split_money(dollars,100)
        tweanty_dollars,dollars = split_money(dollars,20)
        ten_dollars,dollars = split_money(dollars,10)
        five_dollars,dollars = split_money(dollars,5)


        print(f"${value} is equal to:")
        
        if hundred_dollars > 0:
            print(hundred_dollars,"x $100")
        if tweanty_dollars > 0:
            print(tweanty_dollars,"x $20")
        if ten_dollars > 0:
            print(ten_dollars,"x $10")
        if five_dollars > 0:
            print(five_dollars,"x $5")
        if dollars > 0:
            print(dollars,"x $1")
print(f"You converted {total_dollars} dollars.")