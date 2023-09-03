class HighScores:
    def __init__(self, scores):
        self.scores = sorted(scores, reverse=True)

    def get_highest(self):
        """Returns the highest score."""
        return self.scores[0] if len(self.scores) > 0 else None

    def get_last(self):
        """Returns the last added score."""
        return self.scores[-1] if len(self.scores) > 0 else None

    def personal_top_three(self):
        """Returns a list containing the three highest scores."""
        return self.scores[:3] if len(self.scores) >= 3 else []
