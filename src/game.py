import FreeCAD as App

from board import Board
from constants import ROWS, ROW_NAMES, COLS, COL_NAMES, HIGHLIGHT_FIELD_COLOR, BLACK_FIELD_COLOR, WHITE_FIELD_COLOR
from piece import Piece


class Game:
    def __init__(self):
        self.selected = None
        self.board = Board()
        self.turn = 'White'
        self.valid_moves = {}

    def select(self, row, col):
        """Select a piece and try to move it to a selected field"""
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.change_to_default_color(self.valid_moves)
                self.select(row, col)
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            self.highlight_valid_moves(self.valid_moves)
            return True
        return False

    def winner(self):
        """Return the winner of the game if there is one"""
        return self.board.winner()

    def highlight_valid_moves(self, moves):
        """Change field color to indicate valid moves for selected piece"""
        for move in moves:
            row, col = move
            field = App.ActiveDocument.getObjectsByLabel(ROW_NAMES[row] + COL_NAMES[col])[0]
            field.ViewObject.ShapeColor = HIGHLIGHT_FIELD_COLOR

    def change_to_default_color(self, moves):
        """Change field color back to default"""
        for move in moves:
            row, col = move
            field = App.ActiveDocument.getObjectsByLabel(ROW_NAMES[row] + COL_NAMES[col])[0]
            if (row + col) % 2 == 0:
                field.ViewObject.ShapeColor = BLACK_FIELD_COLOR
            else:
                field.ViewObject.ShapeColor = WHITE_FIELD_COLOR

    def change_turn(self):
        """Change the turn from white to black or vice versa"""
        self.valid_moves = {}
        if self.turn == 'White':
            self.turn = 'Black'
        else:
            self.turn = 'White'

    def get_ai_board(self):
        """Return the board"""
        ai_board = Board(create_board=False)
        board = []
        for row in range(ROWS):
            board.append([])
            for col in range(COLS):
                piece = self.board.get_piece(row, col)
                if piece == 0:
                    board[row].append(0)
                else:
                    p = Piece(piece.row, piece.col, piece.color)
                    p.x = piece.x
                    p.y = piece.y
                    p.king = piece.king
                    board[row].append(p)
        ai_board.board = board
        return ai_board

    def ai_move(self, piece, move, jumped):
        """Make a move for the AI"""
        self.board.move(piece, move[0], move[1], False)
        self.board.remove(jumped, False)
        self.change_turn()

    def _move(self, row, col):
        """Move the selected piece to the given row and col if the move is valid and remove jumped pieces"""
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col, False)
            jumped = self.valid_moves[(row, col)]
            if jumped:
                self.board.remove(jumped, False)
            self.change_to_default_color(self.valid_moves)
            self.change_turn()
        else:
            return False
        return True
