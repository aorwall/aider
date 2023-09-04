from typing import List

def parse_initial_diagram(diagram: str) -> List[List[str]]:
    parsed_diagram = [list(row) for row in diagram.strip().split('\n')]

    for row in parsed_diagram:
        assert all(len(cell) == 2 for cell in row), f"Invalid input: {parsed_diagram}"

    return parsed_diagram

class Garden:
    def __init__(self, diagram: str, students: List[str] = None):
        self.diagram = parse_initial_diagram(diagram)
        self.students = sorted(['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']) \
            if students is None else sorted(students)

        self.plant_names = {'C': 'Clover', 'G': 'Grass', 'R': 'Radish', 'T': 'Tulip', 'V': 'Violet'}

    def plants(self, student_name: str) -> List[str]:
        index = self.students.index(student_name)
        plants = []
        for row in self.diagram:
            for col in range(index, len(row), len(self.students)):
                plant_code = row[col][0].upper()
                plants.append(self.plant_names[plant_code])

        return plants
