# Author: <Andri Benedikt>
# Date: <09-04-2024>
# Project: <assignment_05_03>
# Acknowledgements: <>

class Account:
    def __init__(self, balance) -> None:
        self.balance = balance
    def __str__(self):
        return f'Balance: {self.balance:.2f}'


class SavingsAccount(Account): 
    def __init__(self, balance, intrest=0.05, bonus=0.1) -> None:
        super().__init__(balance)
        self.intrest = intrest
        self.bonus = bonus
    def update_balance(self):
        self.balance = self.balance*(1+self.intrest+self.bonus)
class DebitAccount(Account):
    def __init__(self, balance, intrest=0.02) -> None:
        super().__init__(balance)
        self.intrest = intrest
    def update_balance(self):
        self.balance = self.balance*(1+self.intrest)