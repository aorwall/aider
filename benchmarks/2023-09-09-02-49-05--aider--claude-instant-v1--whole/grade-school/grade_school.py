class School:
    def __init__(self):
        self.roster = {}

    def add_student(self, name, grade):
        if grade not in self.roster:
            self.roster[grade] = []
        if name not in self.roster[grade]:
            self.roster[grade].append(name)
        else:
            print(f"{name} is already enrolled in grade {grade}.")

    def print_roster(self):
        for grade in sorted(self.roster):
            for student in sorted(self.roster[grade]):
                print(f"{student} is in grade {grade}")

    def print_grade(self, grade_number):
        if grade_number in self.roster:
            print(sorted(self.roster[grade_number]))
        else:
            print()

    def print_roster_dict(self):
        print(self.roster)
