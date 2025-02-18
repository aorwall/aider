class Scale:
    def __init__(self, tonic):
        self.tonic = tonic.capitalize()
        self.chromatic_scale = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
        self.sharp_notes = {'C': 'C', 'D':'D', 'E':'E', 'F':'F', 'G':'G', 'A':'A', 'B':'B'}
        self.flat_notes = {'C':'C', 'D':'D', 'E':'E', 'F':'F', 'G':'G', 'A':'A', 'B':'B'}

    def chromatic(self):
        index = self.chromatic_scale.index(self.tonic)
        return self.chromatic_scale[index:] + self.chromatic_scale[:index]

    def interval(self, intervals):
        scale = [self.tonic]
        current_note = self.tonic
        for i in intervals:
            if i == 'M':
                current_note = self.next_note(current_note, 2)
            elif i == 'm':
                current_note = self.next_note(current_note, 1)
            else: # Augmented Second
                current_note = self.next_note(current_note, 3)
            scale.append(current_note)
        return scale

    def next_note(self, note, steps):
        index = (self.chromatic_scale.index(note) + steps) % len(self.chromatic_scale)
        return self.chromatic_scale[index]
