class Team:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.games_played = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0

    def add_result(self, other_team, result):
        if result == "win":
            self.points += 3
            other_team.points -= 0
        elif result == "draw":
            self.points += 1
            other_team.points += 1
        else:
            self.points += 0
            other_team.points += 3

    @property
    def record(self):
        return f"{self.name} | {self.games_played} | {self.wins} | {self.draws} | {self.losses}"
return [team.record for team in sorted_teams]

def tally(rows):
    teams = {}
    for row in rows:
        home_team, away_team, result = row.split(";")
        if home_team not in teams:
            teams[home_team] = Team(home_team)
        if away_team not in teams:
            teams[away_team] = Team(away_team)

        ht = teams[home_team]
        at = teams[away_team]
        ht.add_result(at, result)
        at.add_result(ht, 'lose' if result == 'win' else ('draw' if result == 'draw' else 'win'))
        ht.games_played += 1
        at.games_played += 1

    sorted_teams = sorted(teams.values(), key=lambda x: (-x.points, x.name))
    return [team.record for team in sorted_teams]

print(tally(['a;b;win', 'c;d;win', 'b;c;win', 'd;a;win']))