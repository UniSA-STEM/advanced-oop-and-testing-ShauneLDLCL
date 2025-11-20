'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''
from math import isnan

from animal import Animal

class Enclosure:
    CLEANLINESS = {"Clean", "Moderate", "Dirty"}
    ENVIRONMENTS = {"Savannah", "Aquatic", "Aviary", "Jungle", "Desert", "Arctic", "Rainforest", "Grasslands", "Wetlands"}
    def __init__(self, name, size, environment_type, cleanliness_level, compatible_species):
        self.__name = name
        self.__environment_type = environment_type
        self.__size = size
        self.__cleanliness = cleanliness_level
        self.__compatible_species = compatible_species
        self.__animal_species = []

    def get_name(self):
        return self.__name

    def set_name(self, enclosure_name):
        if not isinstance(enclosure_name, str) or not enclosure_name.strip():
            raise ValueError("Enclosure name must be a non-empty string.")
        self.__name = enclosure_name

    name = property(get_name, set_name)

    def get_environment_type(self):
        return self.__environment_type

    def set_environment_type(self, environment_type):
        if not isinstance(environment_type, str) or not environment_type.strip():
            raise ValueError("Environment type must be a non-empty string.")
        if not environment_type not in Enclosure.ENVIRONMENTS:
            raise ValueError(f"Environment must be one of: {Enclosure.ENVIRONMENTS}")
        self.__environment_type = environment_type

    environment_type = property(get_environment_type, set_environment_type)

    def get_size(self):
        return self.__size

    def set_size(self, enclosure_size):
        if not isinstance(enclosure_size, int) or enclosure_size <= 0:
            raise ValueError("Size must be a positive integer.")
        if enclosure_size < len(self.__animal_species):
            raise ValueError("Size cannot be smaller than the current number of animals.")
        self.__size = enclosure_size

    enclosure_size = property(get_size, set_size)

    def get_cleanliness(self):
        return self.__cleanliness

    def set_cleanliness(self, cleanliness_level):
        if not isinstance(cleanliness_level, str) or not cleanliness_level.strip():
            raise ValueError("Cleanliness must be a non-empty string.")
        if cleanliness_level not in Enclosure.CLEANLINESS:
            raise ValueError(f"Cleanliness must be one of: {Enclosure.CLEANLINESS}")
        self.__cleanliness = cleanliness_level

    cleanliness_level = property(get_cleanliness, set_cleanliness)

    def get_compatible_species(self):
        return self.__compatible_species

    compatible_species = property(get_compatible_species)

    def get_animals(self):
        return (self.__animal_species)

    animal_species = property(get_animals)

    def add_animal(self, animal):
        if not isinstance(animal, Animal):
            raise ValueError("Only Animal objects may be added to an enclosure.")

        if not isinstance(animal, self.__compatible_species):
            raise ValueError(f"This enclosure only accepts {self.__compatible_species.__name__} types")

        if len(self.__animal_species) >= self.__size:
            raise ValueError("Enclosure is full.")

        self.__animal_species.append(animal)

    def remove_animal(self, animal):
        if animal not in self.__animal_species:
            raise ValueError("This animal is not in the enclosure.")
        self.__animal_species.remove(animal)

    def enclosure_status(self):
        animal_names = (", ".join(animal.get_name() for animal in self.__animal_species) if self.__animal_species else "No animals")

        return (
            f"Enclosure: {self.__name}\n"
            f"Environment: {self.__environment_type}\n"
            f"Cleanliness: {self.__cleanliness}\n"
            f"Animals: {animal_names}\n"
            f"Capacity: {len(self.__animal_species)}/{self.__size}"
        )

    def __str__(self):
        return self.enclosure_status()

