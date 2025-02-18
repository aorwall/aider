class Garden:
    def __init__(self, diagram="", students=None):
        self._students = ["Alice", "Bob", "Charlie", "David",
                          "Eve", "Fred", "Ginny", "Harriet",
                          "Ileana", "Joseph", "Kincaid", "Larry"] \
            if students is None else students

        # Processing the garden diagram
        self._diagram = [[], []]
        rows = diagram.split('\n')
        for i, row in enumerate(rows):
            for j, c in enumerate(row):
                if c != 'V': continue
                self._diagram[i].append((j % 2) * 2 + (j // len(rows[0])) - 1)

    def plants(self, student):
        idx = self._students.index(student)
        return ['radishes', 'grass', 'clover'][(idx%4//2)+(idx<8)*2]
