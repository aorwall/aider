class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        if pins < 0 or pins > 10:
            raise ValueError("Pins must be between 0 and 10")
        self.rolls.append(pins)

    def score(self):
        score = 0
        frame_index = 0
        for frame in range(10):
            if frame < 9:
                if self.rolls[frame_index] == 10:  # strike
                    score += 10 + self.rolls[frame_index + 1] + self.rolls[frame_index + 2]
                    frame_index += 1
                elif self.rolls[frame_index] + self.rolls[frame_index + 1] == 10:  # spare
                    score += 10 + self.rolls[frame_index + 2]
                    frame_index += 2
                else:  # open frame
                    score += self.rolls[frame_index] + self.rolls[frame_index + 1]
                    frame_index += 2
            else:  # tenth frame
                if self.rolls[frame_index] == 10:  # strike
                    score += 10 + self.rolls[frame_index + 1] + self.rolls[frame_index + 2]
                    frame_index += 3
                elif self.rolls[frame_index] + self.rolls[frame_index + 1] == 10:  # spare
                    score += 10 + self.rolls[frame_index + 2]
                    frame_index += 3
                else:  # open frame
                    score += self.rolls[frame_index] + self.rolls[frame_index + 1]
                    frame_index += 2
        if frame_index != len(self.rolls):
            raise IndexError("Invalid number of rolls")
        return score
