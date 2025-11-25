"""
File: mammal.py
Description: Implements the Mammal subclass of the Animal base class, modelling
characteristics unique to mammals such as nocturnal behaviour and fur/hair type.
This class defines species-specific implementations for required behaviours such
as making sound, eating, and sleeping, and introduces a unique grooming behaviour.
Author: Shaune Legayada
ID: 110444251
Username: legsd001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal

class Mammal(Animal):
    """
    Represents a mammal within the zoo, extending the base Animal class.

    Attributes:
        __is_nocturnal (bool): Indicates whether the mammal is active at night.
        __hair_type (str): The hair or fur type associated with the mammal.
    """

    def __init__(self, name, species, age, diet, sound, is_nocturnal, hair_type):
        """
        Create a Mammal instance with additional mammalian characteristics.

        :parameter is_nocturnal:
        bool — Whether the mammal is active primarily at night.

        :parameter hair_type:
        str — Description of the mammal's hair or fur.
        """
        super().__init__(name, species, age, diet, sound)
        self.__is_nocturnal = is_nocturnal
        self.__hair_type = hair_type

    # -------------------- Properties --------------------

    def get_is_nocturnal(self):
        """Return True if the mammal is nocturnal."""
        return self.__is_nocturnal

    def set_is_nocturnal(self, nocturnal):
        """Set nocturnal behaviour with validation."""
        if not isinstance(nocturnal, bool):
            raise ValueError("is_nocturnal must be a boolean value.")
        self.__is_nocturnal = nocturnal

    is_nocturnal = property(get_is_nocturnal, set_is_nocturnal)

    def get_hair_type(self):
        """Return the mammal's hair or fur type."""
        return self.__hair_type

    def set_hair_type(self, hair):
        """Set the hair/fur type with validation."""
        if not isinstance(hair, str) or not hair.strip():
            raise ValueError("hair_type must be a non-empty string.")
        self.__hair_type = hair

    hair_type = property(get_hair_type, set_hair_type)

    # -------------------- Behaviour Implementations --------------------

    def make_sound(self):
        """Return the vocalisation sound of the mammal."""
        return f"{self.name} (a {self.species}) makes a {self.sound} sound."

    def eat(self):
        """Return a description of the mammal consuming its food."""
        return f"{self.name} devours its {self.diet.lower()}."

    def sleeping(self):
        """Return a sleeping behaviour description based on nocturnal status."""
        if self.__is_nocturnal:
            return f"{self.name} curls up in its den and sleeps during the day."
        return f"{self.name} rests peacefully in the shade at night."

    def groom(self):
        """
        Return a description of the mammal grooming itself.
        This behaviour is unique to mammals in the system.
        """
        return f"{self.name} grooms its {self.hair_type.lower()} to keep it clean and shiny."
