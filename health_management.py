class HealthIssues:
    def __init__(self, description, date_reported, severity, treatment_plan):
        self.__description = description
        self.__date_reported = date_reported
        self.__severity = severity
        self.__treatment_plan = treatment_plan

    def get_description(self):
        return self.__description

    def get_date_reported(self):
        return self.__date_reported

    def get_severity(self):
        return self.__severity

    def get_treatment_plan(self):
        return self.__treatment_plan

    description = property(get_description)
    date_reported = property(get_date_reported)
    severity = property(get_severity)
    treatment_plan = property(get_treatment_plan)

    def __str__(self):
        return (f"Description: {self.__description}\n"
                f"Date: {self.__date_reported}\n"
                f"Severity: {self.__severity}\n"
                f"Treatment: {self.__treatment_plan}")


