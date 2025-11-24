"""
File: test_health_records.py
Description: Tests for HealthIssues and HealthRecords classes.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
"""

import pytest
from health_issues import HealthIssues
from health_records import HealthRecords
from mammal import Mammal


@pytest.fixture
def lion():
    return Mammal("Leo", "Lion", 8, "Meat", "roaring", False, "Golden Mane")


@pytest.fixture
def records():
    return HealthRecords()


def test_add_issue(records, lion):
    issue = HealthIssues("Injury", "2025-01-01", "High", "Rest")
    records.add_issue(lion, issue)
    assert len(records.get_issues(lion)) == 1


def test_severity_level(records, lion):
    issue = HealthIssues("Infection", "2025-01-05", "Critical", "Medication")
    records.add_issue(lion, issue)
    assert records.severity_level(lion) is True


def test_get_animals_with_issues(records, lion):
    issue = HealthIssues("Cut", "2025-02-01", "Low", "Bandage")
    records.add_issue(lion, issue)
    all_animals = records.get_animals_with_issues()
    assert lion in all_animals
