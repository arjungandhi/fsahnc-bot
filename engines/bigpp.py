"""
BigPP is a engine that tries to move the pieces into the shape of a big PP.
"""
from .minimal import MinimalEngine
from chess.engine import PlayResult


class BigPP(MinimalEngine):
    def search(self, board, *args):
        moves = list(board.legal_moves)
        moves.sort(key=str)
        return PlayResult(moves[0], None)
