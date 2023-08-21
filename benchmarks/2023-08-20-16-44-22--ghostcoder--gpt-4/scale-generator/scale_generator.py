class Scale:
    CHROMATIC_SHARP = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    CHROMATIC_FLAT = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
    SHARP_KEYS = ['G', 'D', 'A', 'E', 'B', 'F#', 'a', 'e', 'b', 'f#', 'c#', 'g#', 'd#']
    FLAT_KEYS = ['F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'd', 'g', 'c', 'f', 'bb', 'eb']
    INTERVALS = {'m': 1, 'M': 2, 'A': 3}

    def __init__(self, tonic):
        self.tonic = tonic.capitalize()
        if self.tonic in self.SHARP_KEYS:
            self.chromatic_scale = self.CHROMATIC_SHARP
        elif self.tonic in self.FLAT_KEYS:
            self.chromatic_scale = self.CHROMATIC_FLAT
        else:
            self.chromatic_scale = self.CHROMATIC_SHARP if self.tonic.isupper() else self.CHROMATIC_FLAT
        self.tonic_index = self.chromatic_scale.index(self.tonic)

    def chromatic(self):
        return self.chromatic_scale[self.tonic_index:] + self.chromatic_scale[:self.tonic_index]

    def interval(self, intervals):
        scale = [self.tonic]
        index = self.tonic_index
        for interval in intervals:  # Include the last interval as it leads back to the tonic
            index = (index + self.INTERVALS[interval]) % len(self.chromatic_scale)
            scale.append(self.chromatic_scale[index])
        return scale