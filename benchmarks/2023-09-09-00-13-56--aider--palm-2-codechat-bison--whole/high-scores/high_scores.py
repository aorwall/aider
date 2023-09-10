class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def get_highest_score(self):
        return max(self.scores)

    def get_last_added_score(self):
        return self.scores[-1]

    def get_three_highest_scores(self):
        return sorted(self.scores, reverse=True)[:3]
