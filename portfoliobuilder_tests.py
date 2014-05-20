import unittest
from portfoliobuilder import Portfolio, Stock

class portfolio_and_stock_test(unittest.TestCase):

	def test_portfolio(self):
		my_stock = [Stock("Leucadia","LUK",10,27)]
		Stock_Portfolio = Portfolio(my_stock)
		self.assertEqual(1,len(Stock_Portfolio.stocks))

	def test_two_stocks_added_to_portfolio(self):
		my_stocks = [Stock("Leucadia","LUK",10,27), Stock("Apple","APPL",2,400)]
		Stock_Portfolio = Portfolio(my_stocks)
		self.assertEqual(2,len(Stock_Portfolio.stocks))

	def test_stock_contains_company(self):
		Leucadia = Stock("Leucadia","LUK",10,27)
		self.assertEqual("Leucadia",Leucadia.company)

	def test_stock_contains_ticker(self):
		Leucadia = Stock("Leucadia","LUK",10,27)
		self.assertEqual("LUK",Leucadia.ticker)

	def test_stock_contains_shares(self):
		Leucadia = Stock("Leucadia","LUK",10,27)
		self.assertEqual(10,Leucadia.shares)

	def test_stock_contains_price(self):
		Leucadia = Stock("Leucadia","LUK",10,27)
		self.assertEqual(27,Leucadia.price)

	def test_marketcap(self):
		Leucadia = Stock("Leucadia","LUK",10,27)
		self.assertEqual(270,Leucadia.marketcap)

if __name__ == '__main__':
    unittest.main()