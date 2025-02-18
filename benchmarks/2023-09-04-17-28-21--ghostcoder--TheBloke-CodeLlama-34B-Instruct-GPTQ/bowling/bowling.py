class BowlingGame:
    def __init__(self):
        self.rolls = []
        self.current_roll = 0

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        score = 0
        for frame in range(0, 10):
            if self._is_strike(frame):
                score += self._calculate_strike_score(frame)
            elif self._is_spare(frame):
                score += self._calculate_spare_score(frame)
            else:
                score += self._calculate_regular_score(frame)
        return score

    def _is_strike(self, frame_index):
        return self.rolls[frame_index] == 10

    def _is_spare(self, frame_index):
        return self.rolls[frame_index] + self.rolls[frame_index + 1] == 10

    def _calculate_strike_score(self, frame_index):
        return 10 + self.rolls[frame_index + 1] + self.rolls[frame_index + 2]

    def _calculate_spare_score(self, frame_index):
        return 10 + self.rolls[frame_index + 2]

    def _calculate_regular_score(self, frame_index):
        return self.rolls[frame_index] + self.rolls[frame_index + 1]
