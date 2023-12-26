import numpy as np
import pygame
from game.pieces.base_piece_class import Piece


class Knight(Piece):

    w_image = pygame.image.load('assets/pieces/wN.png')
    b_image = pygame.image.load('assets/pieces/bN.png')

    def can_move(self, new_pos, board):
        jumps = np.array([(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)])
        diff = np.array(self.position) - np.array(new_pos)
        return np.any((diff == jumps).all(axis=1))