from players.MancalaAI import MancalaAI

class MiMancalaAI(MancalaAI):

    def get_move(self, board):
        valid_moves = board.get_valid_moves()
        game_state = (board,valid_moves)
        my_mancala_idx = 0 if self.player_num == 2 else 7
        opp_mancala_idx = 7 if self.player_num == 2 else 0