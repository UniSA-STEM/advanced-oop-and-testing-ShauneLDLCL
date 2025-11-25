"""
File: animal.py
Description: Defines the abstract Animal base class used throughout the Zoo
Management System. This class establishes the fundamental structure and behaviour
shared by all animal types within the zoo, including core identifying attributes
(name, species, age, diet, sound) and essential abstract behaviours such as
eating, sleeping, and making sound. Subclasses must implement these behaviours
to model species-specific actions within the simulation.
Author: Shaune Legayada
ID: 110444251
Username: legsd001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract base class representing a generic animal in the zoo system.

    Attributes:
        __name (str): The animal's identifying name.
        __species (str): The biological species of the animal.
        __age (int): The animal's age in years.
        __dietary_needs (str): The food type the animal consumes.
        __sound (str): The characteristic sound made by the animal.
    """

    def __init__(self, name, species, age, diet, sound):
        """
        Initialise a new Animal instance with its core identifying attributes.

        :parameter name:
        str — The animal's name.

        :parameter species:
        str — The species classification (e.g., 'Lion', 'Cobra').

        :parameter age:
        int — Age of the animal in years.

        :parameter diet:
        str — The dietary category or food type consumed.

        :parameter sound:
        str — The sound the animal makes.
        """
        self.__name = name
        self.__species = species
        self.__age = age
        self.__dietary_needs = diet
        self.__sound = sound

    # -------------------- Properties --------------------

    def get_name(self):
        """Return the animal's name."""
        return self.__name

    def set_name(self, animal_name):
        """Set the animal's name with validation."""
        if not isinstance(animal_name, str) or not animal_name.strip():
            raise ValueError("Name must be a non-empty string.")
        self.__name = animal_name

    name = property(get_name, set_name)

    def get_species(self):
        """Return the species of the animal."""
        return self.__species

    def set_species(self, animal_species):
        """Set the animal's species with validation."""
        if not isinstance(animal_species, str) or not animal_species.strip():
            raise ValueError("Species must be a non-empty string.")
        self.__species = animal_species

    species = property(get_species, set_species)

    def get_age(self):
        """Return the animal's age."""
        return self.__age

    def set_age(self, animal_age):
        """Set the animal's age with validation."""
        if not isinstance(animal_age, int):
            raise ValueError("Age must be an integer value.")
        self.__age = animal_age

    age = property(get_age, set_age)

    def get_diet(self):
        """Return the animal's dietary needs."""
        return self.__dietary_needs

    def set_diet(self, animal_diet):
        """Set the animal's diet with validation."""
        if not isinstance(animal_diet, str) or not animal_diet.strip():
            raise ValueError("Diet must be a non-empty string.")
        self.__dietary_needs = animal_diet

    diet = property(get_diet, set_diet)

    def get_sound(self):
        """Return the sound the animal makes."""
        return self.__sound

    def set_sound(self, sound):
        """Set the animal's sound with validation."""
        if not isinstance(sound, str) or not sound.strip():
            raise ValueError("Sound must be a non-empty string.")
        self.__sound = sound

    sound = property(get_sound, set_sound)

    # -------------------- Abstract Behaviours --------------------

    @abstractmethod
    def make_sound(self):
        """
        Produce the sound associated with the animal's species.
        Subclasses must override this method.
        """
        pass

    @abstractmethod
    def eat(self):
        """
        Perform species-specific eating behaviour.
        Subclasses must override this method.
        """
        pass

    @abstractmethod
    def sleeping(self):
        """
        Return a description of how the animal typically sleeps.
        Subclasses must override this method.
        """
        pass
