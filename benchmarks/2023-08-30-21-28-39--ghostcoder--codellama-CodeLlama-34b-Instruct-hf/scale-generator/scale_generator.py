class Scale:
    def __init__(self, tonic):
        self.tonic = tonic

    def chromatic_scale(self):
        chromatic_scale = []
        for i in range(12):
            chromatic_scale.append(self.tonic + i)
        return chromatic_scale

    def diatonic_scale(self, intervals):
        diatonic_scale = [self.tonic]
        for interval in intervals:
            if interval == "M":
                diatonic_scale.append(self.tonic + 1)
            elif interval == "m":
                diatonic_scale.append(self.tonic + 0.5)
            else:
                raise ValueError("Invalid interval")
        return diatonic_scale

    def interval(self, interval):
        if interval == "M":
            return self.tonic + 1
        elif interval == "m":
            return self.tonic + 0.5
        else:
            raise ValueError("Invalid interval")
