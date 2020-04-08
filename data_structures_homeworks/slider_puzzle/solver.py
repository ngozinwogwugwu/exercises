from board import Board, BoardPosition
from collections import namedtuple
from heapq import heappush, heappop


BoardNode = namedtuple('BoardNode', ['priority', 'board', 'parent'])


class Solver:
  final_board_node = None

  def __init__(self, initial_board):
    self.initial_board = initial_board
    self.puzzle_heap = []

  def is_solvable(self):
    # todo: determine whether a given board is solvable
    pass

  def moves(self):
    final_board_node = self.get_final_board_node()
    return final_board_node.priority - final_board_node.board.manhattan

  def move(self, parent_board_node, num_moves):
    num_moves += 1
    if parent_board_node.board.is_goal():
      return parent_board_node

    self.add_board_neighbors_to_priority_queue(parent_board_node, num_moves)

    return self.move(
        parent_board_node=heappop(self.puzzle_heap),
        num_moves=num_moves
    )

  def add_board_neighbors_to_priority_queue(self, parent_board_node, num_moves):
    child_boards = parent_board_node.board.neighbors()
    for child_board in child_boards:
      if parent_board_node.parent is None or parent_board_node.parent.board.tiles != child_board.tiles:
        heappush(
            self.puzzle_heap,
            BoardNode(
                priority=child_board.manhattan + num_moves,
                board=child_board,
                parent=parent_board_node
            )
        )

  def solution(self):
    final_board_node = self.get_final_board_node()
    return self.get_board_path(final_board_node)


  def get_board_path(self, final_board_node):
    board_node = final_board_node
    solution_boards = []
    while board_node is not None:
      solution_boards.append(board_node.board)
      board_node = board_node.parent
    
    solution_boards.reverse()
    return solution_boards

  def get_final_board_node(self):
    root_board_node = BoardNode(
        priority=self.initial_board.manhattan,
        board=self.initial_board,
        parent=None
    )
    heappush(self.puzzle_heap, root_board_node)
    return self.move(
        parent_board_node=root_board_node,
        num_moves=0
    )
