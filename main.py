import pandas as pd

# TODO: Patrimônio Mínimo de Sobrevivência
def pms(month_spend):
    return 6 * month_spend


# TODO: Patrimônio Mínimo Recomendado
def pmr(month_spend, employability):
    if employability == "low":
        return 12 * month_spend
    elif employability == "high":
        return 20 * month_spend


# TODO: Patrimônio Ideal para a sua idade até a aposentadoria
def pi(year_spend, age):
    return  0,1 * year_spend * age


# TODO: Patrimônio Necessário para Independência Financeira
def pnif(year_spend, net_profitability):
    return year_spend / net_profitability

age = input("How old are you? ")
retirement = input("How old will you be when you retire? ")
time_to_retirement = retirement - age
month_income = input("What is your average monthly income? ")
month_spend = input("What is your average monthly spend? ")
months_of_year = 12
year_spend = month_spend * months_of_year
total_investments = input("What is the total value of your investments? ")
net_profitability = input("What is your average net profitability of your investments? "
employability = input("How good do you consider your emploiability?(high/low) ")
