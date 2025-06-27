class Book:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, others):
        return Book(self.amount + others.amount)

    def __str__(self):
        return f"Book amount: {self.amount}"  # print values of string for users

    def __repr__(self):
        return f"Book amount: {self.amount}"  # print values of string streams for developer


b1 = Book(100)
b2 = Book(200)

print(b1)
print(repr(b1))

print(b2)
print(repr(b2))

b3 = b1 + b2
print(b3)
