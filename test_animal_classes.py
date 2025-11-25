"""
File: test_animal_classes.py
Description: Unit tests for verifying correct behaviour of the Mammal, Reptile,
and Bird subclasses. Tests ensure each subclass correctly implements required
Animal abstract methods and species-specific behaviours. This file validates
sound production, eating, sleeping, and unique actions for each subclass.
Author: Shaune Legayada
ID: 110444251
Username: legsd001
This is my own work as defined by the University's Academic Integrity Policy.
"""

import pytest
from mammal import Mammal
from reptile import Reptile
from bird import Bird

# -------------------- Fixtures --------------------

@pytest.fixture
def lion():
    return Mammal("Leo", "Lion", 8, "Meat", "roaring", False, "Golden Mane")

@pytest.fixture
def cobra():
    return Reptile("SLYTHERIN", "Cobra", 5, "Rodents", "Parsel Tongue", True, 30, 8)

@pytest.fixture
def ibis():
    return Bird("Gary", "Ibis", 5, "Maccas Fries", "Screech", 1.25, True, "Northward")

# -------------------- Tests --------------------

def test_mammal_actions(lion):
    """Test mammal sound, eating, sleeping, and grooming behaviours."""
    assert "roaring" in lion.make_sound()
    assert lion.eat() == "Leo devours its meat."
    assert "rests" in lion.sleeping()
    assert "grooms" in lion.groom()

def test_reptile_actions(cobra):
    """Test reptile sound, eating, basking, shedding, and biting behaviours."""
    assert "Parsel Tongue" in cobra.make_sound()
    assert "injects venom" in cobra.eat()
    assert "rocks" in cobra.sleeping()
    assert "basks" in cobra.bask()
    assert "sheds" in cobra.shed_skin()

def test_bird_actions(ibis):
    """Test bird sound, eating, sleeping, flying, and migrating behaviours."""
    assert "Screech" in ibis.make_sound()
    assert ibis.eat() == "Gary pecks at its maccas fries."
    assert "perches" in ibis.sleeping()
    assert "takes off" in ibis.fly()
    assert "migrates" in ibis.migrate()
