"""
File: health_records.py
Description: Manages medical histories for all animals inside the Zoo Management
System. The HealthRecords class stores all HealthIssues for each animal, supports
severity checks, retrieves health histories, and generates formatted medical
reports. This class centralises all health-related data and ensures safe
validation and processing for veterinarian interactions.
Author: Shaune Legayada
ID: 110444251
Username: legsd001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from health_issues import HealthIssues
from animal import Animal

class HealthRecords:
    """
    Represents the full collection of health issues for animals in the zoo.

    Attributes:
        __records (dict): Maps Animal → list[HealthIssues].
        __empty_list (list): Returned when no issues exist for an animal.
    """

    def __init__(self):
        """Initialise an empty health record system."""
        self.__records = {}
        self.__empty_list = []

    # -------------------- Issue Management --------------------

    def add_issue(self, animal, issue):
        """
        Record a new health issue for a given animal.

        Validates:
        - Animal must be an Animal instance.
        - Issue must be a HealthIssues instance.
        """
        if not isinstance(animal, Animal):
            raise ValueError("Health issues must be attached to Animal objects.")
        if not isinstance(issue, HealthIssues):
            raise ValueError("Only HealthIssue objects can be recorded.")

        if animal not in self.__records:
            self.__records[animal] = []
        self.__records[animal].append(issue)

    def get_issues(self, animal):
        """
        Retrieve all issues for an animal.

        :returns:
        list[HealthIssues] — All issues recorded for that animal.
        """
        if animal in self.__records:
            return self.__records[animal]
        return self.__empty_list

    # -------------------- Severity Checks --------------------

    def severity_level(self, animal):
        """
        Determine if the animal has any High or Critical severity issues.

        :returns:
        bool — True if a severe issue exists, otherwise False.
        """
        issues = self.get_issues(animal)
        index = 0

        while index < len(issues):
            current_issue = issues[index]
            if current_issue.severity == "High" or current_issue.severity == "Critical":
                return True
            index += 1

        return False

    # -------------------- Retrieval Helpers --------------------

    def get_animals_with_issues(self):
        """
        Return a list of all animals with at least one recorded issue.

        :returns:
        list[Animal]
        """
        animals = []
        for animal in self.__records:
            animals.append(animal)
        return animals

    # -------------------- Report Generation --------------------

    def generate_report(self, animal):
        """
        Produce a formatted full medical report for a given animal.

        :returns:
        str — Multi-line formatted report including each issue.
        """
        issues = self.get_issues(animal)

        if len(issues) == 0:
            return f"No health issues recorded for {animal.get_name()}."

        report = f"Health Report for {animal.get_name()}:\n"
        index = 0

        while index < len(issues):
            issue = issues[index]
            issue_number = index + 1
            issue_summary = issue.summarise_issue()
            report = report + f"{issue_number}. {issue_summary}\n"
            index += 1

        return report
