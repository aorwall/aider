CHROMATIC_SCALE = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

SHARP_KEYS = ["G", "D", "A", "E", "B", "F#", "C#", "G#", "D#", "A#", "F"]
FLAT_KEYS = ["F", "Bb", "Eb", "Ab", "Db", "Gb", "d", "g", "c", "f", "bb", "eb"]


class Scale:
    def __init__(self, tonic):
        self.tonic = tonic.upper()

    def chromatic(self):
        tonic_index = CHROMATIC_SCALE.index(self.tonic)
        return CHROMATIC_SCALE[tonic_index:] + CHROMATIC_SCALE[:tonic_index]

    def interval(self, intervals):
        scale = [self.tonic]
        note = self.tonic
        for interval in intervals:
            if interval == "m":
                if CHROMATIC_SCALE.index(note) + 1 < len(CHROMATIC_SCALE):
                    note = CHROMATIC_SCALE[CHROMATIC_SCALE.index(note) + 1]
                else:
                    note = CHROMATIC_SCALE[0]
            elif interval == "M":
                if CHROMATIC_SCALE.index(note) + 2 < len(CHROMATIC_SCALE):
                    note = CHROMATIC_SCALE[CHROMATIC_SCALE.index(note) + 2] 
                else:
                    note = CHROMATIC_SCALE[CHROMATIC_SCALE.index(note) + 2 - len(CHROMATIC_SCALE)]
            elif interval == "A":
                if CHROMATIC_SCALE.index(note) + 3 < len(CHROMATIC_SCALE):
                    note = CHROMATIC_SCALE[CHROMATIC_SCALE.index(note) + 3]
                else:
                    note = CHROMATIC_SCALE[CHROMATIC_SCALE.index(note) + 3 - len(CHROMATIC_SCALE)]
           