WIDTH = 360
HEIGHT = 360
SQUARE_SIZE = 45

ROWS = 8
ROW_NAMES = ["A", "B", "C", "D", "E", "F", "G", "H"]

COL_NAMES = ["1", "2", "3", "4", "5", "6", "7", "8"]
COLS = 8

BLACK_FIELD_COLOR = (112.0 / 255.0, 128.0 / 255.0, 144.0 / 255.0)
WHITE_FIELD_COLOR = (1.0, 1.0, 1.0)
HIGHLIGHT_FIELD_COLOR = (85.0 / 255.0, 255.0 / 255.0, 127.0 / 255.0)

INITIAL_BOARD = {"A1": "White01", "A3": "White02", "A5": "White03", "A7": "White04",
                 "B2": "White05", "B4": "White06", "B6": "White07", "B8": "White08",
                 "C1": "White09", "C3": "White10", "C5": "White11", "C7": "White12",
                 "F2": "Black12", "F4": "Black11", "F6": "Black10", "F8": "Black09",
                 "G1": "Black08", "G3": "Black07", "G5": "Black06", "G7": "Black05",
                 "H2": "Black04", "H4": "Black03", "H6": "Black02", "H8": "Black01"}

# TODO: Change the initial positions (x and y values)of the pieces to the correct positions
INITIAL_PIECE_POS = {"White01": (0, 0), "White02": (0, 2), "White03": (0, 4), "White04": (0, 6),
                     "White05": (1, 1), "White06": (1, 3), "White07": (1, 5), "White08": (1, 7),
                     "White09": (2, 0), "White10": (2, 2), "White11": (2, 4), "White12": (2, 6),
                     "Black01": (7, 1), "Black02": (7, 3), "Black03": (7, 5), "Black04": (7, 7),
                     "Black05": (6, 0), "Black06": (6, 2), "Black07": (6, 4), "Black08": (6, 6),
                     "Black09": (5, 1), "Black10": (5, 3), "Black11": (5, 5), "Black12": (5, 7)}
