import FreeCADGui as Gui
import FreeCAD as App

from constants import INITIAL_PIECE_POS, SQUARE_SIZE, FIELD_LABELS
from game import Game


class Play:
    def __init__(self):
        self.view = Gui.ActiveDocument.ActiveView
        self.callback = self.view.addEventCallback("SoKeyboardEvent", self.detect_selection)
        self.reset_pieces()
        self.game = Game()
        print("Game started!!")

    def detect_selection(self, info):
        select_key = (info["Key"] == "s")
        escape_key = (info["Key"] == "ESCAPE")
        down = (info["State"] == "DOWN")
        if select_key and down:
            selection = Gui.Selection.getSelection()
            if len(selection) == 1:
                obj = selection[0]
                if obj.Label in FIELD_LABELS:
                    row, col = self.get_row_col_of_field(x=obj.Placement.Base.x, y=obj.Placement.Base.y)
                else:
                    row, col = self.get_row_col_of_fc_obj(label=obj.Label)

                self.game.select(row, col)

            if self.game.winner() is not None:
                # TODO: Display winner (with 3D object)
                print(self.game.winner())
                self.remove()

        if escape_key and down:
            self.remove()
            print("Game ended!!")

    def remove(self):
        self.view.removeEventCallback("SoKeyboardEvent", self.callback)

    def get_row_col_of_field(self, x, y):
        row = int(y // SQUARE_SIZE)
        col = int(x // SQUARE_SIZE)
        return row, col

    def get_row_col_of_fc_obj(self, label):
        for r in self.game.board.board:
            for piece in r:
                if piece != 0:
                    if piece.freecad_object.Label == label:
                        row = piece.row
                        col = piece.col
        return row, col

    def reset_pieces(self):
        """Reset the piece positions to the initial positions and make all pieces visible"""
        for label in INITIAL_PIECE_POS:
            piece = App.ActiveDocument.getObjectsByLabel(label)[0]
            piece.Placement.Base.x = INITIAL_PIECE_POS[label][0]
            piece.Placement.Base.y = INITIAL_PIECE_POS[label][1]
            piece.ViewObject.Visibility = True


if __name__ == "__main__":
    play = Play()
