class BowlingGame:
    def __init__(self):
        self._frames = [[]] # list of frames, where each frame is a list of rolls
        self._current_frame_index = -1 # index of current frame (-1 means no rolls yet)

    def roll(self, pins):
        if len(self._frames[self._current_frame_index]) == 2 or (len(self._frames[self._current_frame_index]) == 1 and self._frames[self._current_frame_index][-1] == 10):
            # start new frame after strike or spare
            self._frames.append([pins])
            self._current_frame_index += 1
        else:
            # add roll to current frame
            self._frames[self._current_frame_index].append(pins)

    def _calculate_frame_score(self, frame_index):
        total = sum(self._frames[frame_index])
        if total > 10:
            raise ValueError("Invalid number of pins")
        elif total == 10:
            return 10 + self._next_two_balls_for_strike(frame_index+1)
        elif total < 10:
            next_frame_start = frame_index + 1
            while len(self._frames[next_frame_start]) == 0:
                next_frame_start += 1 # skip empty frames
            if len(self._frames[next_frame_start]) >= 2:
                bonus = sum(self._frames[next_frame_start][:2])
            else:
                bonus = 0
            return total + bonus
        else:
            return total

    def _next_two_balls_for_strike(self, frame_index):
        total = 0
        for i in range(2):
            try:
                total += self._frames[frame_index][i]
            except IndexError:
                break
        return total

    def score(self):
        result = 0
        for i in range(min(10, len(self._frames)):
            result += self._calculate_frame_score(i)
        return result
