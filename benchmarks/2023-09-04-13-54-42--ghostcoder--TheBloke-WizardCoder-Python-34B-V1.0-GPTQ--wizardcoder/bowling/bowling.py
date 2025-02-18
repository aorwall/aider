import sys
from typing import List

class BowlingGame:
    def __init__(self):
        self.frames = []
        self.bonus_attempts = []

    def _is_valid_frame(self, index: int) -> bool:
        return len(self.frames[index]) <= 2

    def _calculate_frame_value(self, index: int) -> int:
        frame = self.frames[index]
        frame_total = sum(frame)

        if frame_total > 10:
            raise ValueError("Invalid pins count.")

        if frame_total == 10:
            # Strike
            if index < 9:
                next_frame = self._get_next_frame(index)
                if len(next_frame) != 1:
                    raise IndexError("Cannot throw bonus with an open tenth frame")
                else:
                    return 10 + next_frame[0][0]
            elif index == 9:
                if len(self.bonus_attempts) == 0:
                    return 10
                else:
                    return 10 + self.bonus_attempts[-1]
            else:
                return 10
        elif frame_total == 1:
            # Spare
            if index < 9:
                next_frame = self._get_next_frame(index)
                if len(next_frame) != 1:
                    raise ValueError("Invalid fill balls")
                else:
                    return 10 + next_frame[0][0]
            elif index == 9:
                if len(self.bonus_attempts) == 0:
                    return 10
                else:
                    return 10 + self.bonus_attempts[-1]
            else:
                return 10
        else:
            # Open frame
            if index < 9:
                return frame_total
            elif index == 9:
                if len(self.bonus_attempts) == 0:
                    return frame_total
                else:
                    return frame_total + self.bonus_attempts[-1]
            else:
                return frame_total

    def _get_next_frame(self, index: int) -> List[List[int]]:
        if index >= 9:
            return []

        next_frame = self.frames[index+1]
        while len(next_frame) < 2 and index < 9:
            index += 1
            next_frame = self.frames[index]

        return next_frame

    def roll(self, pins: int):
        if pins < 0 or pins > 10:
            raise ValueError("Invalid pins count.")

        if len(self.frames) < 10:
            self.frames.append([pins])
        else:
            if not self._is_valid_frame(-1):
                raise IndexError("Cannot throw bonus with an open tenth frame")

            if len(self.bonus_attempts) < 2:
                self.bonus_attempts.append(pins)
            else:
                self.frames[-1].append(pins)

    def score(self) -> int:
        total_score = 0
        for i in range(len(self.frames)):
            total_score += self._calculate_frame_value(i)

        return total_score

def main():
    game = BowlingGame()

    try:
        args = [int(x) for x in sys.argv[1:]]
        for arg in args:
            game.roll(arg)

        print(game.score())
    except ValueError as e:
        print(f"Error: {e}")
    except IndexError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
