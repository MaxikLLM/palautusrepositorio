class Player:
    def __init__(self, player_dict):
        self.name = player_dict['name']
        self.nationality = player_dict['nationality']
        self.team = player_dict['team']
        self.assists = player_dict['assists']
        self.goals = player_dict['goals']
        self.points = self.goals + self.assists

    def __str__(self):
        return f"{self.name:20} {self.team:14} {self.goals:1} + {self.assists:1} = {self.points:2}"
