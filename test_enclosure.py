"""
File: test_enclosure.py
Description: Contains unit tests for verifying Enclosure behaviour including
species validation, capacity enforcement, cleanliness modification, and correct
animal tracking. Ensures enclosures behave predictably and match assignment
specifications.
Author: Shaune Legayada
ID: 110444251
Username: legsd001
This is my own work as defined by the University's Academic Integrity Policy.
"""

import pytest
from enclosure import Enclosure
from mammal import Mammal

# -------------------- Fixtures --------------------

@pytest.fixture
def lion():
    return Mammal("Mufasa", "Lion", 8, "Meat", "roaring", False, "Golden Mane")

@pytest.fixture
def enclosure():
    return Enclosure("Savannah Zone", 2, "Savannah", "Moderate", Mammal)

# -------------------- Tests --------------------

def test_add_animal_success(enclosure, lion):
    """Ensure valid animals can be added."""
    enclosure.add_animal(lion)
    assert len(enclosure.animal_species) == 1

def test_add_incompatible_animal(enclosure, lion):
    """Ensure invalid types cannot be added to an enclosure."""
    class FakeAnimal:
        pass
    fake = FakeAnimal()
    with pytest.raises(ValueError):
        enclosure.add_animal(fake)

def test_enclosure_full(enclosure, lion):
    """Ensure enclosure rejects animals when capacity is reached."""
    enclosure.add_animal(lion)
    enclosure.add_animal(Mammal("Simba", "Lion", 5, "Meat", "roaring", False, "Soft Mane"))
    with pytest.raises(ValueError):
        enclosure.add_animal(lion)

def test_cleanliness_update(enclosure):
    """Ensure cleanliness can be updated properly."""
    enclosure.set_cleanliness("Clean")
    assert enclosure.get_cleanliness() == "Clean"
