from yahoo_finance import Share
import json

class Company:

    num_stocks=0

    def __init__(self,name):
        self.name=name

    def get_stock_price(self):
        stock=Share(self.name)
        return stock.get_price()

    def get_num_stocks(self):
        return self.num_stocks

    def set_num_stocks(self,num):
        self.num_stocks+=num

    def get_name(self):
        return self.name