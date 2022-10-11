"""
BigPP is a engine that tries to move the pieces into the shape of a big PP.
"""
from .minimal import MinimalEngine
from chess.engine import PlayResult


class BigPP(MinimalEngine):
    
    def __init__(self):
        self.mask = "/path/to/mask"
    
    
    def search(self, board, *args):
        moves = list(board.legal_moves)
        # we want to maximize the pp shape 
        # iterate through the legal moves 
        # play them and then score them based
        # on their similarity to mask
        
        
        moves.sort(key=str)
        return PlayResult(moves[0], None)

    def score_move(self,move,board):
        # returns a tuple of (move,score)
        
        # make a copy of the board 
        
        # get the piece map 
        
        # convert piece map to image 
        
        # did against self.mask 