class Garden:
    def __init__(self, diagram, students=None):
        self.diagram = diagram.split('\n')
        self.students = sorted(students) if students else ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
        self.plant_names = {'V': 'Violets', 'R': 'Radishes', 'C': 'Clover', 'G': 'Grass'}

    def plants(self, student):
        index = self.students.index(student)
        plants_initials = [row[index*2:index*2+2] for row in self.diagram]
        return [self.plant_names[initial] for initials in plants_initials for initial in initials]
