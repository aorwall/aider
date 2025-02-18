class HighScores:
    def __init__(self, scores):
        self.scores = sorted(scores)


    def personal_top_three(self):
        """Returns a list of the top three scores for this player."""
        if len(self.scores) < 3:
            return self.scores
        else:
            return self.scores[-3:]

    def personal_best(self):
        """Returns the best (i.e., highest) score for this player."""
        if len(self.scores) > 0:
            return max(self.scores)
        else:
            raise ValueError("No scores available.")

    def personal_worst(self):
        """Returns the worst (i.e., lowest) score for this player."""
        if len(self.scores) > 0:
            return min(self.scores)
        else:
            raise ValueError("No scores available.")

    def personal_average(self):
        """Returns the average of all the scores for this player."""
        if len(self.scores) > 0:
            return sum(self.scores)/len(self.scores)
        else:
            raise ValueError("No scores available.")

    def personal_standard_deviation(self):
        """Returns the standard deviation of this player's scores."""
        import math
        if len(self.scores) > 0:
            mean = sum(self.scores)/len(self.scores)
            variance = sum((score - mean)**2 for score in self.scores)/len(self.scores)
            stddev = math.sqrt(variance)
            return round(stddev, 2)
        else:
            raise ValueError("No scores available.")

    @staticmethod
    def from_file(filename):
        """Creates a HighScores instance from a given filename.
           Assumes that each line contains one integer on it."""
        with open(filename, 'r') as f:
            lines = [int(line.strip()) for line in f.readlines()]
        return HighScores(lines)

    def get_highest(self):
        """Returns the highest score."""
        if len(self.scores) > 0:
            return self.scores[-1]
        else:
            raise ValueError("No scores available.")

    def get_last(self):
        """Returns the last added score."""
        if len(self.scores) > 0:
            return self.scores[0]
        else:
            raise ValueError("No scores available.")

    def get_top_three(self):
        """Returns the three highest scores."""
        if len(self.scores) >= 3:
            return self.scores[:3][::-1]
        elif len(self.scores) == 2:
            return self.scores[::-1]
        elif len(self.scores) == 1:
            return self.scores
        else:
            raise ValueError("Not enough scores available.")
