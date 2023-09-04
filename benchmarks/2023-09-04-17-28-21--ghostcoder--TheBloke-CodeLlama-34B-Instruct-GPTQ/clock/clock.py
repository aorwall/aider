class Clock:
    def __init__(self, hour=0, minute=0):
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        return f"{self.hour:0>2d}:{self.minute:0>2d}"

    def __str__(self):
        return f"{self.hour:0>2d}:{self.minute:0>2d}"

    def __eq__(self, other):
        return (self.hour == other.hour) and (self.minute == other.minute)

    def __add__(self, minutes):
        self.minute += minutes
        while self.minute >= 60:
            self.minute -= 60
            self.hour += 1
        while self.hour >= 24:
            self.hour -= 24
        return self

    def __sub__(self, minutes):
        self.minute -= minutes
        while self.minute < 0:
            self.minute += 60
            self.hour -= 1
        while self.hour < 0:
            self.hour += 24
        return self

def test_clock():
    assert repr(Clock()) == '00:00'
    assert repr(Clock(1, 2)) == '01:02'
    assert repr(Clock('1', '2')) == '01:02'
    assert repr(Clock(1, '2')) == '01:02'
    assert repr(Clock('1', 2)) == '01:02'
    assert repr(Clock(1.5, 2.5)) == '01:02'

if __name__ == "__main__":
    test_clock()
