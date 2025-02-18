def tally(rows):
    # Create a dictionary to store the statistics of each team
    stats = {}

    # Define a helper function to update the statistics of a team
    def update_stats(team, mp, w, d, l, p):
        if team not in stats:
            stats[team] = {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0}

        stats[team]["MP"] += mp
        stats[team]["W"] += w
        stats[team]["D"] += d
        stats[team]["L"] += l
        stats[team]["P"] += p

    # Parse the rows and update the statistics of each team
    for row in rows:
        team1, team2, outcome = row.split(';')

        if outcome == 'win':
            update_stats(team1, 1, 1, 0, 0, 3)
            update_stats(team2, 1, 0, 0, 1, 0)
        elif outcome == 'draw':
            update_stats(team1, 1, 0, 1, 0, 1)
            update_stats(team2, 1, 0, 1, 0, 1)
        else:  # outcome == 'loss'
            update_stats(team1, 1, 0, 0, 1, 0)
            update_stats(team2, 1, 1, 0, 0, 3)

    # Convert the dictionary to a list of tuples
    result = [(team, stats[team]['MP'], stats[team]['W'], stats[team]['D'], stats[team]['L'], stats[team]['P']) for team in stats]
    result = sorted(result, key=lambda x: (-x[-1], x[0]))

    return result
