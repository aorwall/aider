class Garden:
    def __init__(self, diagram, students=None):
        if students is None:
            self.students = ["Alice", "Bob", "Charlie", "David",
                              "Eve", "Fred", "Ginny", "Harriet",
                              "Ileana", "Joseph", "Kincaid", "Larry"]
        else:
            self.students = sorted(students)

        self.diagram = diagram.split("\n")

    def plants(self, student):
        index = self.students.index(student) % 2
        return [''.join([self.diagram[row][(col*2)+index] for col in range(2)]) for row in range(2)]
