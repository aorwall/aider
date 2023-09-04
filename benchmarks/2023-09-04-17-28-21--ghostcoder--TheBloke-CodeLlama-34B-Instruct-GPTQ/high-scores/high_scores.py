class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def personal_best(self):
        """Returns the highest score."""
        return max(self.scores)

    def latest_score(self):
        """Returns the last added score."""
        return self.scores[-1]

    def personal_top_three(self):
        """Returns the top three scores."""
        return sorted(self.scores, reverse=True)[:3]
