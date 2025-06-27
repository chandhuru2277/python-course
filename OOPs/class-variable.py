class ANIMAL:
    species= "Wild Animals"

    def __init__(self,species_name):
        self.species_name=species_name
    
    def get_species_name(self):
        self.report= f"Animal name: {self.species_name}"
        return self.report


cat= ANIMAL("Cat")
print(cat.get_species_name())
print(ANIMAL.species)

dog= ANIMAL("Dog")
print(dog.get_species_name())
print(ANIMAL.species)
