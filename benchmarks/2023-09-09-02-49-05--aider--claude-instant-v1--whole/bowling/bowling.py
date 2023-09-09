class BowlingGame:

    def __init__(self):
        self.frames = [0] * 10
        self.current_frame = 0
        self.score = 0
        self.bonus_rolls = 0

    def roll(self, pins):
        if self.current_frame >= 10 and self.bonus_rolls == 0:
            raise ValueError("cannot roll after 10th frame")

        if self.current_frame == 10 and self.bonus_rolls > 0:
            self.bonus_rolls -= 1

        if self.frames[self.current_frame] != 0:
            self.frames[self.current_frame] += pins
        else:
            self.frames[self.current_frame] = pins

        if self.is_strike(pins):
            self.current_frame += 1
        elif self.is_spare(pins): 
            self.current_frame += 1
            if self.current_frame == 10:
                self.bonus_rolls = 1
        else:
            self.current_frame += 1

    def is_strike(self, pins):
        return pins == 10

    def is_spare(self, pins):
        return self.frames[self.current_frame] == 10

    def score(self):
        score = 0
        frame_index = 0
        for frame in self.frames:
            if self.is_strike(frame):
                score += 10 + self.frames[frame_index+1] + self.frames[frame_index+2]
                frame_index += 1
            elif self.is_spare(frame):
                if frame_index == 9:
                    score += 10 + self.frames[frame_index+1]
                else:
                    score += 10 + self.frames[frame_index+2]
                frame_index += 2
            else:
                score += sum(frame)
                frame_index += 1
        return score
