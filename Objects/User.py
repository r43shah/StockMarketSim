from .Portfolio import Portfolio

class User:

    portfolio=[]
    cash=0

    def __init__(self,name):
        self.name=name

    def get_name(self):
        return self.name

    def add_portfolio(self,portfolio_name):
        new_portfolio=Portfolio(portfolio_name)
        self.portfolio.append(new_portfolio)

    def delete_portfolio(self,portfolio_name):
        portfolio_index=-1
        for n in range(len(self.portfolio)):
            if self.portfolio[n].get_name()==portfolio_name:
                portfolio_index=n
                break
        if portfolio_index!=-1:
            self.portfolio.pop(portfolio_index)

    def get_portfolio(self,name):
        for n in range(len(self.portfolio)):
            if name==self.portfolio[n].get_name():
                return self.portfolio[n]
        return -1


    def get_portfolios(self):
        return self.portfolio

    def get_cash(self):
        return self.cash

    def set_cash(self,value):
        self.cash+=value
