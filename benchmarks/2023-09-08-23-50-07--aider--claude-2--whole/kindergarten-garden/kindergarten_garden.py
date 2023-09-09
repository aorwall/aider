class Garden:
    DEFAULT_STUDENTS = ["Alice", "Bob", "Charlie", "David", 
                       "Eve", "Fred", "Ginny", "Harriet",
                       "Ileana", "Joseph", "Kincaid", "Larry"]

    PLANT_KEY = {
        'V': 'Violets',
        'R': 'Radishes',
        'C': 'Clover',
        'G': 'Grass'
    }
    
    def __init__(self, diagram, students=DEFAULT_STUDENTS):
        self.diagram = diagram.splitlines()
        self.students = sorted(students)

    def plants(self, student):
        index = self.students.index(student) * 2
        plants = []
        for row in self.diagram:
            plant_codes = row[index:index+2]
            plant_names = [self.PLANT_KEY[code] for code in plant_codes]
            plants.extend(plant_names)
        return plants
