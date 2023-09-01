from collections import defaultdict
def tally(rows):
    teams = defaultdict(list)
    for row in rows:
        team1, team2, outcome = row.split(';')
        teams[team1].append(outcome)
        teams[team2].append(outcome)

    points = {}
    for team, matches in teams.items():
        wins = matches.count('win')
        draws = matches.count('draw')
        losses = matches.count('loss')
        points[team] = wins * 3 + draws

    return sorted(points.items(), key=lambda x: (-x[1], x[0]))
