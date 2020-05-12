# https://leetcode.com/problems/3sum/
from typing import List
import unittest

class Solution:
    def isBoardArrayValid(self, array: List[int]) -> bool:
        numbers = list(filter(lambda x: x is not None, array))
        return len(numbers) == len(list(set(numbers)))


    def areBoardRowsValid(self, board: List[List[int]]) -> bool:
        for row in board:
            if not self.isBoardArrayValid(row):
                return False
        return True


    def areBoardColsValid(self, board: List[List[int]]) -> bool:
        for idx in range(len(board[0])):
            column = [row[idx] for row in board]
            if not self.isBoardArrayValid(column):
                return False
        return True


    def are3x3SquaresValid(self, board: List[List[int]]) -> bool:
        for row_idx in range(0, 9, 3):
            rows = board[row_idx:row_idx+3]
            for col_idx in range(0, 9, 3):
                three_by_three = []
                for row in rows:
                    three_by_three += row[col_idx:col_idx+3]
                if not self.isBoardArrayValid(three_by_three):
                    return False
        return True


    def strArraytoIntArray(self, str_array: List[str]) -> List[int]:
        int_array = []
        for string in str_array:
            if string == ".":
                int_array.append(None)
            else:
                int_array.append(int(string))
        return int_array


    def isValidSudoku(self, str_board: List[List[str]]) -> bool:
        board = []

        for str_array in str_board:
            board.append(self.strArraytoIntArray(str_array))

        if not self.areBoardRowsValid(board):
            return False
        if not self.areBoardColsValid(board):
            return False
        if not self.are3x3SquaresValid(board):
            return False
        return True


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_example_case(self):
        example = [
          ["5","3",".",  ".","7",".",  ".",".","."],
          ["6",".",".",  "1","9","5",  ".",".","."],
          [".","9","8",  ".",".",".",  ".","6","."],

          ["8",".",".",  ".","6",".",  ".",".","3"],
          ["4",".",".",  "8",".","3",  ".",".","1"],
          ["7",".",".",  ".","2",".",  ".",".","6"],

          [".","6",".",  ".",".",".",  "2","8","."],
          [".",".",".",  "4","1","9",  ".",".","5"],
          [".",".",".",  ".","8",".",  ".","7","9"]
        ]
        self.assertEqual(self.solution.isValidSudoku(example), True)


    def test_edge_case(self):
        example = [
          ["8","3",".",  ".","7",".",  ".",".","."],
          ["6",".",".",  "1","9","5",  ".",".","."],
          [".","9","8",  ".",".",".",  ".","6","."],

          ["8",".",".",  ".","6",".",  ".",".","3"],
          ["4",".",".",  "8",".","3",  ".",".","1"],
          ["7",".",".",  ".","2",".",  ".",".","6"],

          [".","6",".",  ".",".",".",  "2","8","."],
          [".",".",".",  "4","1","9",  ".",".","5"],
          [".",".",".",  ".","8",".",  ".","7","9"]
        ]
        self.assertEqual(self.solution.isValidSudoku(example), False)


if __name__ == '__main__':
    unittest.main()
