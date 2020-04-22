# Percolation
here's my solution, in python for the [percolation programming assignment](https://coursera.cs.princeton.edu/algs4/assignments/percolation/specification.php)

I'm modeling [percolation](https://en.wikipedia.org/wiki/Percolation) here using an _n_ by _n_ grid. The grid percolates if there is a path from the top to the bottom through open nodes.

The goal of this assignment is to determine the value _p_, which represents the ratio of open nodes to total nodes in the system where we can expect the system to percolate.

## How to run it yourself
There are two programs here that you can use: a visualizer and a stats program

### Visualizer
The visualizer will generate a 6x6 grid and randomly "open" nodes until the system percolates. It prints every step of this process to the console


