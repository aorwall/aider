import sys
from collections import defaultdict

def tally(rows):
    results = defaultdict(lambda: [0, 0, 0, 0, 0, 0])

    for row in rows:
        home_team, away_team, outcome = row.split(';')

        if outcome == 'win':
            results[home_team][0] += 1
            results[home_team][3] += 1
            results[away_team][0] += 1
            results[away_team][5] += 1
        elif outcome == 'draw':
            results[home_team][0] += 1
            results[home_team][4] += 1
            results[away_team][0] += 1
            results[away_team][4] += 1
        else:
            results[home_team][0] += 1
            results[home_team][5] += 1
            results[away_team][0] += 1
            results[away_team][3] += 1

    sorted_results = sorted(results.items(), key=lambda x: (-x[1][3], x[0]))

    print("{:<30} | {:^3} | {:^2} | {:^2} | {:^2} | {:^2}".format("Team", "MP", "W", "D", "L", "P"))
    print("-"*50)

    for team, record in sorted_results:
        points = record[3]*3 + record[4]*1 + record[5]*0
        print("{:<30} | {:>3} | {:>2} | {:>2} | {:>2} | {:>2}".format(team, sum([record[i] for i in [0, 1, 2]]), record[1], record[4], record[5], points))

if __name__ == "__main__":
    lines = []
    while True:
        try:
            lines.append(input())
        except EOFError:
            break
    tally(lines)
