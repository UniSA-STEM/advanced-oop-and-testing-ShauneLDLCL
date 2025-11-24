from health_issues import HealthIssues
from animal import Animal
class HealthRecords:
    def __init__(self):
        self.__records = {}
        self.__empty_list = []

    def add_issue(self, animal, issue):
        if not isinstance(animal, Animal):
            raise ValueError("Health issues must be attached to Animal objects.")
        if not isinstance(issue, HealthIssues):
            raise ValueError("Only HealthIssue objects can be recorded.")

        if animal not in self.__records:
            self.__records[animal] = []
        self.__records[animal].append(issue)

    def get_issues(self, animal):
        if animal in self.__records:
            return self.__records[animal]
        return self.__empty_list

    def severity_level(self, animal):
        issues = self.get_issues(animal)
        issues_counter = 0

        while issues_counter < len(issues):
            current_issue = issues[issues_counter]
            if current_issue.severity == "High" or current_issue.severity == "Critical":
                return True
            issues_counter += 1

        return False

    def get_animals_with_issues(self):

        animals = []
        for animal in self.__records:
            animals.append(animal)
        return animals

    def generate_report(self, animal):
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

