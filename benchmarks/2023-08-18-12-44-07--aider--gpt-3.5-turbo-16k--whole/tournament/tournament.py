def tally(rows):
    teams = {}
    for row in rows:
        team1, team2, outcome = row.split(';')
        if team1 not in teams:
            teams[team1] = {'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0}
        if team2 not in teams:
            teams[team2] = {'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0}

        teams[team1]['MP'] += 1
        teams[team2]['MP'] += 1

        if outcome == 'win':
            teams[team1]['W'] += 1
            teams[team1]['P'] += 3
            teams[team2]['L'] += 1
        elif outcome == 'loss':
            teams[team1]['L'] += 1
            teams[team2]['W'] += 1
            teams[team2]['P'] += 3
        elif outcome == 'draw':
            teams[team1]['D'] += 1
            teams[team1]['P'] += 1
            teams[team2]['D'] += 1
            teams[team2]['P'] += 1

    sorted_teams = sorted(teams.items(), key=lambda x: (-x[1]['P'], x[0]))

    table = []
    for team, stats in sorted_teams:
        table.append(f"{team.ljust(30)} | {stats['MP']} | {stats['W']} | {stats['D']} | {stats['L']} | {stats['P']}")

    table.insert(0, "Team                           | MP |  W |  D |  L |  P")

    return '\n'.join(table)
