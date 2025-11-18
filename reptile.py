'''
File: reptile.py
Description: Defines the Reptile subclass which extends the Animal base class.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

class Reptile(Animal):
    def __init__(self, name, species, age, diet, sound, is_venomous, preferred_temperature, shedding_frequency):
        super().__init__(name, species, age, diet, sound)
        self.__is_venomous = is_venomous
        self.__preferred_temperature = preferred_temperature
        self.__shedding_frequency = shedding_frequency

    def get_is_venomous(self):
        return self.__is_venomous

    def set_is_venomous(self, venomous):
        if not isinstance(venomous, bool):
            raise ValueError("is_venomous must be a boolean value.")
        self.__is_venomous = venomous

    is_venomous = property(get_is_venomous, set_is_venomous)

    def get_preferred_temperature(self):
        return self.__preferred_temperature

    def set_preferred_temperature(self, temperature):
        if not isinstance(temperature, (float, int)) or temperature <= 0:
            raise ValueError("Preferred temperature must be a positive number.")
        self.__preferred_temperature = float(temperature)

    preferred_temperature = property(get_preferred_temperature, set_preferred_temperature)

    def get_shedding_frequency(self):
        return self.__shedding_frequency

    def set_shedding_frequency(self, frequency):
        if not isinstance(frequency, int) or frequency <= 0:
            raise ValueError("Shedding frequency must be a positive integer (in weeks).")
        self.__shedding_frequency = frequency

    shedding_frequency = property(get_shedding_frequency, set_shedding_frequency)

    def make_sound(self):
        return f"{self.name} (a {self.species}) makes a {self.sound} sound."

    def eat(self):
        if self.__is_venomous:
            return f"{self.name} injects venom into its prey before consuming the {self.diet.lower()}."
        return f"{self.name} ambushes and swallows its {self.diet.lower()} whole."

    def sleeping(self):
        return f"{self.name} sleeps under warm rocks to regulate its body temperature."

    def bask(self):
        return f"{self.name} basks in the sun to maintain a temperature around {self.__preferred_temperature}°C."

    def shed_skin(self):
        return f"{self.name} sheds its old skin every {self.__shedding_frequency} weeks to grow."

    def bite(self):
        if self.__is_venomous:
            return f"{self.name} strikes quickly and delivers a potent venomous bite!"
        return f"{self.name} strikes, but it is not venomous."

basalisk = Reptile("SLYTHERIN", "Cobra", 5, "Rodents", "Parsel Tongue", True, 30, 8)
print(basalisk.make_sound())
print(basalisk.eat())
print(basalisk.sleeping())
print(basalisk.bask())
print(basalisk.shed_skin())
print(basalisk.bite())