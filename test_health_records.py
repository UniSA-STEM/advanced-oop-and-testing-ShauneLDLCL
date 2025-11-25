"""
File: test_health_records.py
Description: Tests the functionality of the HealthIssues and HealthRecords
classes, including adding issues, retrieving histories, detecting severe cases,
and listing animals with medical records. Ensures correct linking of health data
to animals and validation logic within health record operations.
Author: Shaune Legayada
ID: 110444251
Username: legsd001
This is my own work as defined by the University's Academic Integrity Policy.
"""

import pytest
from health_issues import HealthIssues
from health_records import HealthRecords
from mammal import Mammal

# -------------------- Fixtures --------------------

@pytest.fixture
def lion():
    return Mammal("Leo", "Lion", 8, "Meat", "roaring", False, "Golden Mane")

@pytest.fixture
def records():
    return HealthRecords()

# -------------------- Tests --------------------

def test_add_issue(records, lion):
    """Ensure issues are successfully stored."""
    issue = HealthIssues("Injury", "2025-01-01", "High", "Rest")
    records.add_issue(lion, issue)
    assert len(records.get_issues(lion)) == 1

def test_severity_level(records, lion):
    """Ensure severity check detects high or critical issues."""
    issue = HealthIssues("Infection", "2025-01-05", "Critical", "Medication")
    records.add_issue(lion, issue)
    assert records.severity_level(lion) is True

def test_get_animals_with_issues(records, lion):
    """Ensure animals with recorded issues appear in list."""
    issue = HealthIssues("Cut", "2025-02-01", "Low", "Bandage")
    records.add_issue(lion, issue)
    all_animals = records.get_animals_with_issues()
    assert lion in all_animals
