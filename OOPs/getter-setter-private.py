class Bankaccount:
    __branch_code = 32277

    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def set_balance(self, new_balance):
        self.balance = self.balance + new_balance

    def get_branch_code():
        return Bankaccount.__branch_code

    def set_branch_code(new_branch_code):
        Bankaccount.__branch_code = new_branch_code

    def customer_get_branch_code(self):
        self.branch_code = Bankaccount.__branch_code
        return self.branch_code

    def cutomer_set_branch_code(self, branch_code):
        Bankaccount.__branch_code = branch_code


t = Bankaccount(100)
print(t.get_balance())
t.set_balance(100)
print(t.get_balance())

# you can't access the private variable outer the class
# print("branch code")
# print(t.__branch_code)

print("branch code")
print(Bankaccount.get_branch_code())  # using class to access the private variable

# change the private variable using outside
Bankaccount.set_branch_code(2277)
print(Bankaccount.get_branch_code())

# customer get the branch code
print(t.customer_get_branch_code())

# customer set the branch code
t.cutomer_set_branch_code(1111)
print(t.customer_get_branch_code())
