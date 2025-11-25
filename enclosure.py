"""
File: enclosure.py
Description: Defines the Enclosure class responsible for managing habitat zones within the Zoo
Management System. Each enclosure enforces strict validation rules for environment type,
cleanliness level, capacity limits, and compatible species. The class maintains a collection
of animals currently housed, supports adding and removing animals with validation, and provides
clear formatted reports summarising the enclosure’s condition. This module ensures the safe
and structured organisation of animals according to habitat requirements.
Author: Shaune Legayada
ID: 110444251
Username: legsd001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal

class Enclosure:
    CLEANLINESS = {"Clean", "Moderate", "Dirty"}
    ENVIRONMENTS = {"Savannah", "Aquatic", "Aviary", "Jungle", "Desert", "Arctic", "Rainforest", "Grasslands", "Wetlands"}

    def __init__(self, name, size, environment_type, cleanliness_level, compatible_species):
        """
        Initialise a new enclosure with habitat settings and animal capacity.

        :param name: str
            The display name of the enclosure.
        :param size: int
            Maximum number of animals allowed.
        :param environment_type: str
            Habitat type selected from ENVIRONMENTS.
        :param cleanliness_level: str
            Current cleanliness state selected from CLEANLINESS.
        :param compatible_species: type
            The Animal subclass allowed to be housed inside.

        Behaviour:
        Stores all attributes as provided. Validation occurs in setters where applicable.
        """
        self.__name = name
        self.__environment_type = environment_type
        self.__size = size
        self.__cleanliness = cleanliness_level
        self.__compatible_species = compatible_species
        self.__animal_species = []

    def get_name(self):
        """
        Return the enclosure name.

        :returns: str
        """
        return self.__name

    def set_name(self, enclosure_name):
        """
        Set the enclosure name with validation.

        :param enclosure_name: str
        :raises ValueError: If the name is empty or invalid.
        """
        if not isinstance(enclosure_name, str) or not enclosure_name.strip():
            raise ValueError("Enclosure name must be a non-empty string.")
        self.__name = enclosure_name

    enclosure_name = property(get_name, set_name)

    def get_environment_type(self):
        """
        Return the habitat/environment type.

        :returns: str
        """
        return self.__environment_type

    def set_environment_type(self, environment_type):
        """
        Set the environment type with validation.

        :param environment_type: str
        :raises ValueError: If environment type is invalid.
        """
        if not isinstance(environment_type, str) or not environment_type.strip():
            raise ValueError("Environment type must be a non-empty string.")
        if environment_type not in Enclosure.ENVIRONMENTS:
            raise ValueError(f"Environment must be one of: {Enclosure.ENVIRONMENTS}")
        self.__environment_type = environment_type

    environment_type = property(get_environment_type, set_environment_type)

    def get_size(self):
        """
        Return the maximum capacity of the enclosure.

        :returns: int
        """
        return self.__size

    def set_size(self, enclosure_size):
        """
        Set the enclosure size with validation.

        :param enclosure_size: int
        :raises ValueError: If size is invalid or smaller than current occupancy.
        """
        if not isinstance(enclosure_size, int) or enclosure_size <= 0:
            raise ValueError("Size must be a positive integer.")
        if enclosure_size < len(self.__animal_species):
            raise ValueError("Size cannot be smaller than the current number of animals.")
        self.__size = enclosure_size

    enclosure_size = property(get_size, set_size)

    def get_cleanliness(self):
        """
        Return the cleanliness level.

        :returns: str
        """
        return self.__cleanliness

    def set_cleanliness(self, cleanliness_level):
        """
        Set the enclosure cleanliness state.

        :param cleanliness_level: str
        :raises ValueError: If the state is invalid.
        """
        if not isinstance(cleanliness_level, str) or not cleanliness_level.strip():
            raise ValueError("Cleanliness must be a non-empty string.")
        if cleanliness_level not in Enclosure.CLEANLINESS:
            raise ValueError(f"Cleanliness must be one of: {Enclosure.CLEANLINESS}")
        self.__cleanliness = cleanliness_level

    cleanliness_level = property(get_cleanliness, set_cleanliness)

    def get_compatible_species(self):
        """
        Return the allowed species type for this enclosure.

        :returns: type
        """
        return self.__compatible_species

    compatible_species = property(get_compatible_species)

    def get_animals(self):
        """
        Return all animals housed in the enclosure.

        :returns: list[Animal]
        """
        return (self.__animal_species)

    animal_species = property(get_animals)

    def add_animal(self, animal):
        """
        Add an animal into the enclosure.

        :param animal: Animal
        :raises ValueError:
            - If object is not an Animal
            - If incompatible species
            - If enclosure is full
        """
        if not isinstance(animal, Animal):
            raise ValueError("Only Animal objects may be added to an enclosure.")

        if not isinstance(animal, self.__compatible_species):
            raise ValueError(f"This enclosure only accepts {self.__compatible_species.__name__} types")

        if len(self.__animal_species) >= self.__size:
            raise ValueError("Enclosure is full.")

        self.__animal_species.append(animal)

    def remove_animal(self, animal):
        """
        Remove an animal from the enclosure.

        :param animal: Animal
        :raises ValueError: If the animal is not currently housed.
        """
        if animal not in self.__animal_species:
            raise ValueError("This animal is not in the enclosure.")
        self.__animal_species.remove(animal)

    def enclosure_status(self):
        """
        Return a formatted summary containing:
        - Enclosure name
        - Environment type
        - Cleanliness level
        - Animal list
        - Occupancy/Capacity

        :returns: str
        """
        animal_names = (", ".join(animal.get_name() for animal in self.__animal_species) if self.__animal_species else "No animals")

        return (
            f"Enclosure: {self.__name}\n"
            f"Environment: {self.__environment_type}\n"
            f"Cleanliness: {self.__cleanliness}\n"
            f"Animals: {animal_names}\n"
            f"Capacity: {len(self.__animal_species)}/{self.__size}"
        )

    def __str__(self):
        """
        Return a readable display of the enclosure status.

        :returns: str
        """
        return self.enclosure_status()
