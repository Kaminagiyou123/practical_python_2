# report.py
#
# Exercise 2.4
import csv
from fileparse import parse_csv
def read_portfolio(filename):
 '''
  read a stock portfolio file into a list of records using parse_csv function.
 '''
 with open(filename) as lines:
  return parse_csv(lines, select=['name','shares','price'], types=[str,int,float])

   
def read_price(filename):
 '''
  read a stock price file into a dictionary with name and price.
 '''
 prices={}
 with open(filename) as lines:
   pricefile= parse_csv(lines,types=[str,float],has_headers=False)
 for s in pricefile:
   prices[s[0]]=s[1]
 return prices

def make_report(portfolio,prices):
  '''
  combine the portfolio (list of dicts) and prices (dicts of name:current price),and generate a list of tupples with name, shares, price, change

  '''
  report=[]
  for s in portfolio:
    row=(s['name'],s['shares'],s['price'],prices[s['name']]-s['price'])
    report.append(row)
  return report

def print_report(report):
  '''
  print the report (list of tuples) into a presentable format, with headers
  '''
  
  headers= ('name','shares','price','change')
  for a in headers:
   print(f'{a:>10s}',end=" ") 
  print()
  print(('-'*10+" ")*4)
  
  for name,shares,price,change in report:
    print(f'{name:>10s} {shares:10d} {price:10.2f} {change:10.2f}')

def portfolio_report(portfolio_filename,prices_filename):
  
  portfolio=read_portfolio(portfolio_filename)
  prices=read_price(prices_filename)
  report=make_report(portfolio,prices)
  print_report(report)



    



