class Scale:
    def __init__(self, tonic):
        self.tonic = tonic.upper()

    def chromatic(self):
        notes = "C,C#,D,D#,E,F,F#,G,G#,A,A#,B"
        if self.tonic in "CFGA":
            notes = notes.replace("#","b")
        return notes[notes.find(self.tonic):]

    def interval(self, intervals):
        notes = ""
        current_note = self.tonic
        for interval in intervals:
            if interval == "M":
                current_note = self.next_note(current_note, 2)
            elif interval == "m":
                current_note = self.next_note(current_note, 1)
            notes += current_note + ","
        return notes[:-1]

    def next_note(self, start, steps):
        notes = "C,C#,D,D#,E,F,F#,G,G#,A,A#,B"
        if start in "CFGA":
            notes = notes.replace("#","b")
        position = notes.find(start) + steps
        return notes[position%12]
