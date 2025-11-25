"""
File: bird.py
Description: Implements the Bird subclass of the Animal base class, modelling
avian characteristics such as wing span, flight capability, nesting behaviour,
and migration patterns. Provides implementations for abstract methods along with
unique avian behaviours such as flying and nest-building.
Author: Shaune Legayada
ID: 110444251
Username: legsd001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal

class Bird(Animal):
    """
    Represents a bird in the zoo ecosystem.

    Attributes:
        __wing_span (float): Wing span in meters.
        __can_fly (bool): Indicates whether the bird can fly.
        __migration_pattern (str): Pattern followed during migration.
    """

    def __init__(self, name, species, age, diet, sound, wing_span, can_fly, migration_pattern):
        """Initialise a Bird with additional avian characteristics."""
        super().__init__(name, species, age, diet, sound)
        self.__wing_span = wing_span
        self.__can_fly = can_fly
        self.__migration_pattern = migration_pattern

    # -------------------- Properties --------------------

    def get_wing_span(self):
        """Return the bird’s wing span."""
        return self.__wing_span

    def set_wing_span(self, span):
        """Set wing span with validation."""
        if not isinstance(span, (float, int)) or span <= 0:
            raise ValueError("Wing span must be a positive number.")
        self.__wing_span = float(span)

    wing_span = property(get_wing_span, set_wing_span)

    def get_can_fly(self):
        """Return True if the bird can fly."""
        return self.__can_fly

    def set_can_fly(self, fly):
        """Set flying capability with validation."""
        if not isinstance(fly, bool):
            raise ValueError("can_fly must be a boolean value.")
        self.__can_fly = fly

    can_fly = property(get_can_fly, set_can_fly)

    def get_migration_pattern(self):
        """Return the migration pattern."""
        return self.__migration_pattern

    def set_migration_pattern(self, pattern):
        """Set migration pattern with validation."""
        if not isinstance(pattern, str) or not pattern.strip():
            raise ValueError("Migration pattern must be a non-empty string.")
        self.__migration_pattern = pattern

    migration_pattern = property(get_migration_pattern, set_migration_pattern)

    # -------------------- Behaviour Implementations --------------------

    def make_sound(self):
        """Return the bird’s sound."""
        return f"{self.name} an {self.species} makes a {self.sound} sound."

    def eat(self):
        """Return a description of the bird consuming food."""
        return f"{self.name} pecks at its {self.diet.lower()}."

    def sleeping(self):
        """Return bird's typical sleeping behaviour."""
        return f"{self.name} perches high on a branch and tucks its head under its wing."

    # -------------------- Bird-specific Behaviours --------------------

    def fly(self):
        """Return a description of the bird flying or inability to fly."""
        if not self.__can_fly:
            return f"{self.name} cannot fly and remains on the ground."

        if self.__wing_span > 2.0:
            return f"{self.name} spreads its massive {self.__wing_span}m wings and soars majestically."
        return f"{self.name} flaps its {self.__wing_span}m wings rapidly and takes off into the sky."

    def migrate(self):
        """Return description of migration behaviour."""
        if not self.__can_fly or self.__migration_pattern == "None":
            return f"{self.name} does not migrate."
        return f"{self.name} migrates following the {self.__migration_pattern} pattern every season."

    def build_nest(self):
        """Return nest-building behaviour description."""
        return f"{self.name} gathers twigs and leaves to build a comfortable nest."
