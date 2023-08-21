def tally(rows):
    teams = {}
    for row in rows:
        team1, team2, result = row.split(";")
        if team1 not in teams:
            teams[team1] = {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0}
        if team2 not in teams:
            teams[team2] = {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0}

        teams[team1]["MP"] += 1
        teams[team2]["MP"] += 1

        if result == "win":
            teams[team1]["W"] += 1
            teams[team1]["P"] += 3
            teams[team2]["L"] += 1
        elif result == "loss":
            teams[team1]["L"] += 1
            teams[team2]["W"] += 1
            teams[team2]["P"] += 3
        elif result == "draw":
            teams[team1]["D"] += 1
            teams[team1]["P"] += 1
            teams[team2]["D"] += 1
            teams[team2]["P"] += 1

    table = []
    for team, stats in teams.items():
        table.append([team, stats["MP"], stats["W"], stats["D"], stats["L"], stats["P"]])

    table.sort(key=lambda x: (-x[5], x[0]))

    result = ["Team                           | MP |  W |  D |  L |  P"]
    for row in table:
        result.append("{:<30}|{:>3} |{:>3} |{:>3} |{:>3} |{:>3}".format(*row))

    return result