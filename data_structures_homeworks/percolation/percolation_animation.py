from percolation import *
from random import randint

m = 6
perc = Percolation(m)

while not perc.percolates():
  print(perc)
  perc.open(randint(0, m - 1), randint(0, m - 1))

print('-------------------------------')
print ('it percolates!!')
print(perc)

