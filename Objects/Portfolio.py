from .Company import Company

class Portfolio:

    companies=[]

    def __init__(self,name):
        self.name=name

    def get_name(self):
        return self.name

    def get_company(self,name):
        for n in range(len(self.companies)):
            if name==self.companies[n].get_name():
                return self.companies[n]
        return -1

    def get_list_companies(self):
        return self.companies

    def add_company(self,company_name):
        company=Company(company_name)
        self.companies.append(company)

    def delete_company(self,company):
        company_index=-1
        for n in range(len(self.companies)):
            if company==self.companies[n].get_name():
                company_index=n
        if company_index!=-1:
            self.companies.pop(company_index)

    def get_index(self,value,array):
        for n in range(len(array)):
            if value==array[n]:
                return n
        return -1

