class Garden:
    def __init__(self, diagram, students=None):
        self.diagram = diagram.split('\n')
        self.students = sorted(students) if students else [
            'Alice', 'Bob', 'Charlie', 'David',
            'Eve', 'Fred', 'Ginny', 'Harriet',
            'Ileana', 'Joseph', 'Kincaid', 'Larry'
        ]
        self.plants_dict = {'G': 'Grass', 'C': 'Clover', 'R': 'Radishes', 'V': 'Violets'}

    def plants(self, student):
        index = self.students.index(student) * 2
        plants_code = [row[index:index+2] for row in self.diagram]
        return [self.plants_dict[code] for code in ''.join(plants_code)]