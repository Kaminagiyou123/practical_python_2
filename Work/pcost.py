# pcost.py
#
# Exercise 1.27


from stock import Stock
from report import read_portfolio
from portfolio import Portfolio
def portfolio_cost(filename):
 '''
 Computes the total cost (share*price) of a portfolio file
 '''
 portfolio=read_portfolio(filename)
 print(portfolio)
 return portfolio.total_cost
  


# if len(sys.argv)==2:
#  filename=sys.argv[1]
# else:
#  filename='Data/portfolio.csv'
# cost=portfolio_cost(filename)

# print('Total cost:', cost)