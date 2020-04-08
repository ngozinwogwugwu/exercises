from collections import namedtuple
import copy

BoardPosition = namedtuple('BoardPosition', ['row', 'col'])

class Board:
  tiles = []
  dimention = 0
  goal = []
  empty_position = None
  hamming = 0
  manhattan = 0

  def __init__(self, tiles):
    self.tiles = tiles
    self.dimention = len(self.tiles)
    self.set_goal()
    self.set_empty_position()
    self.set_hamming_score()
    self.set_manhattan_score()

  def __repr__(self):
    tiles_string = f"{str(self.dimention)}\n"
    for row in self.tiles:
      tiles_string += str(row) + "\n"
    return tiles_string

  def __lt__(self, other_board):
    if self.hamming < other_board.hamming:
      return True
    return False

  def set_empty_position(self):
    for row in range(0, self.dimention):
      for col in range(0, self.dimention):
        if self.tiles[row][col] == 0:
          self.empty_position = BoardPosition(row, col)
          return
    raise Exception('this board has no empty slots')

  def set_goal(self):
    current_num = 1
    goal_tiles = []

    for row in self.tiles:
      goal_row = []
      for tile in row:
        goal_row.append(current_num)
        current_num += 1
      goal_tiles.append(goal_row)

    goal_tiles[self.dimention - 1][self.dimention - 1] = 0
    self.goal = goal_tiles

  def set_hamming_score(self):
    hamming_score = 0

    for row in range(0, self.dimention):
      for col in range(0, self.dimention):
        if self.tiles[row][col] is not self.goal[row][col] and self.tiles[row][col] is not 0:
          hamming_score += 1

    self.hamming = hamming_score

  def goal_row(self, value):
    return int((value - 1) / self.dimention)

  def goal_col(self, value):
    return (value - 1) % self.dimention

  def distance(self, slot_idx_a, slot_idx_b):
    return abs(slot_idx_a - slot_idx_b)

  def tile_manhattan_score(self, row, col):
    value = self.tiles[row][col]
    if value is 0:
      return 0
    return self.distance(row, self.goal_row(value)) + self.distance(col, self.goal_col(value))

  def set_manhattan_score(self):
    manhattan_score = 0
    for row in range(0, self.dimention):
      for col in range(0, self.dimention):
        manhattan_score += self.tile_manhattan_score(row, col)
    self.manhattan = manhattan_score

  def is_goal(self):
    return self.tiles == self.goal

  def equals(self, other_board):
    return self.tiles == other_board.tiles

  def neighbors(self):
    neighbor_boards = []
    for adjascent_position in self.adjascent_positions():
      neighbor_boards.append(self.neighbor(adjascent_position))
    return neighbor_boards

  def neighbor(self, adjascent_position):
    new_tiles = copy.deepcopy(self.tiles)
    new_tiles[self.empty_position.row][self.empty_position.col] = self.tiles[adjascent_position.row][adjascent_position.col]
    new_tiles[adjascent_position.row][adjascent_position.col] = 0
    return Board(new_tiles)

  def adjascent_positions(self):
    board_range = range(0, self.dimention)
    adjascent_positions = set()

    # up and down
    if self.empty_position.row + 1 in board_range:
      adjascent_positions.add(BoardPosition(self.empty_position.row + 1, self.empty_position.col))
    if self.empty_position.row - 1 in board_range:
      adjascent_positions.add(BoardPosition(self.empty_position.row - 1, self.empty_position.col))

    # left and right
    if self.empty_position.col + 1 in board_range:
      adjascent_positions.add(BoardPosition(self.empty_position.row, self.empty_position.col + 1))
    if self.empty_position.col - 1 in board_range:
      adjascent_positions.add(BoardPosition(self.empty_position.row, self.empty_position.col - 1))

    return adjascent_positions

  def twin(self):
    # TODO: // a board that is obtained by exchanging any pair of tiles
    pass


