'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Enclosure:
    CLEANLINESS = {"Clean", "Moderate", "Dirty"}
    ENVIRONMENTS = {"Savannah", "Aquatic", "Aviary", "Jungle", "Desert", "Arctic"}
    def __init__(self, name, size, environmental_type, cleanliness_level, compatible_species):
        self.__name = name
        self.__environmental_type = environmental_type
        self.__size = size
        self.__cleanliness = cleanliness_level
        self.__compatible_species = compatible_species
        self.__animal_species = []


