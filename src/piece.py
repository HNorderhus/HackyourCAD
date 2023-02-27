import FreeCAD as App

from constants import SQUARE_SIZE, COORDINATE_OFFSET_WHITE, COORDINATE_OFFSET_BLACK


class Piece:
    def __init__(self, row, col, color, piece_label=None, crown_label=None):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        if piece_label is None and crown_label is None:
            self.piece_object = None
            self.crown_object = None
        else:
            self.piece_object = App.ActiveDocument.getObjectsByLabel(piece_label)[0]
            self.crown_object = App.ActiveDocument.getObjectsByLabel(crown_label)[0]
            self.get_pos()

    def get_pos(self):
        """Get the x and y position of the freeCAD piece"""
        self.x = self.piece_object.Placement.Base.x
        self.y = self.piece_object.Placement.Base.y

    def update_pos(self, row, col):
        """Update the row and col of the piece and the x and y position"""
        self.row = row
        self.col = col
        if self.color == 'Black':
            self.x = (col * SQUARE_SIZE + SQUARE_SIZE / 2) - COORDINATE_OFFSET_BLACK[0]
            self.y = (row * SQUARE_SIZE + SQUARE_SIZE / 2) - COORDINATE_OFFSET_BLACK[1]
        elif self.color == 'White':
            self.x = (col * SQUARE_SIZE + SQUARE_SIZE / 2) - COORDINATE_OFFSET_WHITE[0]
            self.y = (row * SQUARE_SIZE + SQUARE_SIZE / 2) - COORDINATE_OFFSET_WHITE[1]

    def make_king(self, for_ai):
        """Change the piece to a king"""
        self.king = True
        if not for_ai:
            self.crown_object.ViewObject.Visibility = True
            self.piece_object.ViewObject.Visibility = False

    def move(self, row, col):
        """Move the piece to a new row and col and change the x and y position"""
        self.update_pos(row, col)
        self.piece_object.Placement.Base.x = self.x
        self.piece_object.Placement.Base.y = self.y
        self.crown_object.Placement.Base.x = self.x
        self.crown_object.Placement.Base.y = self.y

    def ai_move(self, row, col):
        """Move the piece to a new row and col"""
        self.update_pos(row, col)

