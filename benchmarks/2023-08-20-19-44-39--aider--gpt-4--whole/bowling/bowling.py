class BowlingGame:
    def __init__(self):
        self.rolls = []
        self.current_roll = 0

    def roll(self, pins):
        if pins < 0 or pins > 10:
            raise ValueError("Pins must be between 0 and 10")
        if self.current_roll >= 20 and (self.is_spare(self.current_roll - 2) or self.is_strike(self.current_roll - 2)):
            if self.current_roll >= 21 and self.is_spare(self.current_roll - 2):
                raise IndexError("cannot throw bonus with an open tenth frame")
            if self.current_roll >= 22:
                raise IndexError("cannot throw bonus with an open tenth frame")
        elif self.current_roll >= 20:
            raise IndexError("cannot roll after game is over")
        if self.current_roll % 2 == 1 and self.rolls[self.current_roll - 1] + pins > 10:
            raise ValueError("two rolls in a frame cannot score more than 10 points")
        if self.current_roll == 19 and self.is_strike(self.current_roll - 1) and pins == 10:
            raise ValueError("the second bonus rolls after a strike in the last frame cannot be a strike if the first one is not a strike")
        if self.current_roll == 20 and self.is_strike(self.current_roll - 2) and self.rolls[self.current_roll - 1] + pins > 10:
            raise ValueError("two bonus rolls after a strike in the last frame cannot score more than 10 points")
        self.rolls.append(pins)
        self.current_roll += 1

    def score(self):
        if self.current_roll < 20 or (self.current_roll == 20 and not (self.is_spare(self.current_roll - 2) or self.is_strike(self.current_roll - 2))):
            raise IndexError("game is not yet over")
        score = 0
        frame_index = 0
        for frame in range(10):
            if self.is_strike(frame_index):  # strike
                score += 10 + self.strike_bonus(frame_index)
                frame_index += 1
            elif self.is_spare(frame_index):  # spare
                score += 10 + self.spare_bonus(frame_index)
                frame_index += 2
            else:  # open frame
                score += self.sum_of_balls_in_frame(frame_index)
                frame_index += 2
        return score

    def is_strike(self, frame_index):
        return self.rolls[frame_index] == 10

    def is_spare(self, frame_index):
        return self.rolls[frame_index] + self.rolls[frame_index + 1] == 10

    def strike_bonus(self, frame_index):
        return self.rolls[frame_index + 1] + self.rolls[frame_index + 2]

    def spare_bonus(self, frame_index):
        return self.rolls[frame_index + 2]

    def sum_of_balls_in_frame(self, frame_index):
        return self.rolls[frame_index] + self.rolls[frame_index + 1]
