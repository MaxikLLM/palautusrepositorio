import requests
from player import Player
from rich import print as rprint
from rich.table import Table
from rich.console import Console
from rich.prompt import Prompt

class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.players = []
        self.response = requests.get(self.url).json()
        self.get_players()

    def get_players(self):
        for player in self.response:
            self.players.append(Player(player))


class PlayerStats():
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, country):
        players = []

        for player in self.reader.players:
            if player.nationality == country:
                players.append(player)

        players.sort(key=lambda player: player.points, reverse=True)
        return players


def main():
    console = Console()
    season = Prompt.ask("Season [hot_pink]\\[2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25/2025-26][/]", default="2024-25").strip()
    nationality = Prompt.ask("Nationality [hot_pink]\\[USA/FIN/CAN/SWE/CZE/RUS/SLO/FRA/GBR/SVK/DEN/NED/AUT/BLR/GER/SUI/NOR/UZB/LAT/AUS][/]", default="", )
    reader = PlayerReader(f"https://studies.cs.helsinki.fi/nhlstats/{season}/players")
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)

    table = Table(title=f"Season {season} players from {nationality}")
    table.add_column("Player", justify="left", style="blue", no_wrap=True)
    table.add_column("teams", style="purple")
    table.add_column("goals", style="green")
    table.add_column("assists", style="green")
    table.add_column("points", style="green")

    for player in players:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points))

    console.print(table)

if __name__ == "__main__":
    main()
