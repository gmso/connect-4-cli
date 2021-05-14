from enum import Enum

class CellState(Enum):
    EMPTY = 0
    RED = 1
    YELLOW = 2

class Cell():
    current_state = CellState.EMPTY