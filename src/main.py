import FreeCADGui as Gui

from checker.constants import SQUARE_SIZE, WIDTH, HEIGHT
from checker.game import Game


class Play:
    def __init__(self):
        self.view = Gui.ActiveDocument.ActiveView
        self.callback = self.view.addEventCallback("SoMouseButtonEvent", self.detect_mouse_click)
        self.game = Game()
        self.pos = None

    def detect_mouse_click(self, info):
        left = (info["Button"] == "BUTTON1")
        down = (info["State"] == "DOWN")
        pos = info["Position"]
        if left and down:
            self.pos = pos
            row, col = self.get_row_col_from_mouse()
            self.game.select(row, col)

            if self.game.winner() is not None:
                # TODO: Display winner (with 3D object)
                print(self.game.winner())
                self.remove()

    def remove(self):
        self.view.removeEventCallback("SoMouseButtonEvent", self.callback)

    def get_row_col_from_mouse(self):
        x, y = self.pos
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row, col


play = Play()
