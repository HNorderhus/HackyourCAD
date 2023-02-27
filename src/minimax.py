from copy import deepcopy


def minimax(board, depth, is_maximizing):
    """Return the best move for the AI player"""
    if depth == 0 or board.winner() is not None:
        return board.evaluate(), board

    if is_maximizing:
        max_eval = float('-inf')
        best_board = None
        for move in get_all_moves(board=board, color='Black'):
            evaluation = minimax(move, depth - 1, False)[0]
            max_eval = max(max_eval, evaluation)
            if max_eval == evaluation:
                best_board = move
        return max_eval, best_board

    else:
        min_eval = float('inf')
        best_board = None
        for move in get_all_moves(board=board, color='White'):
            evaluation = minimax(move, depth - 1, True)[0]
            min_eval = min(min_eval, evaluation)
            if min_eval == evaluation:
                best_board = move
        return min_eval, best_board


def get_all_moves(board, color):
    """Return a list of all valid moves for a piece with the key being the row and col of the move and the value
    being the new board after the move and the piece that is jumped."""
    moves = []
    for piece in board.get_all_pieces(color=color):
        valid_moves = board.get_valid_moves(piece)
        for move, jumped in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_moves(temp_piece, move, temp_board, jumped)
            moves.append(new_board)
    return moves


def simulate_moves(piece, move, board, jumped):
    """Simulate the move on a temporary board and return the new board"""
    board.move(piece, move[0], move[1], True)
    if jumped:
        board.remove(jumped, True)
    return board

