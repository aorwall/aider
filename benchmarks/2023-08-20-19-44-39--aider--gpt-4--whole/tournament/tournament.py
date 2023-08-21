def tally(rows):
    team_data = {}
    for row in rows:
        team1, team2, result = row.split(';')
        team_data.setdefault(team1, {'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0})
        team_data.setdefault(team2, {'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0})
        team_data[team1]['MP'] += 1
        team_data[team2]['MP'] += 1
        if result == 'win':
            team_data[team1]['W'] += 1
            team_data[team1]['P'] += 3
            team_data[team2]['L'] += 1
        elif result == 'loss':
            team_data[team2]['W'] += 1
            team_data[team2]['P'] += 3
            team_data[team1]['L'] += 1
        else:  # draw
            team_data[team1]['D'] += 1
            team_data[team1]['P'] += 1
            team_data[team2]['D'] += 1
            team_data[team2]['P'] += 1

    sorted_teams = sorted(team_data.items(), key=lambda x: (-x[1]['P'], x[0]))
    output = ['Team                           | MP |  W |  D |  L |  P']
    for team, data in sorted_teams:
        output.append(f"{team:30} | {data['MP']:2} | {data['W']:2} | {data['D']:2} | {data['L']:2} | {data['P']:2}")

    return output
