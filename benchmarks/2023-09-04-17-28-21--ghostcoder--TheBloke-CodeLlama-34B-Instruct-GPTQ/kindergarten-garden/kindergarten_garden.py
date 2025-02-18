class Garden:
    def __init__(self, diagram, students=None):
        self.diagram = diagram
        self.students = [
            "Alice",
            "Bob",
            "Charlie",
            "David",
            "Eve",
            "Fred",
            "Ginny",
            "Harriet",
            "Ileana",
            "Joseph",
            "Kincaid",
            "Larry",
        ][::-1]
        if students is not None:
            self.students = students

    def plants(self, student):
        index = self.students.index(student) * 2
        first_row = [x for x in self.diagram.split("\n")[0]]
        second_row = [x for x in self.diagram.split("\n")[1]]
        return (
            list(
                map(
                    lambda x: x[0],
                    filter(lambda y: y[1] % 2 == 0, enumerate(first_row)),
                )
            )
            + list(
                map(
                    lambda x: x[0],
                    filter(lambda y: y[1] % 2 != 0, enumerate(second_row))[
                        index:
                    ],
                )
            )
        )
