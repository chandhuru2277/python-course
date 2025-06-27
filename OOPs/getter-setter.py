class Bankaccount:
    def __init__(self, balance):
        self.balance= balance
    def get_balance(self):
        return self.balance
    def set_balance(self,new_balance):
        self.balance= self.balance + new_balance

t= Bankaccount(100)
print(t.get_balance())
t.set_balance(100)
print(t.get_balance())

        