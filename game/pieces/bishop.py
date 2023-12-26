import numpy as np
import pygame
from game.pieces.base_piece_class import Piece


class Bishop(Piece):

    w_image = pygame.image.load('assets/pieces/wB.png')
    b_image = pygame.image.load('assets/pieces/bB.png')

    def can_move(self, new_pos, board):
        if np.abs(self.position[0] - new_pos[0]) != np.abs(self.position[1] - new_pos[1]):
            return False

        y_dif = self.position[0] - new_pos[0]
        x_dif = self.position[1] - new_pos[1]

        if y_dif < 0 and x_dif<0: #nie dziala
            for i in range(1, abs(y_dif)):
                if board[self.position[0]+i, self.position[1]+i] != 0:
                    return False
        elif y_dif<0 and x_dif>0: #dziala
            for i in range(1, abs(x_dif)):
                if board[self.position[0]+i, self.position[1]-i] != 0:
                    return False
        elif y_dif>0 and x_dif<0:   #nie dziala
            for i in range(1, abs(x_dif)):
                if board[self.position[0]-i, self.position[1]+i] != 0:
                    return False
        elif y_dif>0 and x_dif>0: #dziala
            for i in range(1, abs(x_dif)):
                if board[self.position[0]-i, self.position[1]-i] != 0:
                    return False
        return True