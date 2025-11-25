"""
File: reptile.py
Description: Implements the Reptile subclass of the Animal base class, modelling
behaviours and traits unique to reptiles such as venom status, shedding frequency,
and preferred temperature. This class provides species-specific implementations
for required behaviours and introduces additional reptile-specific actions.
Author: Shaune Legayada
ID: 110444251
Username: legsd001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal

class Reptile(Animal):
    """
    Represents a reptile in the zoo, extending the Animal base class.

    Attributes:
        __is_venomous (bool): Whether the reptile uses venom.
        __preferred_temperature (float): Ideal body temperature environment.
        __shedding_frequency (int): Frequency of skin shedding (weeks).
    """

    def __init__(self, name, species, age, diet, sound, is_venomous, preferred_temperature, shedding_frequency):
        """
        Create a Reptile instance with reptile-specific characteristics.

        :parameter is_venomous:
        bool — Whether the reptile has venom.

        :parameter preferred_temperature:
        float — The ideal body temperature for the reptile.

        :parameter shedding_frequency:
        int — Weeks between each shedding cycle.
        """
        super().__init__(name, species, age, diet, sound)
        self.__is_venomous = is_venomous
        self.__preferred_temperature = preferred_temperature
        self.__shedding_frequency = shedding_frequency

    # -------------------- Properties --------------------

    def get_is_venomous(self):
        """Return True if the reptile is venomous."""
        return self.__is_venomous

    def set_is_venomous(self, venomous):
        """Set venom status with validation."""
        if not isinstance(venomous, bool):
            raise ValueError("is_venomous must be a boolean value.")
        self.__is_venomous = venomous

    is_venomous = property(get_is_venomous, set_is_venomous)

    def get_preferred_temperature(self):
        """Return the reptile's preferred temperature."""
        return self.__preferred_temperature

    def set_preferred_temperature(self, temperature):
        """Set preferred temperature with validation."""
        if not isinstance(temperature, (float, int)) or temperature <= 0:
            raise ValueError("Preferred temperature must be a positive number.")
        self.__preferred_temperature = float(temperature)

    preferred_temperature = property(get_preferred_temperature, set_preferred_temperature)

    def get_shedding_frequency(self):
        """Return the shedding frequency in weeks."""
        return self.__shedding_frequency

    def set_shedding_frequency(self, frequency):
        """Set shedding frequency with validation."""
        if not isinstance(frequency, int) or frequency <= 0:
            raise ValueError("Shedding frequency must be a positive integer (in weeks).")
        self.__shedding_frequency = frequency

    shedding_frequency = property(get_shedding_frequency, set_shedding_frequency)

    # -------------------- Behaviour Implementations --------------------

    def make_sound(self):
        """Return the reptile’s vocal sound."""
        return f"{self.name} (a {self.species}) makes a {self.sound} sound."

    def eat(self):
        """Return eating behaviour depending on venom status."""
        if self.__is_venomous:
            return f"{self.name} injects venom into its prey before consuming the {self.diet.lower()}."
        return f"{self.name} ambushes and swallows its {self.diet.lower()} whole."

    def sleeping(self):
        """Return the reptile’s sleeping behaviour description."""
        return f"{self.name} sleeps under warm rocks to regulate its body temperature."

    # -------------------- Reptile-specific Behaviours --------------------

    def bask(self):
        """Return a behaviour describing basking for warmth."""
        return f"{self.name} basks in the sun to maintain a temperature around {self.__preferred_temperature}°C."

    def shed_skin(self):
        """Return a behaviour describing the reptile shedding its skin."""
        return f"{self.name} sheds its old skin every {self.__shedding_frequency} weeks to grow."

    def bite(self):
        """Return a description of the reptile biting behaviour."""
        if self.__is_venomous:
            return f"{self.name} strikes quickly and delivers a potent venomous bite!"
        return f"{self.name} strikes, but it is not venomous."
