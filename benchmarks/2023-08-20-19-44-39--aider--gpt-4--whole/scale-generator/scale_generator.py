class Scale:
    CHROMATIC_SCALE_SHARP = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    CHROMATIC_SCALE_FLAT = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
    SHARP_KEYS = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'a', 'e', 'b', 'f#', 'c#', 'g#', 'd#']
    FLAT_KEYS = ['F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'd', 'g', 'c', 'f', 'bb', 'eb']

    def __init__(self, tonic):
        self.tonic = tonic.capitalize()
        self.scale = self.CHROMATIC_SCALE_SHARP if self.tonic in self.SHARP_KEYS else self.CHROMATIC_SCALE_FLAT

    def chromatic(self):
        start = self.scale.index(self.tonic)
        return self.scale[start:] + self.scale[:start]

    def interval(self, intervals):
        scale = self.chromatic()
        result = [scale[0]]
        step_map = {'m': 1, 'M': 2, 'A': 3}
        for interval in intervals:
            result.append(scale[step_map[interval]])
            scale = scale[step_map[interval]:]
        return result
