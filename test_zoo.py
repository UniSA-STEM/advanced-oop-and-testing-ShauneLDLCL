"""
File: test_zoo.py
Description: Tests integration of Zoo operations including animal assignment,
enclosure compatibility, and health-based movement blocking. Validates that the
central Zoo controller correctly interoperates with enclosures and the
HealthRecords system to enforce assignment rules.
Author: Shaune Legayada
ID: 110444251
Username: legsd001
This is my own work as defined by the University's Academic Integrity Policy.
"""

import pytest
from zoo import Zoo
from mammal import Mammal
from enclosure import Enclosure
from health_records import HealthRecords
from health_issues import HealthIssues

# -------------------- Fixtures --------------------

@pytest.fixture
def lion():
    return Mammal("Leo", "Lion", 8, "Meat", "roaring", False, "Golden Mane")

@pytest.fixture
def enclosure():
    return Enclosure("Savannah Zone", 2, "Savannah", "Clean", Mammal)

@pytest.fixture
def records():
    return HealthRecords()

@pytest.fixture
def zoo(records):
    return Zoo(records)

# -------------------- Tests --------------------

def test_assign_animal_to_enclosure(zoo, lion, enclosure):
    """Ensure healthy animals can be assigned to enclosures."""
    zoo.add_animal(lion)
    zoo.add_enclosure(enclosure)
    zoo.assign_animal_to_enclosure(lion, enclosure)
    assert lion in enclosure.animal_species

def test_block_assignment_due_to_health(zoo, records, lion, enclosure):
    """Ensure animals with severe conditions cannot be moved."""
    issue = HealthIssues("Injury", "2025-02-01", "High", "Rest")
    records.add_issue(lion, issue)
    with pytest.raises(ValueError):
        zoo.assign_animal_to_enclosure(lion, enclosure)
