# Collinear Points
The goal of this [programming assignment](https://coursera.cs.princeton.edu/algs4/assignments/collinear/specification.php) is to recognize when points form lines, specifically four or more points in a row

The brute force way to do this is to check each combination of four points, which is not performant. It's possible to use sorting to make a more performant version of this.

## How to run it yourself
```
python client.py
```
should display two graphs. The first one shows all points given in `input8.txt`, and the second shows the lines formed by them

![dots](https://github.com/ngozinwogwugwu/exercises/blob/master/data_structures_homeworks/collinear_points/dots.png)
![lines](https://github.com/ngozinwogwugwu/exercises/blob/master/data_structures_homeworks/collinear_points/lines.png)

## The files here
unit tests and collinear points
```
collinear_points.py
test_collinear_points.py
```

client files
```
client.py
input7.txt
input8.txt
make_points_file.py
```

some geometry
```
line_segment.py
point.py
```

