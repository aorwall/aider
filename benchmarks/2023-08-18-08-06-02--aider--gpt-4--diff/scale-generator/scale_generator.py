class Scale:
    def __init__(self, tonic):
        self.tonic = tonic.upper()
        self.sharps = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        self.flats = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
        self.scale = self.sharps if self.tonic in ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'a', 'e', 'b', 'f#', 'c#', 'g#', 'd#'] else self.flats

    def chromatic(self):
        start = self.scale.index(self.tonic)
        return self.scale[start:] + self.scale[:start]

    def interval(self, intervals):
        scale = self.chromatic()
        result = [scale[0]]
        for interval in intervals:
            if interval == 'm':
                result.append(scale[1])
                scale = scale[2:]
            elif interval == 'M':
                result.append(scale[2])
                scale = scale[3:]
            elif interval == 'A':
                result.append(scale[3])
                scale = scale[4:]
        return result
