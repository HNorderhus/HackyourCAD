import FreeCAD as App

from board import Board
from constants import ROW_NAMES, COL_NAMES, HIGHLIGHT_FIELD_COLOR, BLACK_FIELD_COLOR, WHITE_FIELD_COLOR


class Game:
    def __init__(self):
        self.selected = None
        self.board = Board()
        self.turn = 'White'
        self.valid_moves = {}

    def reset(self):
        """Reset the game by resetting the board and piece positions"""
        self.selected = None
        self.board = Board()
        self.turn = 'White'
        self.valid_moves = {}

    def update(self):
        """Maby not needed"""
        pass

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

    def _move(self, row, col):
        """Move the selected piece to the given row and col if the move is valid and remove jumped pieces"""
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            jumped = self.valid_moves[(row, col)]
            if jumped:
                self.board.remove(jumped)
            self.change_to_default_color(self.valid_moves)
            self.change_turn()
        else:
            return False
        return True
