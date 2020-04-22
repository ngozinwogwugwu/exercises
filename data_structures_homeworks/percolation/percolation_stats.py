from percolation import Percolation
from random import randint


class PercolationStats:
  def __init__(self, n, trials):
    self.n = n
    self.trials = trials

  def single_threshold(self):
    perc = Percolation(self.n)

    while not perc.percolates():
      perc.open(
          row=randint(0, self.n - 1),
          col=randint(0, self.n - 1)
      )
    return perc.number_of_open_sites() / (self.n * self.n)

  def mean(self):
    sum_thresholds = 0

    for trial in range(0, self.trials):
      sum_thresholds += self.single_threshold()

    return sum_thresholds / self.trials
