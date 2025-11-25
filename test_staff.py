"""
File: test_staff.py
Description: Tests staff functionality including animal feeding, enclosure
cleaning, and permission checks for role-restricted operations. Ensures the Staff
class correctly enforces behavioural rules and operates safely when interacting
with other system classes.
Author: Shaune Legayada
ID: 110444251
Username: legsd001
This is my own work as defined by the University's Academic Integrity Policy.
"""

import pytest
from staff import Staff
from mammal import Mammal
from enclosure import Enclosure

# -------------------- Fixtures --------------------

@pytest.fixture
def keeper():
    return Staff("John", "Zookeeper")

@pytest.fixture
def lion():
    return Mammal("Leo", "Lion", 8, "Meat", "roaring", False, "Golden Mane")

@pytest.fixture
def enclosure():
    return Enclosure("Savannah Zone", 3, "Savannah", "Dirty", Mammal)

# -------------------- Tests --------------------

def test_feed_animal(keeper, lion):
    """Ensure feeding behaviour returns correct formatted string."""
    result = keeper.feed_animal(lion)
    assert "feeds" in result

def test_clean_enclosure(keeper, enclosure):
    """Ensure zookeepers can clean enclosures."""
    result = keeper.clean_enclosure(enclosure)
    assert enclosure.get_cleanliness() == "Clean"
    assert "cleaned" in result

def test_clean_enclosure_not_authorised():
    """Ensure non-zookeeper staff cannot clean enclosures."""
    staff = Staff("Bob", "Vet")
    enclosure = Enclosure("Test", 1, "Grasslands", "Dirty", Mammal)
    result = staff.clean_enclosure(enclosure)
    assert "not authorised" in result
