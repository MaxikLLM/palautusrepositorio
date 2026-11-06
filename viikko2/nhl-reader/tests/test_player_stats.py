import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from index import PlayerStats
from player import Player


class StubPlayerReader:
    def __init__(self, players):
        self.players = players


class TestPlayerStats(unittest.TestCase):
    def setUp(self):
        self.players = [
            Player({"name": "Alex", "nationality": "FIN", "team": "BOS", "goals": 20, "assists": 30}),
            Player({"name": "Bailey", "nationality": "USA", "team": "BOS", "goals": 35, "assists": 10}),
            Player({"name": "Casey", "nationality": "FIN", "team": "DAL", "goals": 18, "assists": 40}),
            Player({"name": "Drew", "nationality": "CAN", "team": "DAL", "goals": 25, "assists": 15}),
        ]
        self.stats = PlayerStats(StubPlayerReader(self.players))

    def test_top_scorers_by_nationality_filters_and_sorts_by_points(self):
        result = self.stats.top_scorers_by_nationality("FIN")

        self.assertEqual(["Casey", "Alex"], [player.name for player in result])

    def test_top_scorers_by_nationality_returns_empty_for_no_match(self):
        self.assertEqual([], self.stats.top_scorers_by_nationality("SWE"))

    def test_top_scorers_by_team_filters_and_sorts_by_points(self):
        result = self.stats.top_scorers_by_team("DAL")

        self.assertEqual(["Casey", "Drew"], [player.name for player in result])

    def test_top_scorers_by_team_returns_empty_for_no_match(self):
        self.assertEqual([], self.stats.top_scorers_by_team("MTL"))

    def test_top_goal_scorers_sorts_by_goals_and_limits_results(self):
        result = self.stats.top_goal_scorers(2)

        self.assertEqual(["Bailey", "Drew"], [player.name for player in result])

    def test_top_goal_scorers_returns_all_when_limit_exceeds_player_count(self):
        result = self.stats.top_goal_scorers(10)

        self.assertEqual(["Bailey", "Drew", "Alex", "Casey"], [player.name for player in result])


if __name__ == "__main__":
    unittest.main()