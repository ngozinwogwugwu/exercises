class LineSegment:
  def __init__(self, p,  q):
    self.p = p
    self.q = q

  def __repr__(self):
    return f"({self.p}, {self.q})"