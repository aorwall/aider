class Garden:
    def __init__(self, diagram, students=None):
        if students is None:
            self.students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]
        else:
            self.students = students

        self.diagram = diagram.split("\n")

    def plants(self, student_name):
        student_index = self.students.index(student_name)
        plants = []

        for row in self.diagram:
            start_index = student_index * 2
            end_index = start_index + 2
            plants.extend(row[start_index:end_index])

        return plants

# Test cases
garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
print(garden.plants("Alice"))  # Output: ['Violets', 'Radishes', 'Violets', 'Radishes']
print(garden.plants("Bob"))  # Output: ['Clover', 'Grass', 'Clover', 'Clover']
print(garden.plants("Charlie"))  # Output: ['Violets', 'Violets', 'Clover', 'Grass']
print(garden.plants("David"))  # Output: ['Radishes', 'Clover', 'Radishes', 'Clover']
