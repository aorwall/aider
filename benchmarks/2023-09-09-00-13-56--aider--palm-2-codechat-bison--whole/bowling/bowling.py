class BowlingGame:
    def __init__(self):
        self.frames = []

    def roll(self, pins):
        if len(self.frames) == 10:
            raise ValueError("cannot roll after the tenth frame")

        frame = self.frames[-1]
        if frame.is_complete():
            self.frames.append(Frame())
            frame = self.frames[-1]

        frame.add_roll(pins)

    def score(self):
        score = 0
        for frame in self.frames:
            score += frame.score()

        return score


class Frame:
    def __init__(self):
        self.rolls = []

    def add_roll(self, pins):
        if len(self.rolls) == 2:
            raise ValueError("cannot add more than two rolls to a frame")

        self.rolls.append(pins)

    def is_complete(self):
        return len(self.rolls) == 2

    def score(self):
        if self.is_complete():
            return sum(self.rolls)

        if self.rolls[0] == 10:
            return 10 + self.rolls[1]

        if sum(self.rolls) == 10:
            return 10 + self.rolls[0]

        return sum(self.rolls)
