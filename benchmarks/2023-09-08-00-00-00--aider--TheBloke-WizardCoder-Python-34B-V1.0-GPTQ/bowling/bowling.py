class BowlingGame:
    def __init__(self):
        self.frames = []
        self.bonus_attempts = []

    def roll(self, pins):
        if len(self.frames) == 9:
            self.bonus_attempts.append(pins)
        else:
            self.frames.append(pins)

    def score(self):
        total_score = 0
        frame_index = 0

        for frame in range(10):
            if frame == 9:
                total_score += self._calculate_tenth_frame_score()
            elif self._is_strike(frame_index):
                total_score += self._calculate_strike_score(frame_index)
                frame_index += 1
            elif self._is_spare(frame_index):
                total_score += self._calculate_spare_score(frame_index)
                frame_index += 2
            else:
                total_score += self._calculate_open_frame_score(frame_index)
                frame_index += 2

        return total_score

    def _calculate_tenth_frame_score(self):
        if len(self.bonus_attempts) == 0:
            raise IndexError("cannot calculate tenth frame score without bonus attempts")

        total_score = sum(self.bonus_attempts)

        if self._is_strike(8):
            total_score += self.frames[8]
        elif self._is_spare(8):
            total_score += self.frames[8]

        return total_score

    def _calculate_strike_score(self, frame_index):
        if frame_index + 1 >= len(self.frames):
            raise IndexError("cannot calculate strike score without the next two throws")

        strike_bonus = self.frames[frame_index + 1] + self.frames[frame_index + 2]
        return 10 + strike_bonus

    def _calculate_spare_score(self, frame_index):
        if frame_index + 1 >= len(self.frames):
            raise IndexError("cannot calculate spare score without the next throw")

        spare_bonus = self.frames[frame_index + 1]
        return 10 + spare_bonus

    def _calculate_open_frame_score(self, frame_index):
        if frame_index + 1 >= len(self.frames):
            raise IndexError("cannot calculate open frame score without the next throw")

        return self.frames[frame_index] + self.frames[frame_index + 1]

    def _is_strike(self, frame_index):
        return frame_index < len(self.frames) and self.frames[frame_index] == 10

    def _is_spare(self, frame_index):
        return frame_index < len(self.frames) - 1 and self.frames[frame_index] + self.frames[frame_index + 1] == 10
