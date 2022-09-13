import random
from chess.engine import PlayResult
from .minimal import MinimalEngine


# Strategy names and ideas from tom7's excellent eloWorld video
class RandomMove(MinimalEngine):
    def search(self, board, *args):
        return PlayResult(random.choice(list(board.legal_moves)), None)


class Alphabetical(MinimalEngine):
    def search(self, board, *args):
        moves = list(board.legal_moves)
        moves.sort(key=board.san)
        return PlayResult(moves[0], None)


class FirstMove(MinimalEngine):
    """Gets the first move when sorted by uci representation"""

    def search(self, board, *args):
        moves = list(board.legal_moves)
        moves.sort(key=str)
        return PlayResult(moves[0], None)
