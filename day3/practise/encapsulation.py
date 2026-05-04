class bankaccount:
    def __init__(self,name,amount):
        self.name=name
        self._amount=amount

    def get_balance(self):
        return self._amount
    
    def deposit(self,dp_amount:int):
        if dp_amount >0:
            self._amount+=dp_amount

        else:
            print("Invalid deposit amount")
    
    def withdraw(self,wd_amount:int):
        if wd_amount <=self._amount and wd_amount > 0:
            self._amount-=wd_amount

        else:
            print("balance not enough")

customer1=bankaccount("giri",50000)
customer2=bankaccount("hari",78000)

print(customer1.get_balance())

customer1.deposit(-876)
print(customer1.get_balance())

customer1.withdraw(7526)
print(customer1.get_balance())

print(customer2.get_balance())

customer2.withdraw(545004)
print(customer2.get_balance())

customer2.deposit(645)
print(customer2.get_balance())