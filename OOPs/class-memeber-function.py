class Parent:
    def public_method(self):
        print("I am public method")

    def private_method(self):
        print("I am private method")

    def protected_method(self):
        print("I am protected method")

    def access_private_method(self):
        return self.private_method()


class Child(Parent):
    def access_member(self):
        self.public_method()
        self.protected_method()
        self.access_private_method()

        try:
            self._Parent__private_method()
        except AttributeError:
            print("you can't access directly!")


c = Child()
c.public_method()
c.protected_method()
c.access_member()
