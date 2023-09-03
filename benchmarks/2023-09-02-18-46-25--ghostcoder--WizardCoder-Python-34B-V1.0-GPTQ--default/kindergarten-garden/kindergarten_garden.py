class Garden:
    def __init__(self, diagram, students=None):
        if students is None:
            self.students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]
        else:
            self.students = sorted(students)

        self.diagram = diagram.split("\n")

    def plants(self, student_name):
        # Split the string into rows
        row1 = list(self.diagram[0])
        row2 = list(self.diagram[1])

        # Get the index of the student name in the roster
        index = self.students.index(student_name) * 4

        # Slice the appropriate section for each row based on the index
        plants1 = row1[index:index+4]
        plants2 = row2[index:index+4]

        # Replace letters with plant names
        for i in range(len(plants1)):
            if plants1[i] == 'V':
                plants1[i] = 'Violets'
            elif plants1[i] == 'R':
                plants1[i] = 'Radishes'
            elif plants1[i] == 'C':
                plants1[i] = 'Clover'
            elif plants1[i] == 'G':
                plants1[i] = 'Grass'

        for j in range(len(plants2):
            if plants2[j] == 'V':
                plants2[j] = 'Violets'
            elif plants2[j] == 'R':
                plants2[j] = 'Radishes'
            elif plants2[j] == 'C':
                plants2[j] = 'Clover'
            elif plants2[j] == 'G':
                plants2[j] = 'Grass'

        return [plants1, plants2]
