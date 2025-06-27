class Animal:
    species = "Wild animal"

    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} Make a sound"


class Dog(Animal):
    def speak(self):
        return f"{self.name} make barks"


class Cat(Animal):
    def speak(self):
        return f"{self.name} make memow"


a= Animal("some animal")
print(a.speak())

b= Dog("Tommy")
print(b.speak())

c= Cat("Kitty")
print(c.speak())