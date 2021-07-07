from portfolio import Portfolio

with open('Work/Data/portfolio.csv') as lines:
  port=Portfolio.from_csv(lines)

print(list(port))