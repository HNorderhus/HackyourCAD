GAME_LEVELS = {"beginner": 1, "amateur": 2, "professional": 3, "expert": 4}

SQUARE_SIZE = 45

ROWS = 8
ROW_NAMES = ["A", "B", "C", "D", "E", "F", "G", "H"]

COL_NAMES = ["1", "2", "3", "4", "5", "6", "7", "8"]
COLS = 8

BLACK_FIELD_COLOR = (112.0 / 255.0, 128.0 / 255.0, 144.0 / 255.0)
WHITE_FIELD_COLOR = (1.0, 1.0, 1.0)
HIGHLIGHT_FIELD_COLOR = (85.0 / 255.0, 255.0 / 255.0, 127.0 / 255.0)

FIELD_LABELS = {"A1": BLACK_FIELD_COLOR, "A2": WHITE_FIELD_COLOR, "A3": BLACK_FIELD_COLOR, "A4": WHITE_FIELD_COLOR,
                "A5": BLACK_FIELD_COLOR, "A6": WHITE_FIELD_COLOR, "A7": BLACK_FIELD_COLOR, "A8": WHITE_FIELD_COLOR,
                "B1": WHITE_FIELD_COLOR, "B2": BLACK_FIELD_COLOR, "B3": WHITE_FIELD_COLOR, "B4": BLACK_FIELD_COLOR,
                "B5": WHITE_FIELD_COLOR, "B6": BLACK_FIELD_COLOR, "B7": WHITE_FIELD_COLOR, "B8": BLACK_FIELD_COLOR,
                "C1": BLACK_FIELD_COLOR, "C2": WHITE_FIELD_COLOR, "C3": BLACK_FIELD_COLOR, "C4": WHITE_FIELD_COLOR,
                "C5": BLACK_FIELD_COLOR, "C6": WHITE_FIELD_COLOR, "C7": BLACK_FIELD_COLOR, "C8": WHITE_FIELD_COLOR,
                "D1": WHITE_FIELD_COLOR, "D2": BLACK_FIELD_COLOR, "D3": WHITE_FIELD_COLOR, "D4": BLACK_FIELD_COLOR,
                "D5": WHITE_FIELD_COLOR, "D6": BLACK_FIELD_COLOR, "D7": WHITE_FIELD_COLOR, "D8": BLACK_FIELD_COLOR,
                "E1": BLACK_FIELD_COLOR, "E2": WHITE_FIELD_COLOR, "E3": BLACK_FIELD_COLOR, "E4": WHITE_FIELD_COLOR,
                "E5": BLACK_FIELD_COLOR, "E6": WHITE_FIELD_COLOR, "E7": BLACK_FIELD_COLOR, "E8": WHITE_FIELD_COLOR,
                "F1": WHITE_FIELD_COLOR, "F2": BLACK_FIELD_COLOR, "F3": WHITE_FIELD_COLOR, "F4": BLACK_FIELD_COLOR,
                "F5": WHITE_FIELD_COLOR, "F6": BLACK_FIELD_COLOR, "F7": WHITE_FIELD_COLOR, "F8": BLACK_FIELD_COLOR,
                "G1": BLACK_FIELD_COLOR, "G2": WHITE_FIELD_COLOR, "G3": BLACK_FIELD_COLOR, "G4": WHITE_FIELD_COLOR,
                "G5": BLACK_FIELD_COLOR, "G6": WHITE_FIELD_COLOR, "G7": BLACK_FIELD_COLOR, "G8": WHITE_FIELD_COLOR,
                "H1": WHITE_FIELD_COLOR, "H2": BLACK_FIELD_COLOR, "H3": WHITE_FIELD_COLOR, "H4": BLACK_FIELD_COLOR,
                "H5": WHITE_FIELD_COLOR, "H6": BLACK_FIELD_COLOR, "H7": WHITE_FIELD_COLOR, "H8": BLACK_FIELD_COLOR}

INITIAL_BOARD = {"A1": ("White01", "whiteCrown1"), "A3": ("White02", "whiteCrown2"),
                 "A5": ("White03", "whiteCrown3"), "A7": ("White04", "whiteCrown4"),
                 "B2": ("White05", "whiteCrown5"), "B4": ("White06", "whiteCrown6"),
                 "B6": ("White07", "whiteCrown7"), "B8": ("White08", "whiteCrown8"),
                 "C1": ("White09", "whiteCrown9"), "C3": ("White10", "whiteCrown10"),
                 "C5": ("White11", "whiteCrown11"), "C7": ("White12", "whiteCrown12"),
                 "F2": ("Black12", "blackCrown12"), "F4": ("Black11", "blackCrown11"),
                 "F6": ("Black10", "blackCrown10"), "F8": ("Black09", "blackCrown9"),
                 "G1": ("Black08", "blackCrown8"), "G3": ("Black07", "blackCrown7"),
                 "G5": ("Black06", "blackCrown6"), "G7": ("Black05", "blackCrown5"),
                 "H2": ("Black04", "blackCrown4"), "H4": ("Black03", "blackCrown3"),
                 "H6": ("Black02", "blackCrown2"), "H8": ("Black01", "blackCrown1")}

INITIAL_PIECE_POS = {("White01", "whiteCrown1"): (0.0, 0.0), ("White02", "whiteCrown2"): (90.0, 0.0),
                     ("White03", "whiteCrown3"): (180.0, 0.0), ("White04", "whiteCrown4"): (270.0, 0.0),
                     ("White05", "whiteCrown5"): (45.0, 45.0), ("White06", "whiteCrown6"): (135.0, 45),
                     ("White07", "whiteCrown7"): (225.0, 45.0), ("White08", "whiteCrown8"): (315.0, 45.0),
                     ("White09", "whiteCrown9"): (0.0, 90.0), ("White10", "whiteCrown10"): (90.0, 90.0),
                     ("White11", "whiteCrown11"): (180.0, 90.0), ("White12", "whiteCrown12"): (270.0, 90.0),
                     ("Black01", "blackCrown1"): (0.0, 0.0), ("Black02", "blackCrown2"): (-90.0, 0.0),
                     ("Black03", "blackCrown3"): (-180.0, 0.0), ("Black04", "blackCrown4"): (-270.0, 0.0),
                     ("Black05", "blackCrown5"): (-45.0, -45.0), ("Black06", "blackCrown6"): (-135.0, -45.0),
                     ("Black07", "blackCrown7"): (-225.0, -45.0), ("Black08", "blackCrown8"): (-315.0, -45.0),
                     ("Black09", "blackCrown9"): (0.0, -90.0), ("Black10", "blackCrown10"): (-90.0, -90.0),
                     ("Black11", "blackCrown11"): (-180.0, -90.0), ("Black12", "blackCrown12"): (-270.0, -90.0)}

COORDINATE_OFFSET_WHITE = (22.5, 22.5)
COORDINATE_OFFSET_BLACK = (337.5, 337.5)

