class players:
    def __init__(self, name, position, rating, team):
        self.name = name
        self.position = position
        self.rating = rating
        self.team = team

    def titles(self):
        if team == patriots:
            return 6
        elif team == ravens:
            return 3
        elif team == chiefs:
            return 3
        elif team == forniners:
            return 6
        else:
            return 2

class MVP(players):
    pass

MVP_1 = MVP("Tom", "QB", 91, "patriots")
MVP_2 = MVP("Ben", "QB", 90, "steelers")
MVP_3 = MVP("Russel", "QB", 95, "seahawks")
MVP_4 = MVP("Josh", "QB", 90, "bills")
MPV_5 = MVP("Patrick", "QB", 96, "chiefs")
MVP_6 = MVP("Derrick", "RB", 95, "titans")


print(MVP_1.name)
print(MVP_2.rating)
