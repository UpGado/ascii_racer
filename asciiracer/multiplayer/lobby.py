class Lobby:
    def __init__(self):
        self.score_table = {}

    def create_record_for_new_player(self, player_id: int):
        self.score_table[player_id] = 0

    def update_player_score(self, player_id: int, score: int):
        self.score_table[player_id] = score


