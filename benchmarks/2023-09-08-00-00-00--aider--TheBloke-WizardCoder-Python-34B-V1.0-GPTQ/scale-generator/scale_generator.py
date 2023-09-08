class Scale:
    def __init__(self, tonic):
        self.tonic = tonic.upper()

    def chromatic(self):
        chromatic_scale = [
            "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"
        ]
        return chromatic_scale

    def interval(self, intervals):
        diatonic_scale = []
        diatonic_scale.append(self.tonic)
        for interval in intervals:
            if interval == "M":
                next_note = diatonic_scale[-1]
                if next_note == "G#" or next_note == "A#":
                    next_note = chr(ord(next_note) + 1)
                elif next_note == "B" or next_note == "E":
                    next_note = chr(ord(next_note) - 1)
                elif next_note == "A":
                    next_note = "B"
                elif next_note == "D":
                    next_note = "E"
                elif next_note == "G":
                    next_note = "A"
                elif next_note == "C":
                    next_note = "D"
                elif next_note == "F":
                    next_note = "G"
                diatonic_scale.append(next_note)
            elif interval == "m":
                next_note = diatonic_scale[-1]
                if next_note == "A":
                    next_note = "Bb"
                elif next_note == "D":
                    next_note = "Eb"
                elif next_note == "G":
                    next_note = "Ab"
                elif next_note == "C":
                    next_note = "Db"
                elif next_note == "F":
                    next_note = "Gb"
                elif next_note == "Bb":
                    next_note = "Cb"
                elif next_note == "Eb":
                    next_note = "Fb"
                diatonic_scale.append(next_note)
        return diatonic_scale
