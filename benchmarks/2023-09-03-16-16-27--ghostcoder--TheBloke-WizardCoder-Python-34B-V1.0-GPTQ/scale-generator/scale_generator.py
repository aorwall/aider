from typing import List

class Scale:
    def __init__(self, tonic):
        self.tonic = tonic.upper()
        self._notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'] # all notes in order on the keyboard
        self._intervals = {'M': 2, '#': 1, 'm': -1} # mapping of interval names to their corresponding number of semitones

    def chromatic(self):
        """Returns the chromatic scale starting at the tonic"""
        index = self._notes.index(self.tonic)
        return [note for note in self._notes[index:] + self._notes[:index]]

    def interval(self, intervals: List[str]) -> List[str]:
        """Generates a new scale based on the given sequence of intervals"""
        result = []
        current = self._notes.index(self.tonic)
        result.append(self._notes[current])
        for i in intervals:
            if i not in self._intervals:
                raise ValueError("Invalid interval")
            current += self._intervals.get(i, 0)
            result.append(self._notes[current % len(self._notes))
        return result