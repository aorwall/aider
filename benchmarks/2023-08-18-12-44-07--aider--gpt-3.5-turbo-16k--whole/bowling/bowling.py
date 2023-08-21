class BowlingGame:
    def __init__(self):
        self.rolls = []
        self.scores = []

    def roll(self, pins):
        if pins < 0 or pins > 10:
            raise ValueError("Invalid number of pins")

        if len(self.rolls) == 20 and not self.is_strike(18) and not self.is_spare(18):
            raise ValueError("Cannot roll if game already has ten frames")

        if len(self.rolls) == 21 and not self.is_strike(18):
            raise ValueError("Cannot roll after bonus rolls for strike")

        if len(self.rolls) == 22:
            raise ValueError("Cannot roll after bonus roll for spare")

        if len(self.rolls) == 20 and (self.is_strike(18) or self.is_spare(18)):
            self.rolls.append(pins)
        elif len(self.rolls) == 21 and self.is_strike(18):
            self.rolls.append(pins)
        elif len(self.rolls) == 21 and self.is_spare(18):
            if self.rolls[19] + pins > 10:
                raise ValueError("Bonus roll after a spare cannot score more than 10 points")
            self.rolls.append(pins)
        else:
            self.rolls.append(pins)

    def score(self):
        total_score = 0
        roll_index = 0

        for frame in range(10):
            if self.is_strike(roll_index):
                total_score += 10 + self.strike_bonus(roll_index)
                roll_index += 1
            elif self.is_spare(roll_index):
                total_score += 10 + self.spare_bonus(roll_index)
                roll_index += 2
            else:
                total_score += self.frame_score(roll_index)
                roll_index += 2

        return total_score

    def is_strike(self, roll_index):
        return self.rolls[roll_index] == 10

    def is_spare(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1] == 10

    def strike_bonus(self, roll_index):
        return self.rolls[roll_index + 1] + self.rolls[roll_index + 2]

    def spare_bonus(self, roll_index):
        return self.rolls[roll_index + 2]

    def frame_score(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1]
