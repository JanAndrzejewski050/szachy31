import numpy as np
import pygame
from game.pieces.base_piece_class import Piece


class Rook(Piece):

    w_image = pygame.image.load('assets/pieces/wR.png')
    b_image = pygame.image.load('assets/pieces/bR.png')

    def can_move(self, new_pos, board):
        if self.position[0] != new_pos[0] and self.position[1] != new_pos[1]:
            return False

        # Określenie przedziałów, gdzie wieża może być
        up, down = sorted([self.position[0], new_pos[0]])
        left, right = sorted([self.position[1], new_pos[1]])

        # Sprawdzenie czy nowa pozycja mieści się w przedziałach
        if new_pos[0] < up or new_pos[0] > down or new_pos[1] < left or new_pos[1] > right:
            return False

        # Sprawdzenie czy trasa ruchu w pionie jest pusta
        if self.position[0] != new_pos[0] and any(board[i, self.position[1]] != 0 for i in range(up + 1, down)):
            return False

        # Sprawdzenie czy trasa ruchu w poziomie jest pusta
        if self.position[1] != new_pos[1] and any(board[self.position[0], j] != 0 for j in range(left + 1, right)):
            return False

        return True
