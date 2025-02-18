class HighScores:
    def __init__(self, scores):
        self.scores = sorted([int(x) for x in scores], reverse=True)

    def latest_score(self):
        return self.scores[-1]

    def personal_best(self):
        return self.scores[0]

    def top_three(self):
        return self.scores[:3]

    def personal_top_three(self):
        # The following two lines ensure that we only consider each person's highest score once
        unique_scores = list(set(self.scores))
        unique_scores.sort(reverse=True)

        if len(unique_scores) >= 3:
            return unique_scores[:3]
        else:
            return unique_scores
