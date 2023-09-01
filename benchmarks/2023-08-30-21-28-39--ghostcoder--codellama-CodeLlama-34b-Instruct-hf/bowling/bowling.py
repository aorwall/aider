class BowlingGame:
    def __init__(self):
        self.frames = []
        self.bonus_rolls = 0
        self.bonus_rolls_scores = []

    def roll(self, pins):
        if len(self.frames) == 10:
            raise ValueError("cannot roll after game is over")

        if pins < 0 or pins > 10:
            raise ValueError("invalid number of pins")

        if len(self.frames) == 9 and pins == 10:
            raise ValueError("cannot throw bonus with an open tenth frame")

        self.frames.append(pins)

        if len(self.frames) == 10:
            self.bonus_rolls = 0
            self.bonus_rolls_scores = []

        if len(self.frames) == 10 and pins == 10:
            self.bonus_rolls += 1
            self.bonus_rolls_scores.append(pins)

        if len(self.frames) == 10 and self.bonus_rolls == 2:
            self.bonus_rolls_scores.append(pins)

        if len(self.frames) == 10 and self.bonus_rolls == 1:
            self.bonus_rolls_scores.append(pins)

    def score(self):
        if len(self.frames) != 10:
            raise ValueError("game is not over")

        score = 0
        for i in range(10):
            if self.frames[i] == 10:
                score += 10 + self.frames[i + 1] + self.frames[i + 2]
            else:
                score += self.frames[i]

        if self.bonus_rolls == 1:
            score += self.bonus_rolls_scores[0]
        elif self.bonus_rolls == 2:
            score += self.bonus_rolls_scores[0] + self.bonus_rolls_scores[1]

        return score
