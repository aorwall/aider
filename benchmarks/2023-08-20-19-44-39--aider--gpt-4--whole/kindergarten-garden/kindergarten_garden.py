class Garden:
    def __init__(self, diagram, students=None):
        self.diagram = diagram.split('\n')
        self.students = sorted(students) if students else [
            'Alice', 'Bob', 'Charlie', 'David',
            'Eve', 'Fred', 'Ginny', 'Harriet',
            'Ileana', 'Joseph', 'Kincaid', 'Larry'
        ]
        self.plant_names = {'V': 'Violets', 'R': 'Radishes', 'C': 'Clover', 'G': 'Grass'}

    def plants(self, student):
        index = self.students.index(student) * 2
        plants = [self.diagram[0][index:index+2], self.diagram[1][index:index+2]]
        return [self.plant_names[p] for p in ''.join(plants)]
