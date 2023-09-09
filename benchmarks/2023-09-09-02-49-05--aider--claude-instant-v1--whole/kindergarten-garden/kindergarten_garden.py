class Garden:
    def __init__(self, diagram, students=["Alice", "Bob", "Charlie", "David", 
                                            "Eve", "Fred", "Ginny", "Harriet", 
                                            "Ileana", "Joseph", "Kincaid", "Larry"]):
        self.diagram = diagram
        self.students = students
        self.plant_map = {"V": "Violets", "R": "Radishes", "C": "Clover", "G": "Grass"}
        
    def plants(self, name):
        student_index = self.students.index(name)
        plants = []
        for cup in self.diagram[student_index*4:student_index*4+4]:
            plants.append(self.plant_map[cup])
        return plants
