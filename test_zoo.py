"""
File: test_zoo.py
Description: Tests for Zoo class interactions linking animals, enclosures, staff, and health.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
"""

import pytest
from zoo import Zoo
from mammal import Mammal
from staff import Staff
from enclosure import Enclosure
from health_records import HealthRecords
from health_issues import HealthIssues


@pytest.fixture
def lion():
    return Mammal("Leo", "Lion", 8, "Meat", "roaring", False, "Golden Mane")


@pytest.fixture
def enclosure():
    return Enclosure("Savannah Zone", 2, "Savannah", "Clean", Mammal)


@pytest.fixture
def staff():
    return Staff("John", "Zookeeper")


@pytest.fixture
def records():
    return HealthRecords()


@pytest.fixture
def zoo(records):
    return Zoo(records)


def test_assign_animal_to_enclosure(zoo, lion, enclosure):
    zoo.add_animal(lion)
    zoo.add_enclosure(enclosure)
    zoo.assign_animal_to_enclosure(lion, enclosure)
    assert lion in enclosure.animal_species


def test_block_assignment_due_to_health(zoo, records, lion, enclosure):
    issue = HealthIssues("Injury", "2025-02-01", "High", "Rest")
    records.add_issue(lion, issue)

    with pytest.raises(ValueError):
        zoo.assign_animal_to_enclosure(lion, enclosure)
