from follow import follow
import csv

def select_columns(rows,indices):
 for row in rows:
  yield [row[index] for index in indices]
  
def convert_types(rows,types):
 for row in rows:
  yield [func(val) for func,val in zip(types,row)]
  
def make_dicts(rows,headers):
 for row in rows:
  yield dict(zip(headers,row))

def filter_symbols(rows,names):
 return (row for row in rows if row['name'] in names)
  
def parse_stock_data(lines):
 rows=csv.reader(lines)
 rows=select_columns(rows,[0,1,4])
 rows=convert_types(rows,[str,float,float])
 rows=make_dicts(rows,['name','price','change'])
 return rows

def ticker(portfile,logfile,fmt):
 import report
 from stock import Stock
 from tableformat import create_formatter
 portfolio=report.read_portfolio(portfile)
 lines=follow(logfile)
 rows=parse_stock_data(lines)
 rows=filter_symbols(rows,portfolio)
 formatter=create_formatter(fmt)
 headings=['name','price','change']
 formatter.headings(headings)
 for row in rows:
  formatter.row([str(row[h]) for h in headings])


if __name__=='__main__':
 ticker('Work/Data/portfolio.csv', 'Work/Data/stocklog.csv', 'txt')

