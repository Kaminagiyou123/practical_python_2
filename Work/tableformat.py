class TableFormatter:
 def headings(self,headers):
  '''
  Emit the table headings
  '''
  raise NotImplementedError
 
 def row(self,rowdata):
  '''
  Emit a single row
  '''
  raise NotImplementedError
 
class TextTableFormatter(TableFormatter):
  '''
  Emit the table in plain-text format
  '''
  def headings(self,headers):
   for h in headers:
    print(f'{h:>10s}',end=' ')
   print()
   print(("-"*10+" ")*len(headers))
   
  def row(self,rowdata):
   for d in rowdata:
    print(f'{d:>10s}',end=' ')
   print()

class CSVTableFormatter(TableFormatter):
 def headings(self,headers):
  print(','.join(headers))
 
 def row(self,rowdata):
  print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
 def headings(self,headers):
  print('<tr><th>'+'</th><th>'.join(headers)+'</th></tr>')
 
 def row(self,rowdata):
  print('<tr><td>'+'</td><td>'.join(rowdata)+'</td></tr>')

class FormatError(RuntimeError):
  pass
def create_formatter(fmt):
  if fmt=='txt':
    formatter=TextTableFormatter()
  elif fmt=='csv':
    formatter=CSVTableFormatter()
  elif fmt=='html':
    formatter=HTMLTableFormatter()
  else:
    raise FormatError(f"Not accepted format {fmt}")
  return formatter


def print_table(portfolio,select,formatter):
  formatter.headings(select)
  
  for s in portfolio:
    rowdata=[str(getattr(s,colname)) for colname in select]
    formatter.row(rowdata)
    
  
  