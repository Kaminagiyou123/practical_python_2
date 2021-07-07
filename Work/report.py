# report.py
#
# Exercise 2.4
from stock import Stock
from fileparse import parse_csv
import tableformat 
from portfolio import Portfolio
def read_portfolio(filename,**opts):
 '''
  read a stock portfolio file into a list of records using parse_csv function.
 '''
 with open(filename) as lines:
  portdicts= parse_csv(lines, select=['name','shares','price'], types=[str,int,float],**opts)
  portfolio=[Stock(**s) for s in portdicts]
  return Portfolio(portfolio)

   
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
    row=(s.name,s.shares,s.price,prices[s.name]-s.price)
    report.append(row)
  return report

def print_report(reportdata,formatter):
  '''
  print the report (list of tuples) into a presentable format, with headers
  '''
  
  formatter.headings(['name','shares','price','change'])
  
  
  for name,shares,price,change in reportdata:
    rowdata=[name,str(shares),f'{price:0.2f}',f'{change:0.2f}']
    formatter.row(rowdata)

def portfolio_report(portfolio_filename,prices_filename,fmt):
  # read data files
  portfolio=read_portfolio(portfolio_filename)
  prices=read_price(prices_filename)
  #create the report data
  report=make_report(portfolio,prices)
  
  formatter=tableformat.create_formatter(fmt)

  print_report(report,formatter)





    



