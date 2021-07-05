# pcost.py
#
# Exercise 1.27

import csv
from stock import Stock
from fileparse import parse_csv

def portfolio_cost(filename):
 '''
 Computes the total cost (share*price) of a portfolio file
 '''
 total_cost=0
 with open(filename) as lines:
  rows= parse_csv(lines, select=['name','shares','price'], types=[str,int,float])

  total_cost= sum(row['shares']*row['price'] for row in rows)

 return total_cost
  


# if len(sys.argv)==2:
#  filename=sys.argv[1]
# else:
#  filename='Data/portfolio.csv'
# cost=portfolio_cost(filename)

# print('Total cost:', cost)