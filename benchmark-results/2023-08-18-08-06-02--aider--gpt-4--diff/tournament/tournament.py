def tally(rows):
    teams = {}

    for row in rows:
        team1, team2, result = row.split(';')

        if team1 not in teams:
            teams[team1] = {'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0}
        if team2 not in teams:
            teams[team2] = {'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0}

        teams[team1]['MP'] += 1
        teams[team2]['MP'] += 1

        if result == 'win':
            teams[team1]['W'] += 1
            teams[team1]['P'] += 3
            teams[team2]['L'] += 1
        elif result == 'loss':
            teams[team2]['W'] += 1
            teams[team2]['P'] += 3
            teams[team1]['L'] += 1
        elif result == 'draw':
            teams[team1]['D'] += 1
            teams[team1]['P'] += 1
            teams[team2]['D'] += 1
            teams[team2]['P'] += 1

    table = ['Team                           | MP |  W |  D |  L |  P']
    for team, data in sorted(teams.items(), key=lambda x: (-x[1]['P'], x[0])):
        table.append(f"{team:30} | {data['MP']:2} | {data['W']:2} | {data['D']:2} | {data['L']:2} | {data['P']:2}")

    return table
