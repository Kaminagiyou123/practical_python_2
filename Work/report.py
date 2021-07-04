# report.py
#
# Exercise 2.4
import csv
def read_portfolio(filename):
 portfolio=[]
 with open(filename) as f:
  rows=csv.reader(f)
  headers=next(rows)
 
  for row in rows:
   holding=dict(zip(headers,(row[0],int(row[1]),float(row[2]))))
   portfolio.append(holding)
   
  return portfolio
   
def read_price(filename):
 prices={}
 with open(filename) as f:
  rows=csv.reader(f)
  for row in rows:
   try:
    prices[row[0]]=float(row[1])
   except IndexError:
     pass
  
  return prices

def make_report(portfolio,prices):
  report=[]
  for s in portfolio:
    row=(s['name'],s['shares'],s['price'],prices[s['name']]-s['price'])
    report.append(row)
  return report

def print_table(report):
  
  headers= ('name','shares','price','change')
  for a in headers:
   print(f'{a:>10s}',end=" ") 
  print()
  print(('-'*10+" ")*4)
  
  for name,shares,price,change in report:
    print(f'{name:>10s} {shares:10d} {price:10.2f} {change:10.2f}')
    
portfolio=read_portfolio('Work/Data/portfolio.csv')
prices=read_price('Work/Data/prices.csv')
report=make_report(portfolio,prices)
print_table(report)


