class BowlingGame:
    def __init__(self):
        self.rolls = []
        self.frames = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]

    def roll(self, pins):
        if len(self.rolls) >= 21:
            raise Exception('Cannot roll after game is over')

        self.rolls.append(pins)

    def score(self):
        total_score = 0
        roll_index = 0

        for frame in range(10):
            if roll_index == len(self.rolls):
                break

            if self.isStrike(frame):
                total_score += self.strikeBonus(frame)
                roll_index += 1
            elif self.isSpare(frame):
                total_score += self.spareBonus(frame)
                roll_index += 2
            else:
                total_score += sum(self.rolls[roll_index : roll_index + 2])
                roll_index += 2

        if self.isStrike(9):
            total_score += self.strikeBonus(9) + self.fillBalls()
        elif self.isSpare(9):
            total_score += self.spareBonus(9) + self.fillBalls()
        else:
            total_score += sum(self.rolls[-2:])

        return total_score

    def isStrike(self, frame):
        return self.rolls[self.frames[frame][0]] == 10

    def strikeBonus(self, frame):
        return 10 + self.rolls[self.frames[frame][0] + 1] + self.rolls[self.frames[frame][0] + 2]

    def isSpare(self, frame):
        return self.rolls[self.frames[frame][0]] + self.rolls[self.frames[frame][1]] == 10

    def spareBonus(self, frame):
        return 10 + self.rolls[self.frames[frame][1]]

    def fillBalls(self):
        if len(self.rolls) >= 21:
            raise Exception('Cannot have more than 21 rolls')

        return self.rolls[-2:]
