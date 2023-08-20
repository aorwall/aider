class Scale:
    def __init__(self, tonic):
        self.tonic = tonic

    def chromatic(self):
        chromatic_scale = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        tonic_index = chromatic_scale.index(self.tonic.upper())
        return chromatic_scale[tonic_index:] + chromatic_scale[:tonic_index]

    def interval(self, intervals):
        chromatic_scale = self.chromatic()
        scale = [self.tonic.upper()]
        for interval in intervals:
            if interval == 'M':
                if len(chromatic_scale) < 3:
                    break
                scale.append(chromatic_scale[2])
                chromatic_scale = chromatic_scale[2:]
            elif interval == 'm':
                if len(chromatic_scale) < 2:
                    break
                scale.append(chromatic_scale[1])
                chromatic_scale = chromatic_scale[1:]
        return scale
