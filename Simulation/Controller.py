from Objects.User import User
from Objects.Portfolio import Portfolio
from Objects.Orders import Orders
from Objects.Company import Company

def main():
    user=User("Raj")
    user.get_name()
    user.add_portfolio("Technology")
    print(user.get_portfolios())
    user.add_portfolio("Finance")
    print(user.get_portfolios())
    user.delete_portfolio("Finance")
    print(user.get_portfolios())
    portfolio=user.get_portfolio("Technology")
    print(portfolio)
    print(portfolio.get_name())
    portfolio.add_company("AAPL")
    print(portfolio.get_list_companies())
    portfolio.add_company("CCO")
    print(portfolio.get_list_companies())
    portfolio.delete_company("AAPL")
    print(portfolio.get_list_companies())
    company=portfolio.get_company("CCO")
    print(company.get_name())
    print(company.get_stock_price())
    print(company.get_num_stocks())


main()