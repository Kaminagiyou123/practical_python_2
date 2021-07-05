# fileparse.py
import csv
def parse_csv(filename,select=None,types=None, has_headers=True,delimiter=",",silence_error=False):
 '''
 parse a CSV file into list of records (dicionaries or tupples depending on headers)
 '''
 if select and not has_headers:
   raise RuntimeError('select argument requires column headers')
 
 with open(filename) as f:
  rows=csv.reader(f,delimiter=delimiter)
  if has_headers:
    headers=next(rows)
  
  if select:
    indices=[headers.index(colname) for colname in select]
    headers=select
  
  records=[]

  for rowno,row in enumerate(rows,start=1):
   if not row:
     continue
   
   if select:
    row=[row[index] for index in indices]
    
   if types:
     try:
      row=[func(val) for func,val in zip(types,row) ]
     except ValueError as e:
       if silence_error==False:
        print(f'Row {rowno},Couldnt convert {row}')
        print(f'Row {rowno},{e}')
    
   if has_headers:    
      record=dict(zip(headers,row))
   else:
     record=tuple(row)
     
   records.append(record)
   
  return records
 
