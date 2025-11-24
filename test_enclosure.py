"""
File: test_enclosure.py
Description: Tests for Enclosure class including species checks, size limits, and cleanliness.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
"""

import pytest
from enclosure import Enclosure
from mammal import Mammal


@pytest.fixture
def lion():
    return Mammal("Mufasa", "Lion", 8, "Meat", "roaring", False, "Golden Mane")


@pytest.fixture
def enclosure():
    return Enclosure("Savannah Zone", 2, "Savannah", "Moderate", Mammal)


def test_add_animal_success(enclosure, lion):
    enclosure.add_animal(lion)
    assert len(enclosure.animal_species) == 1


def test_add_incompatible_animal(enclosure, lion):
    class FakeAnimal:
        pass

    fake = FakeAnimal()

    with pytest.raises(ValueError):
        enclosure.add_animal(fake)


def test_enclosure_full(enclosure, lion):
    enclosure.add_animal(lion)
    enclosure.add_animal(Mammal("Simba", "Lion", 5, "Meat", "roaring", False, "Soft Mane"))

    with pytest.raises(ValueError):
        enclosure.add_animal(lion)


def test_cleanliness_update(enclosure):
    enclosure.set_cleanliness("Clean")
    assert enclosure.get_cleanliness() == "Clean"
