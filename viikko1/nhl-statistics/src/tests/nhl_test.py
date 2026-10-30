import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search(self):
        player = self.stats.search("Gretzky")
        self.assertEqual(player.name, "Gretzky")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.goals, 35)
        self.assertEqual(player.assists, 89)
        
    def test_search_not_found(self):
        player = self.stats.search("Anon")
        self.assertIsNone(player)

    def test_team(self):
        players = self.stats.team("PIT")
        self.assertEqual(len(players), 1)
        self.assertEqual(players[0].name, "Lemieux")

    def test_top(self):
        top_players = self.stats.top(3)
        self.assertEqual(len(top_players), 4)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Lemieux")
        self.assertEqual(top_players[0].points, 124)

    def test_new_top(self):
        top_players = self.stats.top(3, SortBy.GOALS)
        self.assertEqual(len(top_players), 4)
        self.assertEqual(top_players[0].name, "Lemieux")
        self.assertEqual(top_players[0].points, 99)
        self.assertEqual(top_players[0].goals, 45)

        top_players_assists = self.stats.top(3, SortBy.ASSISTS)
        self.assertEqual(len(top_players_assists), 4)
        self.assertEqual(top_players_assists[1].name, "Yzerman")
        self.assertEqual(top_players_assists[1].points, 98)
        self.assertEqual(top_players_assists[1].assists, 56)

    def test_top_invalid(self):
        with self.assertRaises(ValueError):
            self.stats.top(3, "random")

    