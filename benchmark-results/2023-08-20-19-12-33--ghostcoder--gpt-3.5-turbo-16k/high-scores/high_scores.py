class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def highest(self):
        highest_score = max(self.scores)
        return highest_score

    def last_added(self):
        last_score = self.scores[-1]
        return last_score

    def top_three(self):
        sorted_scores = sorted(self.scores, reverse=True)
        top_three_scores = sorted_scores[:3]
        return top_three_scores

    def personal_best(self):
        return self.highest()

    def personal_top_three(self):
        return self.top_three()

    def latest(self):
        return self.last_added()