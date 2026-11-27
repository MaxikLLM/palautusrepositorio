class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.score = ""

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def score_convert(self, points):
        if points == 0:
            return "Love"
        if points == 1:
            return "Fifteen"
        if points == 2:
            return "Thirty"
        return "Forty"

    def game_situation(self, score_diff):
        if score_diff == 1:
            return f"Advantage {self.player1_name}"
        if score_diff == -1:
            return f"Advantage {self.player2_name}"
        if score_diff >= 2:
            return f"Win for {self.player1_name}"
        return f"Win for {self.player2_name}"

    def draw_situation(self, score):
        if score < 3:
            return f"{self.score_convert(score)}-All"
        else:
            return "Deuce"

    def get_score(self):
        draw = self.player1_score == self.player2_score
        atleast_4_points = self.player1_score >= 4 or self.player2_score >= 4

        if draw:
            draw_score = self.draw_situation(self.player1_score)

            return draw_score

        elif atleast_4_points:
            score_diff = self.player1_score - self.player2_score
            game_situation = self.game_situation(score_diff)

            return game_situation
        
        else:
            current_score = f"{self.score_convert(self.player1_score)}-{self.score_convert(self.player2_score)}"

            return current_score
