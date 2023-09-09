class HighScores:
    def __init__(self, scores):
        self.scores = scores
        
    def highest(self):
        return max(self.scores)
        
    def latest(self):
        return self.scores[-1]
        
    def top_3(self):
        return sorted(self.scores, reverse=True)[:3]

    def personal_best(self):
        return max(self.scores)

    def personal_top_three(self):
        return sorted(self.scores, reverse=True)[:3]
