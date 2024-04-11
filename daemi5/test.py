import sys
sys.path.append('../')
from assignment_05_03 import SavingsAccount, DebitAccount

def print_accounts(accounts):
    for account in accounts:
        print(account)
    print()

def update_accounts(accounts):
    for account in accounts:
        account.update_balance()

sav1 = SavingsAccount(1000)
deb1 = DebitAccount(1000)
sav2 = SavingsAccount(2000)
deb2 = DebitAccount(4000)

accounts = [sav1, deb1, sav2, deb2]
print_accounts(accounts)
update_accounts(accounts)

print_accounts(accounts)
update_accounts(accounts)

print_accounts(accounts)
update_accounts(accounts)

print_accounts(accounts)

print("test")
s1 = SavingsAccount(3000)
s1.update_balance()
print(s1)