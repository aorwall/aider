class Scale:
    def __init__(self, tonic):
        self.tonic = tonic
        self.chromatic_scale = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        self.sharp_signatures = {
            'C': [0],
            'G': [1, 3, 6, 8],
            'D': [1, 3, 5, 6, 8, 10],
            'A': [1, 3, 4, 6, 8, 10],
            'E': [1, 3, 4, 6, 8, 9, 11],
            'B': [1, 3, 4, 6, 8, 10],
            'F#': [1, 3, 4, 6, 7, 8, 10],
            'C#': [1, 2, 4, 5, 7, 9, 11],
        }
        self.flat_signatures = {
            'c': [0],
            'f': [1, 3, 4, 6, 8, 10],
            'bb': [1, 3, 4, 6, 8, 10, 11],
            'eb': [1, 3, 4, 6, 7, 8, 10],
            'ab': [1, 3, 5, 6, 8, 10],
            'db': [1, 3, 5, 6, 7, 9, 10],
            'gb': [1, 3, 5, 6, 8, 10],
            'cb': [1, 4, 6, 7, 9, 11],
        }

    def chromatic(self):
        index = self.chromatic_scale.index(self.tonic.upper())
        return self.chromatic_scale[index:] + self.chromatic_scale[:index]

    def interval(self, intervals):
        result = []
        current_note = self.tonic
        for interval in intervals:
            if interval == 'M':
                current_note = self._get_next_note(current_note, 2)
            elif interval == 'm':
                current_note = self._get_next_note(current_note, 1)
            else:
                raise ValueError('Invalid interval')
            result.append(current_note)
        return result

    def _get_next_note(self, note, skip):
        index = self.chromatic_scale.index(note)
        while True:
            index += 1
            if index >= len(self.chromatic_scale):
                index -= len(self.chromatic_scale)
            if self.chromatic_scale[index] != '#' and self.chromatic_scale[index] != 'b':
                break
        return self.chromatic_scale[index]

def main():
    print("Chromatic scale")
    print(Scale('c').chromatic())
    print()
    print("Intervals")
    print(Scale('d').interval(['M', 'M', 'm', 'M', 'M', 'M']))
    print(Scale('c').interval(['M', 'M', 'm', 'M', 'M', 'M']))
    print(Scale('g').interval(['M', 'M', 'm', 'M', 'M', 'M']))
    print(Scale('a').interval(['M', 'M', 'm', 'M', 'M', 'M']))
    print(Scale('e').interval(['M', 'M', 'm', 'M', 'M', 'M']))
    print(Scale('b').interval(['M', 'M', 'm', 'M', 'M', 'M']))
    print(Scale('f#').interval(['M', 'M', 'm', 'M', 'M', 'M']))
    print(Scale('c#').interval(['M', 'M', 'm', 'M', 'M', 'M']))

if __name__ == '__main__':
    main()
