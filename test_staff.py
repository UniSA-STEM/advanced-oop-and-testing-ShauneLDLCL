"""
File: test_staff.py
Description: Tests for Staff feeding and enclosure cleaning behaviour.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
"""

import pytest
from staff import Staff
from mammal import Mammal
from enclosure import Enclosure


@pytest.fixture
def keeper():
    return Staff("John", "Zookeeper")


@pytest.fixture
def lion():
    return Mammal("Leo", "Lion", 8, "Meat", "roaring", False, "Golden Mane")


@pytest.fixture
def enclosure():
    return Enclosure("Savannah Zone", 3, "Savannah", "Dirty", Mammal)


def test_feed_animal(keeper, lion):
    result = keeper.feed_animal(lion)
    assert "feeds" in result


def test_clean_enclosure(keeper, enclosure):
    result = keeper.clean_enclosure(enclosure)
    assert enclosure.get_cleanliness() == "Clean"
    assert "cleaned" in result


def test_clean_enclosure_not_authorised():
    staff = Staff("Bob", "Vet")
    enclosure = Enclosure("Test", 1, "Grasslands", "Dirty", Mammal)
    result = staff.clean_enclosure(enclosure)
    assert "not authorised" in result
