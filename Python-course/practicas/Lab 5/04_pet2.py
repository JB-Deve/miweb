"""
xercise 4
Refactor the Pet class from the previous example so that it has a class variable
allowed_species that contains a list of all the species that can be added to the class. During
initialisation check that the species that is being created is an allowed species.
"""

class Pet:
    allowed_species = ["dog", "cat", "bird", "hamster"]

    def __init__(self, name, species):

        # if species not in Pet.allowed_species:
        #     raise ValueError(f"Species '{species}' is not allowed. Allowed species {Pet.allowed_species}")

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

