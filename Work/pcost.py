# pcost.py
#
# Exercise 1.27
import sys
import csv

def portfolio_cost(filename):
 '''
 Computes the total cost (share*price) of a portfolio file
 '''
 total_cost=0
 with open(filename) as f:
  rows=csv.reader(f)
  headers=next(rows)
  
  for rowno,row in enumerate(rows,start=1):
     record=dict(zip(headers,row))
     try:
       nshares=int(record['shares'])
       nprice=float(record['price'])
       total_cost+=nshares*nprice
     except ValueError:
      print(f'Row{rowno}: Bad row:{row}')
      continue

 return total_cost
  


# if len(sys.argv)==2:
#  filename=sys.argv[1]
# else:
#  filename='Data/portfolio.csv'
# cost=portfolio_cost(filename)

# print('Total cost:', cost)