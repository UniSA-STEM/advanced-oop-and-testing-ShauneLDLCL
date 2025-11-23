from animal import Animal
from staff import Staff
from enclosure import Enclosure
from health_records import HealthRecords
class Zoo:
    def __init__(self, health_records):
        self.__animals = []
        self.__enclosures = []
        self.__staff = []
        self.__health_records = health_records

    def add_animal(self, animal):
        if not isinstance(animal, Animal):
            raise ValueError("Only Animal instances can be added.")
        self.__animals.append(animal)

    def get_animals(self):
        return self.__animals

    def add_staff(self, staff_member):
        if not isinstance(staff_member, Staff):
            raise ValueError("Only Staff instances can be added.")
        self.__staff.append(staff_member)

    def get_enclosure(self):
        return self.__enclosures

    def add_enclosure(self, enclosure):
        if not isinstance(enclosure, Enclosure):
            raise ValueError("Only Enclosure instances can be added.")
        self.__enclosures.append(enclosure)

    def assign_animal_to_enclosure(self, animal, enclosure):
        if self.__health_records.severity_level(animal):
            raise ValueError(animal.get_name() + " cannot be moved due to health.")
        enclosure.add_animal(animal)




