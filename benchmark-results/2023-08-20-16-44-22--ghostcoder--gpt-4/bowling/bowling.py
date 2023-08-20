class BowlingGame:
    def __init__(self):
        self.rolls = []
        self.current_frame = 1
        self.is_first_roll = True
        self.frame_score = 0

    def roll(self, pins):
        if pins < 0 or pins > 10:
            raise ValueError("Pins must be between 0 and 10")
        if self.current_frame > 10:
            raise IndexError("Cannot roll after tenth frame")
        if not self.is_first_roll and self.frame_score + pins > 10:
            if self.current_frame == 10 and (self.frame_score == 10 or self.frame_score + pins == 10):
                pass  # allow bonus roll in tenth frame
            else:
                raise ValueError("Frame score cannot be more than 10 unless it's the tenth frame")
        self.rolls.append(pins)
        self.frame_score += pins
        if self.current_frame < 10 and (pins == 10 or not self.is_first_roll):
            self.current_frame += 1
            self.is_first_roll = True
            self.frame_score = 0
        else:
            self.is_first_roll = not self.is_first_roll
            if self.is_first_roll:
                self.current_frame += 1
                self.frame_score = 0

    def score(self):
        if self.current_frame < 10 or (self.current_frame == 10 and self.is_first_roll):
            raise IndexError("Score cannot be calculated before end of game")
        score = 0
        roll_index = 0
        for frame in range(10):
            if self.rolls[roll_index] == 10:  # strike
                score += 10 + self.rolls[roll_index + 1] + self.rolls[roll_index + 2]
                roll_index += 1
            elif self.rolls[roll_index] + self.rolls[roll_index + 1] == 10:  # spare
                score += 10 + self.rolls[roll_index + 2]
                roll_index += 2
            else:  # open frame
                score += self.rolls[roll_index] + self.rolls[roll_index + 1]
                roll_index += 2
        return score