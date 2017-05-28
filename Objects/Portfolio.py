from Company import Company

class Portfolio:

    companies=[]

    def __init__(self,name):
        self.name=name

    def get_name(self):
        return self.name

    def get_list_companies(self):
        return self.companies

    def add_company(self,company_name):
        company=Company(company_name)
        self.companies.append(company)

    def remove_company(self,company):
        company_index=self.get_index(company,self.companies)
        if company_index!=-1:
            self.companies.pop(0)

    def get_index(self,value,array):
        for n in range(len(array)):
            if value==array[n]:
                return n
        return -1

