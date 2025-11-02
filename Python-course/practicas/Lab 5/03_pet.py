"""
Exercise 3
Define a class called Pet that takes a name and species at initialisation. The class has two
methods that return the name and species respectively. Test your code with examples.
"""

class Pet:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def get_name(self):
        return self.name

    def get_species(self):
        return self.species
    
pet0 = Pet("paul", "dog")
pet1 = Pet("beto", "dog")
pet2 = Pet("chip", "dog")
pet3 = Pet("marco", "bird")
    
print(f"Name: {pet0.get_name()}, specie: {pet0.get_species()}")
print(f"Name: {pet1.get_name()}, specie: {pet1.get_species()}")
print(f"Name: {pet2.get_name()}, specie: {pet2.get_species()}")
print(f"Name: {pet3.get_name()}, specie: {pet3.get_species()}")
