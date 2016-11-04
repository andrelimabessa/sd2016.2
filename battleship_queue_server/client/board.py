from random import randint

from client.exception.invalid_column import InvalidColumnException
from client.exception.invalid_row import InvalidRowException
from client.exception.max_move_exceeded import MaxMoveExceededException
from common.unit import Unit


class Board(object):
    DEFAULT_ROWS = 10
    DEFAULT_COLUMNS = DEFAULT_ROWS
    DEFAULT_MAX_MOVE = 10
    DEFAULT_MOVES = 0
    DEFAULT_BOARD = None

    def __init__(self,
                 rows=DEFAULT_ROWS,
                 cols=DEFAULT_COLUMNS,
                 max_move=DEFAULT_MAX_MOVE,
                 moves=DEFAULT_MOVES,
                 board=DEFAULT_BOARD):
        self.rows = rows
        self.cols = cols
        self.max_move = max_move
        self.moves = moves
        self.board = board if board else self.create(rows=rows, cols=cols)

    @staticmethod
    def create(rows=DEFAULT_ROWS, cols=DEFAULT_COLUMNS):
        board = [[Unit.WATER for x in range(rows)] for y in range(cols)]
        for i in range(int((rows * cols) / 2)):
            board[randint(0, rows - 1)][randint(0, cols - 1)] = Unit.SHIP
        return board

    def initial_state(self):
        return {
            "rows": Board.DEFAULT_ROWS,
            "cols": Board.DEFAULT_COLUMNS,
            "max_move": Board.DEFAULT_MAX_MOVE,
            "moves": Board.DEFAULT_MOVES,
            "board": self.create()
        }

    def state(self):
        return {
            "rows": self.rows,
            "cols": self.cols,
            "max_move": self.max_move,
            "moves": self.moves,
            "board": self.board
        }

    def load_from_state(self, state):
        self.rows = state["rows"]
        self.cols = state["cols"]
        self.max_move = state["max_move"]
        self.moves = state["moves"]
        self.board = state["board"]

    def restart(self):
        self.load_from_state(state=self.initial_state())

    def remaining_moves(self):
        return self.max_move - self.moves

    def move(self, row, col):
        if row - 1 < 0 or row > self.rows:
            raise InvalidRowException(row_value=row)
        elif col - 1 < 0 or col > self.cols:
            raise InvalidColumnException(column_value=col)
        elif self.moves + 1 > self.max_move:
            raise MaxMoveExceededException(move=self.moves + 1)
        else:
            self.moves += 1
            row -= 1
            col -= 1
            value = self.board[row][col]
            if value == Unit.SHIP or value == Unit.SUNK_SHIP:
                self.board[row][col] = Unit.SUNK_SHIP
            else:
                self.board[row][col] = Unit.BOMB
