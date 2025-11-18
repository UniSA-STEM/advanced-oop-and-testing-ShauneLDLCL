'''
File: bird.py
Description: Defines the Bird subclass which extends the Animal base class.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

class Bird(Animal):
    def __init__(self, name, species, age, diet, sound, wing_span, can_fly, migration_pattern):
        super().__init__(name, species, age, diet, sound)
        self.__wing_span = wing_span
        self.__can_fly = can_fly
        self.__migration_pattern = migration_pattern

    def get_wing_span(self):
        return self.__wing_span

    def set_wing_span(self, span):
        if not isinstance(span, (float, int)) or span <= 0:
            raise ValueError("Wing span must be a positive number.")
        self.__wing_span = float(span)

    wing_span = property(get_wing_span, set_wing_span)

    def get_can_fly(self):
        return self.__can_fly

    def set_can_fly(self, fly):
        if not isinstance(fly, bool):
            raise ValueError("can_fly must be a boolean value.")
        self.__can_fly = fly

    can_fly = property(get_can_fly, set_can_fly)

    def get_migration_pattern(self):
        return self.__migration_pattern

    def set_migration_pattern(self, pattern):
        if not isinstance(pattern, str) or not pattern.strip():
            raise ValueError("Migration pattern must be a non-empty string.")
        self.__migration_pattern = pattern

    migration_pattern = property(get_migration_pattern, set_migration_pattern)

    def make_sound(self):
        return f"{self.name} an {self.species} makes a {self.sound} sound."

    def eat(self):
        return f"{self.name} pecks at its {self.diet.lower()}."

    def sleeping(self):
        return f"{self.name} perches high on a branch and tucks its head under its wing."

    def fly(self):
        if not self.__can_fly:
            return f"{self.name} cannot fly and remains on the ground."

        if self.__wing_span > 2.0:
            return f"{self.name} spreads its massive {self.__wing_span}m wings and soars majestically."
        else:
            return f"{self.name} flaps its {self.__wing_span}m wings rapidly and takes off into the sky."

    def migrate(self):
        if not self.__can_fly or self.__migration_pattern == "None":
            return f"{self.name} does not migrate."
        return f"{self.name} migrates following the {self.__migration_pattern} pattern every season."

    def build_nest(self):
        return f"{self.name} gathers twigs and leaves to build a comfortable nest."

bin_chicken = Bird("Gary", "Ibis", 5, "Maccas Fries", "Screech", 1.25, True, "Northward")
print(bin_chicken.make_sound())
print(bin_chicken.eat())
print(bin_chicken.sleeping())
print(bin_chicken.fly())
print(bin_chicken.migrate())
print(bin_chicken.build_nest())

print(20*"--")

Albatross = Bird ("Larry", "Albatross", 3, "Fish", "CAWWW", 3, True, "Southward")
print(Albatross.make_sound())
print(Albatross.eat())
print(Albatross.sleeping())
print(Albatross.fly())
print(Albatross.migrate())
print(Albatross.build_nest())

print(20*"--")

Chicken = Bird ("Barry", "Chicken", 4, "Eggs", "BAWK", 0.5, False, "None")
print(Chicken.make_sound())
print(Chicken.eat())
print(Chicken.sleeping())
print(Chicken.fly())
print(Chicken.migrate())
print(Chicken.build_nest())