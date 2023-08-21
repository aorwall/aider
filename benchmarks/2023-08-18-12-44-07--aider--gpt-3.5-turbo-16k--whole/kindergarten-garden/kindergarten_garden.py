def plants(self, student):
    student_index = self.students.index(student)
    plant_positions = [student_index * 2, student_index * 2 + 1]
    plants = []
    for row in self.diagram.split("\n"):
        for position in plant_positions:
            plants.append(self.plants_mapping[row[position]])
    return plants
