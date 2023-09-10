import itertools


class Scale:
    """
    Represents a musical scale.

    Args:
        tonic (str): The tonic of the scale.
    """

    def __init__(self, tonic):
        self.tonic = tonic

    def chromatic(self):
        """
        Generates the 12 note chromatic scale starting with the tonic.

        Returns:
            list: A list of 12 notes.
        """
        notes = ["A", "A♯", "B", "C", "C♯", "D", "D♯", "E", "F", "F♯", "G", "G♯"]
        scale = [notes[notes.index(tonic)]]
        for i in range(1, 12):
            scale.append(notes[(notes.index(scale[-1]) + 1) % 12])
        return scale

    def interval(self, intervals):
        """
        Generates the musical scale starting with the tonic and following the specified interval pattern.

        Args:
            intervals (list): A list of intervals.

        Returns:
            list: A list of notes.
        """
        notes = self.chromatic()
        scale = [notes[notes.index(tonic)]]
        for interval in intervals:
            if interval == "M":
                scale.append(notes[(notes.index(scale[-1]) + 2) % 12])
            elif interval == "m":
                scale.append(notes[(notes.index(scale[-1]) + 1) % 12])
            else:
                raise ValueError("Invalid interval: {}".format(interval))
        return scale


if __name__ == "__main__":
    scale = Scale("C")
    print(scale.chromatic())
    print(scale.interval("MMmMMMm"))
