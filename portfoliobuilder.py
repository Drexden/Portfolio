#creates a portfolio and adds a stock, or stocks, to it

class Portfolio(object):
	stocks = []
	def __init__(self,stocks):
		self.stocks = stocks

class Stock(object):
	def __init__(self, company, ticker, shares, price):
		self.company = company
		self.ticker = ticker
		self.shares = shares
		self.price = price
		self.marketcap = shares*price
		

my_stocks = [Stock("Leucadia","LUK",10,27), Stock("Apple","APPL",2,400)]
my_portfolio = Portfolio(my_stocks)
for stock in my_portfolio.stocks:
	print stock.company + " " + stock.ticker + " " + str(stock.shares) + " " + str(stock.price) + " " + str(stock.marketcap)
