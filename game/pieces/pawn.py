import numpy as np
import pygame
from game.pieces.base_piece_class import Piece


class Pawn(Piece):
    w_image = pygame.image.load('assets/pieces/wP.png')
    b_image = pygame.image.load('assets/pieces/bP.png')

    def __init__(self, color, position, size):
        super().__init__(color, position, size)
        self.moved = False

    def can_move(self, new_pos, board):
        y, x = new_pos[0], new_pos[1]

        # Pionek biały
        if self.color == "w":
            # Ruch o 2 pola w pierwszym ruchu
            if not self.moved and y == self.position[0] - 2 and x == self.position[1] and board[y, x] == 0:
                self.moved = True
                return True
            # Ruch o 1 pole do przodu
            elif y == self.position[0] - 1 and x == self.position[1] and board[y, x] == 0:
                self.moved = True
                return True
            # Bicie w przód
            elif y == self.position[0] - 1 and (x == self.position[1] - 1 or x == self.position[1] + 1):
                if board[y, x] != 0:
                    return True

        # Pionek czarny
        elif self.color == "b":
            # Ruch o 2 pola w pierwszym ruchu
            if not self.moved and y == self.position[0] + 2 and x == self.position[1] and board[y, x] == 0:
                self.moved = True
                return True
            # Ruch o 1 pole do przodu
            elif y == self.position[0] + 1 and x == self.position[1] and board[y, x] == 0:
                self.moved = True
                return True
            # Bicie w przód
            elif y == self.position[0] + 1 and (x == self.position[1] - 1 or x == self.position[1] + 1):
                if board[y, x] != 0:
                    return True

        return False
