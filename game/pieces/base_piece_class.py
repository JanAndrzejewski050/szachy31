import numpy
import pygame
from game.chess_board import *


class Piece:

    def __init__(self, color, position, size):
        self.color = color
        self.position = position
        self.size = size


    def draw_piece(self, screen, board_size, w_image, b_image):
        w_scaled_image = pygame.transform.scale(w_image, (self.size, self.size))
        b_scaled_image = pygame.transform.scale(b_image, (50, 50))
        if self.color == "w":
            screen.blit(w_scaled_image, (self.position[1]*board_size//8 + screen.get_width()//2 - board_size//2+13, self.position[0]*board_size//8+15))
        else:
            screen.blit(b_scaled_image, (self.position[1]*board_size//8 + screen.get_width()//2 - board_size//2+13, self.position[0]*board_size//8+15))


    def is_clicked_on(self, screen, board_size):
        x = self.position[1]*board_size//8 + screen.get_width()//2 - board_size//2+13
        y = self.position[0]*board_size//8+15
        if pygame.mouse.get_pressed()[0] is True and x < pygame.mouse.get_pos()[0] < x+self.size and y < pygame.mouse.get_pos()[1] < y+self.size:
            return True


    # wPawn = 10
    # wBishop = 31
    # wKnight = 30
    # wRook = 50
    # wQueen = 90
    # wKing = 10000
    #
    # bPawn = -10
    # bBishop = -31
    # bKnight = -30
    # bRook = -50
    # bQueen = -90
    # bKing = -10000
