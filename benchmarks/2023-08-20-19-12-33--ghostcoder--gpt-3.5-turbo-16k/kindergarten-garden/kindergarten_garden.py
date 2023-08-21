class Garden:
    def __init__(self, diagram, students=None):
        if students is None:
            self.students = [
                "Alice", "Bob", "Charlie", "David",
                "Eve", "Fred", "Ginny", "Harriet",
                "Ileana", "Joseph", "Kincaid", "Larry"
            ]
        else:
            self.students = sorted(students)
        self.diagram = diagram.split("\n")

    def plants(self, student):
        plant_dict = {
            "G": "Grass",
            "C": "Clover",
            "R": "Radishes",
            "V": "Violets"
        }
        student_index = self.students.index(student)
        plants = []
        for row in self.diagram:
            plants.extend([plant_dict[row[student_index * 2]], plant_dict[row[student_index * 2 + 1]]])
        return plants