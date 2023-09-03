class Scale:
    def __init__(self, tonic):
        self.tonic = tonic.upper()

    def chromatic(self):
        chromatic_notes = ["A", "B♭", "B", "C", "D♭", "D", "E♭", "E", "F", "G♭", "G", "A♭"]
        return [note for note in chromatic_notes if self._shift_chromatic_scale().index(note) >= chromatic_notes.index(self.tonic)]

    def interval(self, intervals):
        diatonic_scale = []
        index = 0
        for i in intervals:
            if i == 'M':
                index += 2
            elif i == 'm':
                index += 1
            else:
                raise ValueError("Invalid interval")
            diatonic_scale.append(self._shift_chromatic_scale()[index % 12])
        return diatonic_scale

    def _shift_chromatic_scale(self):
        all_notes = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
        tonic_index = all_notes.index(self.tonic)
        return all_notes[tonic_index:] + all_notes[:tonic_index]
