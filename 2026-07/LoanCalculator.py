'''
Loan Calculator
Given a loan amount, annual interest rate percentage, and fixed monthly payment, return an array of remaining balances after each monthly payment until the loan is paid off.

Each month, interest is calculated on the remaining balance using the monthly interest rate: (annual rate / 100) / 12, then the monthly payment is subtracted.
Return each remaining balance rounded to the nearest dollar.
Include the loan amount in the returned array. The first element in the array will always be the loan amount, and the last element of the array will always be 0.
'''
import math
def get_loan_schedule(loan_amount, annual_rate, monthly_payment):

    monthly_rate = (annual_rate / 100 ) / 12
    balance = loan_amount
    result =[balance]

    while balance > 0:
        balance = balance * (1 + monthly_rate) - monthly_payment
        print(balance)
        # balance = round(balance)
        # print(balance)
        if balance < 0:
            balance = 0
        result.append(round(balance))

    print(result)
    loan_amount = result

    return loan_amount

# t = get_loan_schedule(1000, 0, 200)
# print(t)

t1 = get_loan_schedule(1000, 5, 200)
print(t1)