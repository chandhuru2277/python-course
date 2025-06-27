class Animal:
    def speak(self):
        print("Animal make sound")


class Dog(Animal):
    def speak(self):
        print("barks")


class Cat(Animal):
    def speak(self):
        print("Meow")


class Cow(Animal):
    def speak(self):
        print("Moo")


def make_sound(animal):
    animal.speak()


animals = [Dog(), Cat(), Cow()]
for animal in animals:
    make_sound(animal)
