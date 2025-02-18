from typing import List

class Garden:
    # Define the mapping between plants and their names.
    PLANT_NAMES = {
        'V': 'Violets',
        'R': 'Radishes',
        'C': 'Clover',
        'G': 'Grass',
        'T': 'Tulips'
    }

    def __init__(self, diagram, students: List[str]=None):
        self.diagram = diagram.strip().split('\n')
        if len(self.diagram) != 4:
            raise ValueError('Diagram must have exactly four rows.')
        if len(self.diagram[0]) % 2 == 1:
            raise ValueError('Each row of the diagram must have an even number of characters.')

        if students is None:
            # Use the default list of students.
            self.students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Ginny', 'Harriet', 'Ileana', 'John', 'Kincaid', 'Larry']
        else:
            # Check that there are enough students for each plot.
            num_plots = (len(self.diagram[0]) // 2) * len(self.diagram)
            if len(students) < num_plots:
                raise ValueError('Not enough students for all plots.')
            self.students = sorted(students[:num_plots])

        self._build_plot_map()


    def _build_plot_map(self):
        """Build a dictionary mapping student name to plant type."""
        self.plant_map = {}
        for i, row in enumerate(self.diagram):
            for j in range(0, len(row), 2):
                student = self.students[(i*6 + j//2) % len(self.students)]
                plant = self.PLANT_NAMES[row[j]]
                self.plant_map[student] = plant

    def plants(self, student_name):
        return self.plant_map[student_name]
