class Animal:
    def __init__(self, name):
        self.name= name
        print("Animal __init__ : ", self.name)

class Dog(Animal):
    def __init__(self, name,bread):
        super().__init__(name)
        self.bread= bread
        print("Animal name: ", self.name)
        print("Animal bread name: ", self.bread)

a= Animal("some animal")
d= Dog("Dog","Labrador")