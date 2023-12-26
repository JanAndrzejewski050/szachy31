import pygame
import numpy as np
import time
from game.chess_board import *
from game.pieces.pawn import *


pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
warm_white = (255, 220, 178)
light_brown = (205, 133, 63)
board = ChessBoard(600, (warm_white, light_brown))


def main():

    board.graphical_board(screen)
    board.draw_pieces(screen)
    board.move_piece(screen)


while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()

    screen.fill((0, 0, 0))

    main()

    pygame.display.flip()
    pygame.time.Clock().tick(60)
