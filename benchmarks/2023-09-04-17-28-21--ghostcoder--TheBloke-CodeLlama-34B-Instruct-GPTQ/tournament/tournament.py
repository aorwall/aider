def tally(rows):
    # Create a dictionary to store the results
    results = {}

    # Loop through each row in the input
    for row in rows:
        # Split the row into the two teams
        team1, team2 = row.split(';')

        # Check if the teams are already in the results dictionary
        if team1 not in results:
            # If not, add them with default values
            results[team1] = {'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0}
        if team2 not in results:
            results[team2] = {'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0}

        # Increment the number of matches played for both teams
        results[team1]['MP'] += 1
        results[team2]['MP'] += 1

        # Determine the winner and increment their wins and points
        if row.endswith('win'):
            results[team1]['W'] += 1
            results[team1]['P'] += 3
            results[team2]['L'] += 1
        elif row.endswith('draw'):
            results[team1]['D'] += 1
            results[team1]['P'] += 1
            results[team2]['D'] += 1
            results[team2]['P'] += 1
        else:
            results[team2]['W'] += 1
            results[team2]['P'] += 3
            results[team1]['L'] += 1

    # Sort the results by points, then by name
    sorted_results = sorted(results.items(), key=lambda x: (-x[1]['P'], x[0]))

    # Return the sorted results as a list of strings
    return [f"{name}: {values['MP']} MP, {values['W']} W, {values['D']} D, {values['L']} L, {values['P']} P" for name, values in sorted_results]
