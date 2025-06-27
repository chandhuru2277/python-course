class Employee:

    def show(self):
        print("I am Employee")

    def greet(self):
        print("From Employee class")


class Manager(Employee):
    def show(self):
        super().show(),
        super().greet()
        print("I am also Manager")


e = Employee()
e.show()
m = Manager()
m.show()
