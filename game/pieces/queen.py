import numpy as np
import pygame
from game.pieces.base_piece_class import Piece


class Queen(Piece):
    w_image = pygame.image.load('assets/pieces/wQ.png')
    b_image = pygame.image.load('assets/pieces/bQ.png')

    def can_move(self, new_pos, board):
        y_dif = self.position[0] - new_pos[0]
        x_dif = self.position[1] - new_pos[1]

        # Sprawdź ruch w pionie
        if x_dif == 0:
            direction_y = int(y_dif / np.abs(y_dif))
            for i in range(1, np.abs(y_dif)):
                if board[self.position[0] - i * direction_y, self.position[1]] != 0:
                    return False

        # Sprawdź ruch w poziomie
        elif y_dif == 0:
            direction_x = int(x_dif / np.abs(x_dif))
            for i in range(1, np.abs(x_dif)):
                if board[self.position[0], self.position[1] - i * direction_x] != 0:
                    return False

        # Sprawdź ruch po przekątnej
        elif np.abs(y_dif) == np.abs(x_dif):
            direction_y = int(y_dif / np.abs(y_dif))
            direction_x = int(x_dif / np.abs(x_dif))
            for i in range(1, np.abs(y_dif)):
                if board[self.position[0] - i * direction_y, self.position[1] - i * direction_x] != 0:
                    return False

        else:
            return False

        return True
