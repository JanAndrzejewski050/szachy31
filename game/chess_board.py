import numpy as np
import pygame
from game.pieces.base_piece_class import *
from game.pieces.pawn import *
from game.pieces.king import *
from game.pieces.knight import *
from game.pieces.queen import *
from game.pieces.bishop import *
from game.pieces.rook import *


class ChessBoard:
    piece_size = 52
    board = np.zeros((8, 8), classmethod)

    mouse_clicked = False
    piece_to_move = None
    mouse_hold = False
    turn = "w"


    def __init__(self, size, colors):
        self.size = size
        self.colors = colors


    def graphical_board(self, screen):
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 1:
                    pygame.draw.rect(screen, self.colors[1], (
                        (i * self.size // 8 + screen.get_width() // 2 - self.size // 2),
                        j * self.size // 8 + screen.get_height() // 2 - self.size // 2, self.size // 8, self.size // 8))
                else:
                    pygame.draw.rect(screen, self.colors[0], (
                        (i * self.size // 8 + screen.get_width() // 2 - self.size // 2),
                        j * self.size // 8 + screen.get_height() // 2 - self.size // 2, self.size // 8, self.size // 8))


    def draw_pieces(self, screen):
        for i in range(8):
            for j in range(8):
                if ChessBoard.board[i][j] != 0:
                    piece = ChessBoard.board[i][j]
                    piece.draw_piece(screen, self.size, piece.w_image, piece.b_image)

                    if piece.is_clicked_on(screen, self.size) is True and ChessBoard.turn == piece.color and\
                            ChessBoard.mouse_hold is False and ChessBoard.mouse_clicked is False:
                        ChessBoard.piece_to_move = (piece, i, j)
                        ChessBoard.mouse_clicked = True
                        ChessBoard.mouse_hold = True

        if pygame.mouse.get_pressed()[0] is False:
            ChessBoard.mouse_hold = False

        if pygame.mouse.get_pressed()[2] is True:
            ChessBoard.piece_to_move = None
            ChessBoard.mouse_clicked = False


    def move_piece(self, screen):
        if ChessBoard.piece_to_move is not None and pygame.mouse.get_pressed()[0] is True \
                and ChessBoard.mouse_hold is False and ChessBoard.mouse_clicked is True:

            pos_i = ChessBoard.piece_to_move[1]
            pos_j = ChessBoard.piece_to_move[2]

            mouse_j = (pygame.mouse.get_pos()[0] - (screen.get_width() - self.size) // 2) // (self.size // 8)
            mouse_i = (pygame.mouse.get_pos()[1]) // (self.size // 8)
            new_pos = (mouse_i, mouse_j)

            piece_to_move = ChessBoard.piece_to_move[0]
            attacked_piece = ChessBoard.board[mouse_i][mouse_j]

            if attacked_piece != 0 and attacked_piece.color == piece_to_move.color:
                return 0

            if (mouse_i != pos_i or mouse_j != pos_j) and piece_to_move.can_move(new_pos, ChessBoard.board):

                piece_to_move.position = (mouse_i, mouse_j)

                ChessBoard.board[pos_i][pos_j] = 0
                ChessBoard.board[mouse_i][mouse_j] = piece_to_move

                ChessBoard.mouse_clicked = False
                ChessBoard.piece_to_move = None
                ChessBoard.mouse_hold = True

                if ChessBoard.turn == "w":
                    ChessBoard.turn = "b"
                else:
                    ChessBoard.turn = "w"


    board[7, 4] = King("w", (7, 4), piece_size)
    board[7, 3] = Queen("w", (7, 3), piece_size)
    board[7, 7] = Rook("w", (7, 7), piece_size)
    board[7, 0] = Rook("w", (7, 0), piece_size)
    board[7, 2] = Bishop("w", (7, 2), piece_size)
    board[7, 5] = Bishop("w", (7, 5), piece_size)
    board[7, 6] = Knight("w", (7, 6), piece_size)
    board[7, 1] = Knight("w", (7, 1), piece_size)
    board[6, 1] = Pawn("w", (6, 1), piece_size)
    board[6, 2] = Pawn("w", (6, 2), piece_size)
    board[6, 3] = Pawn("w", (6, 3), piece_size)
    board[6, 4] = Pawn("w", (6, 4), piece_size)
    board[6, 5] = Pawn("w", (6, 5), piece_size)
    board[6, 6] = Pawn("w", (6, 6), piece_size)
    board[6, 7] = Pawn("w", (6, 7), piece_size)
    board[6, 0] = Pawn("w", (6, 0), piece_size)

    board[0, 4] = King("b", (0, 4), piece_size)
    board[0, 3] = Queen("b", (0, 3), piece_size)
    board[0, 0] = Rook("b", (0, 0), piece_size)
    board[0, 7] = Rook("b", (0, 7), piece_size)
    board[0, 2] = Bishop("b", (0, 2), piece_size)
    board[0, 5] = Bishop("b", (0, 5), piece_size)
    board[0, 6] = Knight("b", (0, 6), piece_size)
    board[0, 1] = Knight("b", (0, 1), piece_size)
    board[1, 1] = Pawn("b", (1, 1), piece_size)
    board[1, 2] = Pawn("b", (1, 2), piece_size)
    board[1, 3] = Pawn("b", (1, 3), piece_size)
    board[1, 4] = Pawn("b", (1, 4), piece_size)
    board[1, 5] = Pawn("b", (1, 5), piece_size)
    board[1, 6] = Pawn("b", (1, 6), piece_size)
    board[1, 7] = Pawn("b", (1, 7), piece_size)
    board[1, 0] = Pawn("b", (1, 0), piece_size)
    # board = np.array([-50,-30,-31,-90,-10000,-31,-30,-50],
    #                  [-10,-10,-10,-10,-10,-10,-10,-10],
    #                  [0,0,0,0,0,0,0,0],
    #                  [0,0,0,0,0,0,0,0],
    #                  [0,0,0,0,0,0,0,0],
    #                  [0,0,0,0,0,0,0,0],
    #                  [10,10,10,10,10,10,10,10],
    #                  [50,30,31,90,10000,31,30,50])
