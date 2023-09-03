def tally(rows):
    teams = {}

    # Process each row of data
    for row in rows:
        home_team, away_team, result = row.split(';')

        # Update stats for home team
        if home_team not in teams:
            teams[home_team] = {'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0}

        teams[home_team]['MP'] += 1
        if result == 'win':
            teams[home_team]['W'] += 1
            teams[home_team]['P'] += 3
        elif result == 'draw':
            teams[home_team]['D'] += 1
            teams[home_team]['P'] += 1
        else: # It's a loss
            teams[home_team]['L'] += 1

        # Update stats for away team
        if away_team not in teams:
            teams[away_team] = {'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0}

        teams[away_team]['MP'] += 1
        if result == 'loss':
            teams[away_team]['W'] += 1
            teams[away_team]['P'] += 3
        elif result == 'draw':
            teams[away_team]['D'] += 1
            teams[away_team]['P'] += 1
        else: # It's a win
            teams[away_team]['L'] += 1

    # Build the output string
    lines = ["Team                           | MP |  W |  D |  L |  P"]
    for team, stats in sorted(teams.items(), key=lambda x: (-x[1]['P'], x[0])):
        lines.append(f"{team:<32}| {stats['MP']:>2} | {stats['W']:>2} | {stats['D']:>2} | {stats['L']:>2} | {stats['P']:>2}")

    return '\n'.join(lines)
