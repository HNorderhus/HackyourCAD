import FreeCADGui as Gui
import FreeCAD as App

from constants import INITIAL_PIECE_POS, SQUARE_SIZE, FIELD_LABELS, ROWS, COLS, GAME_LEVELS
from game import Game
from minimax import minimax


class Play:
    def __init__(self):
        self.view = Gui.ActiveDocument.ActiveView
        self.callback = self.view.addEventCallback("SoKeyboardEvent", self.detect_selection)
        self.reset_board()
        self.game = Game()
        self.ai_mode = self.game_mode()
        if self.ai_mode:
            self.depth = self.game_difficulty()
        print("Game started!!")
        print("Press 's' to select a piece and 'ESC' to end the game")

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

            if self.game.turn == 'Black' and self.ai_mode and self.game.winner() is None:
                _, new_board = minimax(self.game.get_ai_board(), self.depth, True)
                piece, move, jumped = self.get_ai_move(new_board=new_board)
                self.game.ai_move(piece, move, jumped)

            if self.game.winner() is not None:
                # TODO: Display winner (with 3D object)
                print(f"The winner is: {self.game.winner()}")
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
                    if piece.king:
                        if piece.crown_object.Label == label:
                            row = piece.row
                            col = piece.col
                    else:
                        if piece.piece_object.Label == label:
                            row = piece.row
                            col = piece.col
        return row, col

    def reset_board(self):
        """Reset the board to the initial state"""
        for label in FIELD_LABELS:
            field = App.ActiveDocument.getObjectsByLabel(label)[0]
            field.ViewObject.ShapeColor = FIELD_LABELS[label]

        for label in INITIAL_PIECE_POS:
            piece = App.ActiveDocument.getObjectsByLabel(label[0])[0]
            piece.Placement.Base.x = INITIAL_PIECE_POS[label][0]
            piece.Placement.Base.y = INITIAL_PIECE_POS[label][1]
            piece.ViewObject.Visibility = True

            crown = App.ActiveDocument.getObjectsByLabel(label[1])[0]
            crown.Placement.Base.x = INITIAL_PIECE_POS[label][0]
            crown.Placement.Base.y = INITIAL_PIECE_POS[label][1]
            crown.ViewObject.Visibility = False

    def get_ai_move(self, new_board):
        jumped = []
        piece = None
        move = None
        for row in range(ROWS):
            for col in range(COLS):
                curr_piece = self.game.board.get_piece(row, col)
                new_piece = new_board.get_piece(row, col)
                if curr_piece != 0 and new_piece == 0:
                    if curr_piece.color == "Black":
                        piece = curr_piece
                    else:
                        jumped.append(curr_piece)
                elif curr_piece == 0 and new_piece != 0:
                    if new_piece.color == "Black":
                        move = (row, col)

        return piece, move, jumped

    def game_mode(self):
        print("Choose a game mode: (1) Human vs Human, (2) Human vs AI")
        choice = int(input("Please enter a number:\n"))
        if choice in [1, 2]:
            if choice == 1:
                return False
            else:
                return True
        else:
            print("Invalid choice. Please try again.")
            self.game_mode()

    def game_difficulty(self):
        print("Choose a game difficulty: Beginner, Amateur, Professional, Expert")
        choice = input("Please enter a difficulty level:\n").lower()
        if choice in GAME_LEVELS:
            return GAME_LEVELS[choice]
        else:
            print("Invalid choice. Please try again.")
            self.game_difficulty()


if __name__ == "__main__":
    play = Play()
