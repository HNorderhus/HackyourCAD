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

FIELD_LABELS = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8",
                "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8",
                "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8",
                "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8"]

INITIAL_BOARD = {"A1": "White001", "A3": "White002", "A5": "White003", "A7": "White004",
                 "B2": "White005", "B4": "White006", "B6": "White007", "B8": "White008",
                 "C1": "White009", "C3": "White010", "C5": "White011", "C7": "White012",
                 "F2": "Black012", "F4": "Black011", "F6": "Black010", "F8": "Black009",
                 "G1": "Black008", "G3": "Black007", "G5": "Black006", "G7": "Black005",
                 "H2": "Black004", "H4": "Black003", "H6": "Black002", "H8": "Black001"}

INITIAL_PIECE_POS = {"White001": (0.0, 0.0), "White002": (90.0, 0.0), "White003": (180.0, 0.0), "White004": (270.0, 0.0),
                     "White005": (45.0, 45.0), "White006": (135.0, 45), "White007": (225.0, 45.0), "White008": (315.0, 45.0),
                     "White009": (0.0, 90.0), "White010": (90.0, 90.0), "White011": (180.0, 90.0), "White012": (270.0, 90.0),
                     "Black001": (0.0, 0.0), "Black002": (-90.0, 0.0), "Black003": (-180.0, 0.0), "Black004": (-270.0, 0.0),
                     "Black005": (-45.0, -45.0), "Black006": (-135.0, -45.0), "Black007": (-225.0, -45.0), "Black008": (-315.0, -45.0),
                     "Black009": (0.0, -90.0), "Black010": (-90.0, -90.0), "Black011": (-180.0, -90.0), "Black012": (-270.0, -90.0)}

COORDINATE_OFFSET_WHITE = (22.5, 22.5)
COORDINATE_OFFSET_BLACK = (337.5, 337.5)
