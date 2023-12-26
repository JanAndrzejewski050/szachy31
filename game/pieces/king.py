import numpy as np
import pygame
from game.pieces.base_piece_class import Piece
from game.pieces.pawn import *
from game.pieces.knight import *
from game.pieces.queen import *
from game.pieces.bishop import *
from game.pieces.rook import *


class King(Piece):

    w_image = pygame.image.load('assets/pieces/wK.png')
    b_image = pygame.image.load('assets/pieces/bK.png')

    def can_move(self, new_pos, board):
        if abs(self.position[0] - new_pos[0]) > 1 or abs(new_pos[1] - self.position[1]) > 1:
            return False
        if self.is_checked(new_pos, board) is True:
            print("kutas")
            return False
        return True

    def is_checked(self, new_pos, board):
        for i in range(8):
            for j in range(8):
                piece = board[i][j]
                if piece != 0 and piece != self and self.color != piece.color:
                    if piece.can_move((new_pos[0], new_pos[1]), board):
                        return True
