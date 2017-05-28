from .Portfolio import Portfolio

class User:

    portfolio=[]

    def __init__(self,name):
        self.name=name

    def getName(self):
        return self.name

    def addPortfolio(self,portfolio_name):
        new_portfolio=Portfolio(portfolio_name)
        self.portfolio.append(new_portfolio)

    def deletePortfolio(self,portfolio_name):
        portfolio_index=self.get_index(portfolio_name,self.portfolio)
        if portfolio_index!=-1:
            self.portfolio.pop(portfolio_index)

    def getPortfolios(self):
        return self.portfolio

    def get_index(self,value,array):
        for n in range(len(array)):
            if value==array[n]:
                return n
        return -1