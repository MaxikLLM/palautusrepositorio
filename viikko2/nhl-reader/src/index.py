import requests

from rich.table import Table
from rich.console import Console
from rich.prompt import Prompt

from player import Player



class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.players = []
        self.get_response(url)
        self.get_players()

    def get_players(self):
        for player in self.response:
            self.players.append(Player(player))

    def get_response(self, url):
        try:
            self.response = requests.get(url, timeout=10).json()
        except requests.exceptions.Timeout:
            print("Wroong url")

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



def ask():
    season = Prompt.ask("Season [hot_pink]\\[2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25/2025-26][/]", default="2024-25").strip()
    nationality = Prompt.ask("Nationality [hot_pink]\\[USA/FIN/CAN/SWE/CZE/RUS/SLO/FRA/GBR/SVK/DEN/NED/AUT/BLR/GER/SUI/NOR/UZB/LAT/AUS][/]", default="", )

    return season, nationality

def build_table(season, nationality, players):
    table = Table(title=f"Season {season} players from {nationality}")
    table.add_column("Player", justify="left", style="blue", no_wrap=True)
    table.add_column("teams", style="purple")
    stats = ["goals", "assists", "points"]
    for stat in stats:
        table.add_column(stat, style="green")

    for player in players:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points))

    return table

def main():
    season, nationality = ask()
    console = Console()
    reader = PlayerReader(f"https://studies.cs.helsinki.fi/nhlstats/{season}/players")
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)

    console.print(build_table(season, nationality, players))

if __name__ == "__main__":
    main()
