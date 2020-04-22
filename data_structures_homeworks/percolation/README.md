# Percolation
here's my solution, in python for the [percolation programming assignment](https://coursera.cs.princeton.edu/algs4/assignments/percolation/specification.php)

I'm modeling [percolation](https://en.wikipedia.org/wiki/Percolation) here using an _n_ by _n_ grid. The grid percolates if there is a path from the top to the bottom through open nodes.

The goal of this assignment is to use a Monte Carlo simulation to determine the value _p_, which represents the ratio of open nodes to total nodes in the system where we can expect the system to percolate.

## How to run it yourself
There are two programs here that you can use: a visualizer and a stats program

### Visualizer
The visualizer will generate a 6x6 grid and randomly "open" nodes until the system percolates. It prints every step of this process to the console. To run this, use the command:

```
python percolation_animation.py
```
and you'll see something like this:
![percolation animation](https://github.com/ngozinwogwugwu/exercises/blob/master/data_structures_homeworks/percolation/percolation_animation.png)

### stats program
The stats program displays less, but has more going on under the hood. It performs the same steps as the visualizer by creating grids, opening nodes, stopping when the grids percolate. The difference is that it uese 20x20 grids, and it creates 500 of them. For each grid, it determines the ratio of open sites to total sites, and it prints the mean of these ratios. 

It does this three times. You should see something like this:

![percolation animation](https://github.com/ngozinwogwugwu/exercises/blob/master/data_structures_homeworks/percolation/run_stats.png)

which indicates that p is ~0.953

## The files here
test files
```
test_percolation.py
```

clients
```
run_stats.py
percolation_animation.py
```
calculators
```
percolation_stats.py
percolation.py
```
