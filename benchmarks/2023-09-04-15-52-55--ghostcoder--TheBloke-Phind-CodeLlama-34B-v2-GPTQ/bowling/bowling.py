class BowlingGame:
    def __init__(self):
        self.frames = [[]] * 10
        self.current_frame = 0
        self.bonus_for_next_fill_ball = False

    def roll(self, pins):
        if pins < 0 or pins > 10:
            raise ValueError('Invalid number of pins')

        if self.current_frame == 10:
            if len(self.frames[9]) == 2 or \
                    (len(self.frames[9]) == 1 and self.frames[9][0] != 10):
                raise ValueError('No more than 3 balls allowed in 10th frame')

        if self.is_strike():
            if self.current_frame == 9:
                self.frames[self.current_frame].append(pins)
                return
            elif self.current_frame >= 8:
                self.frames[7].extend([pins, self.frames[8].pop(0)])
                self.bonus_for_next_fill_ball = True
            else:
                self.frames[self.current_frame].append(pins)

        elif self.is_spare():
            if self.current_frame <= 8:
                self.frames[self.current_frame].append(pins)
            else:
                self.frames[9].append(pins)
                self.bonus_for_next_fill_ball = True

        else:
            if len(self.frames[self.current_frame]) == 2:
                if self.current_frame == 9:
                    self.frames[self.current_frame - 1].extend(self.frames[self.current_frame])
                else:
                    self.frames[self.current_frame - 2].extend(self.frames[self.current_frame])
                self.current_frame += 1
            self.frames[self.current_frame].append(pins)

        if self.current_frame < 9:
            self.current_frame += 1

    def is_strike(self):
        return len(self.frames[self.current_frame]) == 0 or self.frames[self.current_frame][0] == 10

    def is_spare(self):
        return sum(self.frames[self.current_frame]) == 10

    def score(self):
        result = 0
        for i in range(8):
            result += sum(self.frames[i])
        result += sum(self.frames[9][:2])
        if self.bonus_for_next_fill_ball:
            result += self.frames[9][2]
        return result
