from random import randrange

def write_to_points_file(filename, num_points):
  points_file = open(filename, 'w')
  points_file.write(f"{num_points}\n")

  for i in range(num_points):
    points_file.write(f"{randrange(10000)} {randrange(10000)}\n")
  points_file.close()

write_to_points_file('input7.txt', 100)