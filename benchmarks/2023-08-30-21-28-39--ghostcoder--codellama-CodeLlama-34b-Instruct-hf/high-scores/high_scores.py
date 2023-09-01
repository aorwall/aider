class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def get_high_score(self):
        return max(self.scores)

    def get_last_score(self):
        return self.scores[-1]

    def get_top_scores(self, n):
        return sorted(self.scores, reverse=True)[:n]
