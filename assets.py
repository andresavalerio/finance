import pandas as pd

MONTHS_OF_YEAR = 12

class User(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def financial_desires(self):
        pass

class Assets():
    # Patrimônio Mínimo de Sobrevivência
    def __init__(self, month_spend, net_profitability):
        self.month_spend = month_spend
        self.year_spend = month_spend * MONTHS_OF_YEAR
        self.net_profitability = net_profitability
    
    def pms(self):
        return 6 * self.month_spend
    
    # TODO: Patrimônio Mínimo Recomendado
    def pmr(self, employability):
        if employability == "low": # using employability from User
            return 12 * self.month_spend
        elif employability == "high": # using employability from User
            return 20 * self.month_spend
    
    # TODO: Patrimônio Ideal para a sua idade até a aposentadoria
    def pi(self, age):
        return  0,1 * self.year_spend * age # using age from User
    
    # Patrimônio Necessário para Independência Financeira
    def pnif(self):
        return self.year_spend / self.net_profitability
    
    # TODO: print assets
    def show_assets():
        pass
