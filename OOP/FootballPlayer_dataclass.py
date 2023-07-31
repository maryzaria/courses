from dataclasses import dataclass, field


@dataclass(order=True)
class FootballPlayer:
    name: str = field(compare=False)
    surname: str = field(compare=False)
    value: int = field(repr=False)


@dataclass
class FootballTeam:
    name: str
    players: list = field(init=False, default_factory=list, repr=False, compare=False)

    def add_players(self, *args):
        for player in args:
            self.players.append(player)


team1 = FootballTeam('PSG')
team2 = FootballTeam('PSG')
team3 = FootballTeam('Arsenal')

print(team1 == team2)
print(team1 != team2)
print(team1 == team3)
print(team1 != team3)