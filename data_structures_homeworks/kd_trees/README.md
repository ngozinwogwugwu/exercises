# Kd-Trees
my homework solution for the [kd-trees programming assignment](https://coursera.cs.princeton.edu/algs4/assignments/kdtree/specification.php)

[Kd-Trees](https://en.wikipedia.org/wiki/K-d_tree) are a space partitioning data structure. I'm using it here to efficiently find points in the range of a rectangle

## How to run it yourself
```bash
python client.py
```

here's what should pop up (not exactly, though. The client generates a new set of points and a new rectangle every time you run it):
![Image of dots](https://github.com/ngozinwogwugwu/exercises/blob/master/data_structures_homeworks/kd_trees/Screen%20Shot%202020-04-21%20at%206.57.37%20PM.png)

- the black dots represent all the points in the data set
- the rectangle is outlined in black
- the red dots represent the points within the rectangle
- the blue lines represent horizontal partitions
- the red lines represent vertical partitions

## The files here
geometry files:
```
line_segment.py
point_2d.py
rectangle.py
```

data structures files
```
kd_tree.py
point_set.py
```

unit test files
```
test_geometry.py
test_kd_tree.py
```

manual test files
```
input7.txt
client.py
show.py
```
