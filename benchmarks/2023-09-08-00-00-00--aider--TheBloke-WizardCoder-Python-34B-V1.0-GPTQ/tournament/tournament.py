def tally(rows):
    results = {}
    for row in rows:
        team1, team2, outcome = row.split(";")
        if team1 not in results:
            results[team1] = {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0}
        if team2 not in results:
            results[team2] = {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0}

        if outcome == "win":
            results[team1]["W"] += 1
            results[team1]["P"] += 3
            results[team2]["L"] += 1
        elif outcome == "draw":
            results[team1]["D"] += 1
            results[team1]["P"] += 1
            results[team2]["D"] += 1
            results[team2]["P"] += 1
        else:
            results[team1]["L"] += 1
            results[team2]["W"] += 1
            results[team2]["P"] += 3

        results[team1]["MP"] += 1
        results[team2]["MP"] += 1

    sorted_results = sorted(results.items(), key=lambda x: (-x[1]["P"], x[0]))
    header = "Team                           | MP |  W |  D |  L |  P"
    separator = "-" * len(header)
    output = [header, separator]

    for team, data in sorted_results:
        output.append(f"{team} {data['MP']} {data['W']} {data['D']} {data['L']} {data['P']}")

    return "\n".join(output)
