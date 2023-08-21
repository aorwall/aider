class Scale:
    def __init__(self, tonic):
        self.tonic = tonic.upper()

    def chromatic(self):
        chromatic_scale = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        if self.tonic.endswith('B') or self.tonic.endswith('E'):
            chromatic_scale = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
        tonic_index = chromatic_scale.index(self.tonic)
        return chromatic_scale[tonic_index:] + chromatic_scale[:tonic_index]

    def interval(self, intervals):
        chromatic_scale = self.chromatic()
        scale = [self.tonic]
        for interval in intervals:
            if interval == 'M':
                scale.append(chromatic_scale[(chromatic_scale.index(scale[-1].upper()) + 2) % 12])
            elif interval == 'm':
                scale.append(chromatic_scale[(chromatic_scale.index(scale[-1].upper()) + 1) % 12])
        return scale