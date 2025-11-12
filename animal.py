'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

"""
Animal Notes:
- Belong to different categories: (such as mammals, reptiles, birds)
- They may share common behaviours, while also exhibiting unique traits
- all animals should be capable of performing basic actions like making sounds, eating and sleeping.
Other features
- add and remove animals
- assign animals to enclosures
- feeding/cleaning (staff)
- generate reports such as list of animals by species or the status of enclosures (staff)
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, species, age, diet, sound):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__dietary_needs = diet
        self.__sound = sound


    def get_name(self):
        return self.__name

    def set_name(self, animal_name):
        if not isinstance(animal_name, str) or not animal_name.strip():
            raise ValueError("Name must be a non-empty string.")
        self.__name = animal_name

    name = property(get_name, set_name)

    def get_species(self):
        return self.__species

    def set_species(self, animal_species):
        if not isinstance(animal_species, str) or not animal_species.strip():
            raise ValueError("Species must be a non-empty string.")
        self.__species = animal_species

    species = property(get_species, set_species)

    def get_age(self):
        return self.__age

    def set_age(self, animal_age):
        if not isinstance(animal_age, int):
            raise ValueError("Age must be integer value.")
        self.__age = animal_age

    age = property(get_age, set_age)

    def get_diet(self):
        return self.__dietary_needs

    def set_diet(self, animal_diet):
        if not isinstance(animal_diet, str) or not animal_diet.strip():
            raise ValueError("Diet must be a non-empty string.")
        self.__dietary_needs = animal_diet

    diet = property(get_diet, set_diet)\

    def get_sound(self):
        return self.__sound

    def set_sound(self, sound):
        if not isinstance(sound, str) or not sound.strip():
            raise ValueError("Sound must be a non-empty string.")
        self.__sound = sound

    sound = property(get_sound, set_sound)

    """
    Basic Actions
    """
    @abstractmethod
    def make_sound(self):
        pass
    @abstractmethod
    def eat(self):
        pass
    @abstractmethod
    def sleeping(self):
        pass






