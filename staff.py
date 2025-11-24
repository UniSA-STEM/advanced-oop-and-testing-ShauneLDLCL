'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal
from enclosure import Enclosure
from health_records import HealthRecords
from health_issues import HealthIssues

class Staff:
    def __init__(self, name, role):
        self.__name = name
        self.__role = role

    def get_name(self):
        return self.__name

    def set_name(self, staff_name):
        if not isinstance(staff_name, str) or not staff_name.strip():
            raise ValueError("Staff name must be a non-empty string.")
        self.__name = staff_name

    staff_name = property(get_name, set_name)

    def get_role(self):
        return self.__role

    def set_role(self, staff_role):
        if not isinstance(staff_role, str) or not staff_role.strip():
            raise ValueError("Role must be a non-empty string.")
        self.__role = staff_role

    staff_role = property(get_role, set_role)

    def feed_animal(self, animal):
        if not isinstance(animal, Animal):
            raise ValueError("Only valid Animal objects may be fed.")
        return f"{self.__name} feeds {animal.get_name()}. {animal.eat()}"

    def clean_enclosure(self, enclosure):
        if self.__role.lower() != "zookeeper":
            return f"{self.__name} is not authorised to clean enclosures."

        if not isinstance(enclosure, Enclosure):
            raise ValueError("Can only clean an Enclosure object.")

        enclosure.set_cleanliness("Clean")
        return f"{self.__name} cleaned the {enclosure.get_name()} enclosure."

    def conduct_health_check(self, animal, health_records, issue):

        if not isinstance(animal, Animal):
            raise ValueError("Health checks can only be recorded for Animal objects.")

        if not isinstance(health_records, HealthRecords):
            raise ValueError("health_records must be a HealthRecords object.")

        if not isinstance(issue, HealthIssues):
            raise ValueError("issue must be a HealthIssues object.")

        if self.__role.lower() != "veterinarian":
            return f"{self.__name} is not authorised to record health issues."

        health_records.add_issue(animal, issue)
        return f"{self.__name} recorded a health issue for {animal.get_name()}."