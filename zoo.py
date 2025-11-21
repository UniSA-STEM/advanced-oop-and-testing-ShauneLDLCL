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




