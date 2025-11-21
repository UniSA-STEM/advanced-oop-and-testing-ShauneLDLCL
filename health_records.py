from health_issues import HealthIssues

class HealthRecords:
    def __init__(self):
        self.__records = {}
        self.__empty_list = []

    def add_issue(self, animal, issue):
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

