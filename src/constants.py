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

INITIAL_PIECE_POS = {"White01": (22.5, 22.5), "White02": (112.5, 22.5), "White03": (202.5, 22.5), "White04": (292.5, 22.5),
                     "White05": (67.5, 67.5), "White06": (157.5, 67.5), "White07": (247.5, 67.5), "White08": (337.5, 67.5),
                     "White09": (22.5, 112.5), "White10": (112.5, 112.5), "White11": (202.5, 112.5), "White12": (292.5, 112.5),
                     "Black01": (337.5, 337.5), "Black02": (247.5, 337.5), "Black03": (157.5, 337.5), "Black04": (67.5, 337.5),
                     "Black05": (292.5, 292.5), "Black06": (202.5, 292.5), "Black07": (112.5, 292.5), "Black08": (22.5, 292.5),
                     "Black09": (337.5, 247.5), "Black10": (247.5, 247.5), "Black11": (157.5, 247.5), "Black12": (67.5, 247.5)}
