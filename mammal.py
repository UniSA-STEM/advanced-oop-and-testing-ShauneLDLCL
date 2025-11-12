'''
File: mammal.py
Description: Defines the Mammal subclass which extends the Animal base class.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

class Mammal(Animal):
    def __init__(self, name, species, age, diet, sound, is_nocturnal, hair_type):
        super().__init__(name, species, age, diet, sound)
        self.__is_nocturnal = is_nocturnal
        self.__hair_type = hair_type

    def get_is_nocturnal(self):
        return self.__is_nocturnal

    def set_is_nocturnal(self, nocturnal):
        if not isinstance(nocturnal, bool):
            raise ValueError("is_nocturnal must be a boolean value.")
        self.__is_nocturnal = nocturnal

    is_nocturnal = property(get_is_nocturnal, set_is_nocturnal)

    def get_hair_type(self):
        return self.__hair_type

    def set_hair_type(self, hair):
        if not isinstance(hair, str) or not hair.strip():
            raise ValueError("hair_type must be a non-empty string.")
        self.__hair_type = hair

    hair_type = property(get_hair_type, set_hair_type)

    def make_sound(self):
        return f"{self.name} (a {self.species}) makes a {self.sound} sound."

    def eat(self):
        return f"{self.name} devours its {self.diet.lower()}."

    def sleeping(self):
        if self.__is_nocturnal:
            return f"{self.name} curls up in its den and sleeps during the day."
        else:
            return f"{self.name} rests peacefully in the shade at night."

    def groom(self):
        return f"{self.name} grooms its {self.hair_type.lower()} to keep it clean and shiny."


lion = Mammal("Leo", "Lion", 8, "Meat", "roaring", False, "Golden Mane")
print(lion.make_sound())
print(lion.eat())
print(lion.sleeping())
print(lion.groom())
