class Bankaccount:
    def __init__(self,balance):
        self.balance= balance

account= Bankaccount(1000)
print(account.balance)
# you cant access this outer the class 
# account=100 : so can't modify and change
# Error print(account.balance)  
