class HighScores:
    def __init__(self, scores):
        self.scores = sorted(scores, reverse=True)

    def latest(self):
        if not self.scores:
            raise ValueError('No scores available')
        return self.scores[0]

    def personal_best(self):
        if not self.scores:
            raise ValueError('No scores available')
        return max(self.scores)

    def personal_top_three(self):
        if len(self.scores) < 3:
            raise ValueError('Not enough scores available')
        return self.scores[:3]

    def get_highest(self):
        if not self.scores:
            raise ValueError('No scores available')
        return self.scores[0]

    def get_last(self):
        if not self.scores:
            raise ValueError('No scores available')
        return self.scores[-1]

    def get_top_three(self):
        if len(self.scores) < 3:
            raise ValueError('Not enough scores available')
        return self.scores[:3]
