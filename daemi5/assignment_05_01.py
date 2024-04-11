# Author: <Andri Benedikt>
# Date: <09-04-2024>
# Project: <assignment_05_01>
# Acknowledgements: <W3Schools, ChatGPT>


class Stock:
    def __init__(self, symbol, shares) -> None:
        self.symbol = symbol
        self.shares = shares

    def __str__(self) -> str:
        return f"{self.symbol}: {str(self.shares)}"

class Portfolio():
    def __init__(self) -> None:
        self.stocks = []

    def add(self, stock):
        self.stocks.append(stock)
    
    def __str__(self):
        portfolio_contents = ""
        for stock in self.stocks:
            portfolio_contents += str(stock) + "\n"
        return portfolio_contents
    