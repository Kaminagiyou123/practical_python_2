# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
m=0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
  while payment<principal:
      if m<=extra_payment_end_month and m>=extra_payment_start_month:
         payment=2684.11+extra_payment
      else:
         payment = 2684.11   
      principal = principal * (1+rate/12) - payment
      total_paid = total_paid + payment
      m+=1
      print(m,'{:.2f}'.format(total_paid),'{:.2f}'.format(principal))


