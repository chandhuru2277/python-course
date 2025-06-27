class Banckaccount:
    def __init__(self):
        self.__password= "abc"

    def get_balance(self):
        return self.__password

class Debitcard(Banckaccount):
    def print_password(self):
        return self.get_balance()
    
c= Debitcard()
print(c.print_password())
