import csv 
f=open('Work/Data/portfoliodate.csv')
rows=csv.reader(f)
headers=next(rows)
print(headers)

select =['name','shares','price']
indices=[headers.index(colname) for colname in select]
print(indices)

row=next(rows)
record={colname:row[index] for colname,index in zip(select,indices)}
print(record)

portfolio=[{colname:row[index] for colname,index in zip(select,indices)} for row in rows]

print(portfolio)