import pandas as pd
import assets

print("Financial Organization")
print("---")

name = input("How can I call you? ")
age = input("How old are you? ")
retirement = input("How old will you be when you retire? ")
time_to_retirement = retirement - age
month_income = input("What is your average monthly income? ")
month_spend = input("What is your average monthly spend? ")
months_of_year = 12
year_spend = month_spend * months_of_year
total_investments = input("What is the total value of your investments? ")
net_profitability = input("What is your average net profitability of your investments? ")
employability = input("How good do you consider your emploiability?(high/low) ")

user = assets.User(name, age)
