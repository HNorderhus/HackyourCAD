from constants import ROWS, ROW_NAMES, COLS, COL_NAMES, INITIAL_BOARD
from piece import Piece


class Board:
    def __init__(self, create_board=True):
        self.board = []
        self.black_left = self.white_left = 12
        self.black_kings = self.white_kings = 0
        if create_board:
            self.create_board()

    def create_board(self):
        """Create a 2D list of the board with 0 as empty fields and Piece objects as occupied fields"""
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                field = ROW_NAMES[row] + COL_NAMES[col]

                if field in INITIAL_BOARD:
                    piece_label = INITIAL_BOARD[field][0]
                    king_label = INITIAL_BOARD[field][1]
                    color = piece_label[:-2]
                    self.board[row].append(Piece(row, col, color, piece_label, king_label))
                else:
                    self.board[row].append(0)

    def move(self, piece, row, col, for_ai):
        """Move the piece to a new row and col and change the x and y position"""
        if piece.color == 'Black' and row == 0 and not piece.king:
            self.black_kings += 1
            piece.make_king(for_ai)

        elif piece.color == 'White' and row == (ROWS - 1) and not piece.king:
            self.white_kings += 1
            piece.make_king(for_ai)

        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]

        if for_ai:
            piece.ai_move(row, col)
        else:
            piece.move(row, col)

    def get_piece(self, row, col):
        """Return the piece at the given row and col"""
        return self.board[row][col]

    def remove(self, pieces, for_ai):
        """Make the pieces invisible and remove them from the board (2D list)"""
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if not for_ai:
                if piece.king:
                    piece.crown_object.ViewObject.Visibility = False
                else:
                    piece.piece_object.ViewObject.Visibility = False

            if piece != 0:
                if piece.color == 'Black':
                    self.black_left -= 1
                else:
                    self.white_left -= 1

    def winner(self):
        """Return the winner of the game if there is one"""
        if self.black_left <= 0 or not self.exists_valid_moves('Black'):
            return 'White'
        elif self.white_left <= 0 or not self.exists_valid_moves('White'):
            return 'Black'

        return None

    def evaluate(self):
        """Return the value of the board for the AI"""
        return self.black_left - self.white_left + (self.black_kings * 0.5 - self.white_kings * 0.5)

    def get_all_pieces(self, color):
        """Return a list of all pieces of a given color"""
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    def exists_valid_moves(self, color):
        """Return True if there exists a valid move for the given color"""
        for piece in self.get_all_pieces(color):
            valid_moves = self.get_valid_moves(piece)
            if valid_moves:
                return True
        return False

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
