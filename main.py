"""
File: main.py
Description: Demonstration script for the Zoo Management System.
Author: Shaune Legayada
ID: 110444251
Username: legsd001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from mammal import Mammal
from reptile import Reptile
from bird import Bird
from enclosure import Enclosure
from staff import Staff
from health_issues import HealthIssues
from health_records import HealthRecords
from zoo import Zoo


# -------------------------------------------------------
# 1. SETUP HEALTH RECORDS AND ZOO
# -------------------------------------------------------
print("----------- ZOO INITIALISATION -----------")
health_records = HealthRecords()
zoo = Zoo(health_records)
print("Zoo and HealthRecords created.\n")

# -------------------------------------------------------
# 2. CREATE ANIMALS
# -------------------------------------------------------
print("----------- CREATING ANIMALS -----------")
leo = Mammal("Leo", "Lion", 8, "Meat", "roaring", False, "Golden Mane")
slytherin = Reptile("SLYTHERIN", "Cobra", 5, "Rodents", "Parsel Tongue", True, 30, 8)
gary = Bird("Gary", "Ibis", 5, "Maccas Fries", "Screech", 1.25, True, "Northward")

zoo.add_animal(leo)
zoo.add_animal(slytherin)
zoo.add_animal(gary)
print("Animals added to the zoo: Leo, SLYTHERIN, Gary.\n")

# -------------------------------------------------------
# 3. CREATE ENCLOSURES
# -------------------------------------------------------
print("----------- CREATING ENCLOSURES -----------")
savannah = Enclosure("Savannah Zone", 2, "Savannah", "Moderate", Mammal)
reptile_house = Enclosure("Reptile House", 3, "Jungle", "Dirty", Reptile)
aviary = Enclosure("Aviary Dome", 5, "Aviary", "Clean", Bird)

zoo.add_enclosure(savannah)
zoo.add_enclosure(reptile_house)
zoo.add_enclosure(aviary)
print("Enclosures added: Savannah Zone, Reptile House, Aviary Dome.\n")

# -------------------------------------------------------
# 4. CREATE STAFF
# -------------------------------------------------------
print("----------- CREATING STAFF -----------")
john = Staff("John", "Zookeeper")
alice = Staff("Alice", "Veterinarian")

zoo.add_staff(john)
zoo.add_staff(alice)
print("Staff added: John (Zookeeper), Alice (Veterinarian).\n")

# -------------------------------------------------------
# 5. ASSIGN ANIMALS TO ENCLOSURES
# -------------------------------------------------------
print("----------- ASSIGN ANIMALS TO ENCLOSURES -----------")
zoo.assign_animal_to_enclosure(leo, savannah)
zoo.assign_animal_to_enclosure(slytherin, reptile_house)
zoo.assign_animal_to_enclosure(gary, aviary)

print("Savannah status:")
print(savannah.enclosure_status(), "\n")

print("Reptile House status:")
print(reptile_house.enclosure_status(), "\n")

print("Aviary Dome status:")
print(aviary.enclosure_status(), "\n")

# -------------------------------------------------------
# 6. STAFF ACTIONS: FEEDING AND CLEANING
# -------------------------------------------------------
print("----------- STAFF ACTIONS -----------")
print(john.feed_animal(leo))
print(john.clean_enclosure(savannah))
print("Savannah status after cleaning:")
print(savannah.enclosure_status(), "\n")

# -------------------------------------------------------
# 7. VET RECORDS HEALTH ISSUES
# -------------------------------------------------------
print("----------- VETERINARIAN HEALTH CHECKS -----------")
leg_injury = HealthIssues("Leg injury", "2025-01-01", "High", "Rest and observation")
infection = HealthIssues("Infection", "2025-01-10", "Low", "Medication for 7 days")

print(alice.conduct_health_check(leo, health_records, leg_injury))
print(alice.conduct_health_check(gary, health_records, infection))
print()

# -------------------------------------------------------
# 8. TRY TO MOVE AN ANIMAL WITH SERIOUS HEALTH ISSUES
# -------------------------------------------------------
print("----------- ATTEMPT TO MOVE SICK ANIMAL -----------")
try:
    # Leo has a 'High' severity issue, should not be allowed to move.
    zoo.assign_animal_to_enclosure(leo, aviary)
except ValueError as error:
    print("Movement blocked:", error, "\n")

# -------------------------------------------------------
# 9. GENERATE HEALTH REPORTS
# -------------------------------------------------------
print("----------- HEALTH REPORTS -----------")
reports = zoo.generate_health_reports()
for report in reports:
    print(report)
    print("-" * 40)

print("----------- END OF ZOO DEMONSTRATION -----------")
