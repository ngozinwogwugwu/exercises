import unittest
from board import Board, BoardPosition
from solver import BoardNode, Solver
from heapq import heappush, heappop

class TestSolver(unittest.TestCase):
  @classmethod
  def setUp(cls):
    cls.goal_board = Board([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0],
    ])

    cls.easy_board = Board([
        [1, 2, 3],
        [4, 5, 6],
        [7, 0, 8],
    ])

  def test_init(self):
    solver = Solver(self.easy_board)
    self.assertEqual(solver.puzzle_heap, [])
    self.assertEqual(solver.initial_board.tiles, self.easy_board.tiles)

  def test_add_board_neighbors_to_priority_queue(self):
    solver = Solver(self.easy_board)
    board_node = BoardNode(self.easy_board.manhattan, self.easy_board, None)

    solver.add_board_neighbors_to_priority_queue(board_node, 1)
    exptected_goal_board = heappop(solver.puzzle_heap)
    self.assertEqual(exptected_goal_board.board.tiles, self.goal_board.tiles)

  def test_move(self):
    solver = Solver(self.easy_board)
    final_board_node = solver.move(
        parent_board_node=BoardNode(
            priority=solver.initial_board.manhattan,
            board=solver.initial_board,
            parent=None
        ),
        num_moves=0
    )

    self.assertEqual(final_board_node.board.tiles, self.goal_board.tiles)
    self.assertEqual(final_board_node.priority, 1)
    self.assertEqual(final_board_node.parent.board.tiles, self.easy_board.tiles)
    self.assertIsNone(final_board_node.parent.parent)


  def test_get_final_board_node(self):
    solver = Solver(self.easy_board)
    final_board_node = solver.get_final_board_node()

    self.assertEqual(final_board_node.board.tiles, self.goal_board.tiles)
    self.assertEqual(final_board_node.priority, 1)
    self.assertEqual(final_board_node.parent.board.tiles, self.easy_board.tiles)
    self.assertIsNone(final_board_node.parent.parent)

  def test_solution_easy(self):
    solver = Solver(self.easy_board)
    solution_boards = solver.solution()

    self.assertEqual(solution_boards[0].tiles, self.easy_board.tiles)
    self.assertEqual(solution_boards[1].tiles, self.goal_board.tiles)

  def test_moves_easy(self):
    solver = Solver(self.easy_board)
    self.assertEqual(solver.moves(), 1)

  def test_solution_medium(self):
    board = Board([
      [0, 1, 3],
      [4, 2, 5],
      [7, 8, 6],
    ])
    solver = Solver(board)
    self.assertEqual(solver.moves(), 4)

    solution_boards = solver.solution()
    self.assertEqual(
      solution_boards[0].tiles,
      [
        [0, 1, 3],
        [4, 2, 5],
        [7, 8, 6],
      ]
    )

    self.assertEqual(
      solution_boards[1].tiles,
      [
        [1, 0, 3],
        [4, 2, 5],
        [7, 8, 6],
      ]
    )
    self.assertEqual(
      solution_boards[2].tiles,
      [
        [1, 2, 3],
        [4, 0, 5],
        [7, 8, 6],
      ]
    )
    self.assertEqual(
      solution_boards[3].tiles,
      [
        [1, 2, 3],
        [4, 5, 0],
        [7, 8, 6],
      ]
    )

    self.assertEqual(
      solution_boards[4].tiles,
      [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0],
      ]
    )

  # def test_solution_fifteen(self):
  #   board = Board([
  #     [15, 2, 1, 12],
  #     [8, 5, 6, 11],
  #     [4, 9, 10, 7],
  #     [3, 14, 13, 0],
  #   ])
  #   solver = Solver(board)
  #   # self.assertEqual(solver.moves(), 4)

  #   solution_boards = solver.solution()
  #   print(solution_boards)




if __name__ == "__main__":
  unittest.main()

