import FreeCAD as App

from constants import ROWS, ROW_NAMES, COLS, COL_NAMES, INITIAL_BOARD, INITIAL_PIECE_POS
from piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.black_left = self.white_left = 12
        self.black_kings = self.white_kings = 0
        self.reset_pieces()
        self.create_board()

    def create_board(self):
        """Create a 2D list of the board with 0 as empty fields and Piece objects as occupied fields"""
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                field = ROW_NAMES[row] + COL_NAMES[col]

                if field in INITIAL_BOARD:
                    label = INITIAL_BOARD[field]
                    color = label[:-2]
                    self.board[row].append(Piece(label, row, col, color))
                else:
                    self.board[row].append(0)

    def reset_pieces(self):
        """Reset the piece positions to the initial positions and make all pieces visible"""
        for label in INITIAL_PIECE_POS:
            piece = App.ActiveDocument.getObjectsByLabel(label)[0]
            piece.Placement.Base.x = INITIAL_PIECE_POS[label][0]
            piece.Placement.Base.y = INITIAL_PIECE_POS[label][1]
            piece.ViewObject.Visibility = True

    def move(self, piece, row, col):
        """Move the piece to a new row and col and change the x and y position"""
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

    def get_piece(self, row, col):
        """Return the piece at the given row and col"""
        return self.board[row][col]

    def remove(self, pieces):
        """Make the pieces invisible and remove them from the board (2D list)"""
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            piece.freecad_object.ViewObject.Visibility = False
            if piece != 0:
                if piece.color == 'Black':
                    self.black_left -= 1
                else:
                    self.white_left -= 1

    def winner(self):
        """Return the winner of the game if there is one"""
        if self.black_left <= 0:
            return 'White'
        elif self.white_left <= 0:
            return 'Black'

        return None

    def get_valid_moves(self, piece):
        """Return a dictionary with all valid moves for a piece with the key being the row and col of the move and the
        value being the piece that is jumped"""
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row
        if piece.color == 'Black' or piece.king:
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))
        if piece.color == 'White' or piece.king:
            moves.update(self._traverse_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))

        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        """Traverse the board in the left direction and return a dictionary of all valid moves"""
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._traverse_left(r + step, row, step, color, left - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, left + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1

        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        """Traverse the board in the right direction and return a dictionary of all valid moves"""
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break

            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._traverse_left(r + step, row, step, color, right - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, right + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1

        return moves
