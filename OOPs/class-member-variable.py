class Parent:
    def __init__(self):
        self.public_var= 'I am public'
        self._protected_var= "I am protected"
        self.__private_var= "I am private"

    def get_private_var(self):
            return self.__private_var

class Child(Parent):
    def access_members(self):
        print(self.public_var)
        print(self._protected_var)
        print(self.get_private_var())
    def access_private(self):
         return self.get_private_var()

t= Child()
t.access_members()

print(t.public_var)
print(t._protected_var)
print(t.access_private())
