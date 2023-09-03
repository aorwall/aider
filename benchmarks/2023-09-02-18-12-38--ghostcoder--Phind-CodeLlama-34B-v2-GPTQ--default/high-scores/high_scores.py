class HighScores:
    def __init__(self, scores=None):
        if scores is None:
            self.scores = []
        else:
            self.scores = scores

    def latest_score(self):
        # Returns the last added score
        return self.scores[-1] if self.scores else None

    def personal_best(self):
        # Returns the highest score from the list
        return max(self.scores) if self.scores else None

    def top_three_scores(self):
        # Returns the three highest scores
        sorted_scores = sorted(self.scores, reverse=True)[:3]
        return sorted_scores if len(sorted_scores) == 3 else None

    def add_score(self, score):
        # Add a new score to the list
        self.scores.append(score)
