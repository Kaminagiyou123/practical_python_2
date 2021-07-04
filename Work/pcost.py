# pcost.py
#
# Exercise 1.27
import sys
import csv
def portfolio_cost(filename):
 total_cost=0
 with open(filename) as f:
  rows=csv.reader(f)
  headers=next(rows)
 
  for row in rows:
     try:
       nshares=int(row[1])
       nprice=float(row[2])
       total_cost+=nshares*nprice
     except ValueError as e:
      print(e)
      continue

 return total_cost
  


if len(sys.argv)==2:
 filename=sys.argv[1]
else:
 filename='Data/portfolio.csv'
cost=portfolio_cost(filename)

print('Total cost:', cost)