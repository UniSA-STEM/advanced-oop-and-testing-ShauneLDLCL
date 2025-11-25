"""
File: zoo.py
Description: Defines the Zoo class which acts as the central controller for
the Zoo Management System. It coordinates animals, staff, enclosures, and
health records, handling interactions such as assigning animals to enclosures,
blocking movement due to severe health conditions, and generating consolidated
health reports. The class ensures proper validation and system-wide consistency.
Author: Shaune Legayada
ID: 110444251
Username: legsd001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal
from staff import Staff
from enclosure import Enclosure
from health_records import HealthRecords

class Zoo:
    """
    Represents the entire zoo environment.

    Attributes:
        __animals (list[Animal]): All animals registered in the zoo.
        __enclosures (list[Enclosure]): All enclosure zones.
        __staff (list[Staff]): All available staff members.
        __health_records (HealthRecords): Centralised health record manager.
    """

    def __init__(self, health_records):
        """Initialise the zoo with an external HealthRecords manager."""
        self.__animals = []
        self.__enclosures = []
        self.__staff = []
        self.__health_records = health_records

    # -------------------- Add Methods --------------------

    def add_animal(self, animal):
        """Add an Animal instance to the zoo."""
        if not isinstance(animal, Animal):
            raise ValueError("Only Animal instances can be added.")
        self.__animals.append(animal)

    def get_animals(self):
        """Return list of animals registered in the zoo."""
        return self.__animals

    def add_staff(self, staff_member):
        """Add a Staff instance to the zoo."""
        if not isinstance(staff_member, Staff):
            raise ValueError("Only Staff instances can be added.")
        self.__staff.append(staff_member)

    def get_enclosure(self):
        """Return list of enclosures registered in the zoo."""
        return self.__enclosures

    def add_enclosure(self, enclosure):
        """Add an Enclosure instance to the zoo."""
        if not isinstance(enclosure, Enclosure):
            raise ValueError("Only Enclosure instances can be added.")
        self.__enclosures.append(enclosure)

    # -------------------- Core Behaviour --------------------

    def assign_animal_to_enclosure(self, animal, enclosure):
        """
        Attempt to move an animal into an enclosure.

        Behaviour:
        - Blocks movement if the animal has any High/Critical severity issues.
        """
        if self.__health_records.severity_level(animal):
            raise ValueError(animal.get_name() + " cannot be moved due to health.")

        enclosure.add_animal(animal)

    def generate_health_reports(self):
        """
        Generate health reports for all animals with recorded issues.

        :returns:
        list[str] — A list of full medical reports.
        """
        reports = []
        animals_with_issues = self.__health_records.get_animals_with_issues()

        index = 0
        while index < len(animals_with_issues):
            animal = animals_with_issues[index]
            report = self.__health_records.generate_report(animal)
            reports.append(report)
            index += 1

        return reports
