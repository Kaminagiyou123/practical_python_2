import report
import gzip
import fileparse

with gzip.open('Work/Data/portfolio.csv.gz','rt') as f:

 port= fileparse.parse_csv(f,types=[str,int,float])

print(port)