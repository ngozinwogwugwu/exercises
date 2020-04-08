import unittest
from board import Board, BoardPosition

class TestBoard(unittest.TestCase):
  @classmethod
  def setUp(cls):
    cls.board = Board([
        [1, 2, 3],
        [4, 5, 6],
        [7, 0, 8],
    ])

    tiles_0 = [
      [8, 1, 3],
      [4, 0, 2],
      [7, 6, 5],
    ]
    cls.board_0 = Board(tiles_0)
    cls.duplicate_board_0 = Board(tiles_0)

    cls.board_right = Board([
      [8, 1, 3],
      [4, 2, 0],
      [7, 6, 5],
    ])

    cls.board_left = Board([
      [8, 1, 3],
      [0, 4, 2],
      [7, 6, 5],
    ])

    cls.board_up = Board([
      [8, 0, 3],
      [4, 1, 2],
      [7, 6, 5],
    ])

    cls.board_down = Board([
      [8, 1, 3],
      [4, 6, 2],
      [7, 0, 5],
    ])

    cls.goal_board = Board([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0],
    ])

  def test_repr(self):
    expected = "3\n[1, 2, 3]\n[4, 5, 6]\n[7, 0, 8]\n"
    actual = self.board.__repr__()
    self.assertEqual(expected, actual)

  def test_goal(self):
    expected = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    self.assertEqual(expected, self.board.goal)

  def test_hamming(self):
    self.assertEqual(self.board.hamming, 1)
    self.assertEqual(self.board_0.hamming, 5)

  def test_manhattan(self):
    self.assertEqual(self.board.manhattan, 1)
    self.assertEqual(self.board_0.manhattan, 10)

  def test_is_goal(self):
    self.assertFalse(self.board.is_goal())
    self.assertFalse(self.board_0.is_goal())
    self.assertTrue(self.goal_board.is_goal())

  def test_equals(self):
    self.assertFalse(self.board_0.equals(self.board))
    self.assertFalse(self.goal_board.equals(self.board))
    self.assertTrue(self.board_0.equals(self.duplicate_board_0))

  def test_get_empty_position(self):
    self.assertEqual(self.board.empty_position, BoardPosition(2, 1))
    self.assertEqual(self.board_0.empty_position, BoardPosition(1, 1))
    self.assertEqual(self.goal_board.empty_position, BoardPosition(2, 2))

  def test_adjascent_positions(self):
    self.assertSetEqual(
      self.goal_board.adjascent_positions(),
      set([BoardPosition(1, 2), BoardPosition(2, 1)])
    )

    self.assertSetEqual(
      self.board.adjascent_positions(),
      set(
        [
          BoardPosition(1, 1),
          BoardPosition(2, 0),
          BoardPosition(2, 2)
        ]
      )
    )

    self.assertEqual(
      self.board_0.adjascent_positions(),
      set(
        [
          BoardPosition(0, 1), 
          BoardPosition(2, 1), 
          BoardPosition(1, 0), 
          BoardPosition(1, 2), 
        ]
      )
    )

  def test_neighbor(self):
    adjascent_position = BoardPosition(1, 2)
    empty_position = BoardPosition(1, 1)
    self.assertEqual(
      self.board_0.neighbor(adjascent_position).tiles,
      self.board_right.tiles
    )

  def test_neighbors(self):
    self.assertListEqual(
        [neighbor.tiles for neighbor in self.board_0.neighbors()],
        [
          self.board_up.tiles,
          self.board_left.tiles,
          self.board_right.tiles,
          self.board_down.tiles,
        ]
      )


if __name__ == "__main__":
  unittest.main()
