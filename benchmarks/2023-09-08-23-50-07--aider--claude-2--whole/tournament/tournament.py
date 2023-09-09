def tally(rows):
  teams = {}

  for row in rows:
    home_team, away_team, outcome = row.split(';')

    for team in [home_team, away_team]:
      if team not in teams:
        teams[team] = {'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0}

    if outcome == 'win':
      teams[home_team]['MP'] += 1
      teams[home_team]['W'] += 1
      teams[home_team]['P'] += 3
      teams[away_team]['MP'] += 1
      teams[away_team]['L'] += 1

    elif outcome == 'loss':
      teams[away_team]['MP'] += 1
      teams[away_team]['W'] += 1
      teams[away_team]['P'] += 3
      teams[home_team]['MP'] += 1
      teams[home_team]['L'] += 1

    else:
      teams[home_team]['MP'] += 1
      teams[home_team]['D'] += 1
      teams[home_team]['P'] += 1
      teams[away_team]['MP'] += 1
      teams[away_team]['D'] += 1
      teams[away_team]['P'] += 1

  output = "Team                           | MP |  W |  D |  L |  P\n"

  for team in sorted(teams, key=lambda x: (-teams[x]['P'], x)):
    stats = teams[team]
    output += f"{team:30} |  {stats['MP']:2} |  {stats['W']:2} |  {stats['D']:2} |  {stats['L']:2} |  {stats['P']:2}\n"

  return output
