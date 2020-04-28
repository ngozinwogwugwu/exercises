# Slider Puzzle
the goal of this [programming assignment](https://coursera.cs.princeton.edu/algs4/assignments/8puzzle/specification.php) is to use heaps to solve slider puzzles

the idea is to navigate a heap of possible board states. In order to prevent the algorithm from traversing a path that leads away from the goal, we score each state based on how similar it is to the end goal, and move to the state with the highest score

## Using this
I tested mainly using unit tests, so you'll need to use the python CLI to test it. You should see something like this:

```python
>>> from board import Board, BoardPosition
>>> from solver import BoardNode, Solver
>>> board = Board([[0, 1, 3],[4, 2, 5],[7, 8, 6]])
>>> board
3
[0, 1, 3]
[4, 2, 5]
[7, 8, 6]

>>> solver = Solver(board)
>>> solution_boards = solver.solution()
>>> solution_boards
[3
[0, 1, 3]
[4, 2, 5]
[7, 8, 6]
, 3
[1, 0, 3]
[4, 2, 5]
[7, 8, 6]
, 3
[1, 2, 3]
[4, 0, 5]
[7, 8, 6]
, 3
[1, 2, 3]
[4, 5, 0]
[7, 8, 6]
, 3
[1, 2, 3]
[4, 5, 6]
[7, 8, 0]
]
```
