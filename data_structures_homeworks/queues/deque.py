

class Node():
  def __init__(self, number):
    self.next_node = None
    self.previous_node = None
    self.number = number

class Deque():

  def __init__(self):
    self.first = None
    self.last = None

  def isEmpty(self):
    return self.first is None and self.last is None

  def size(self):
    if self.isEmpty():
      return 0


  def addFirst(self, number):
    new_node = Node(number)

    if self.isEmpty():
      self.last = new_node
    else:
      self.first.previous_node = new_node

    new_node.next_node = self.first
    self.first = new_node


  def addLast(self, number):
    new_node = Node(number)

    if self.isEmpty():
      self.first = new_node
    else:
      self.last.next_node = new_node

    new_node.previous_node = self.last
    self.last = new_node


  def removeFirst(self):
    if self.isEmpty():
      return None

    first_node = self.first
    self.first = first_node.next_node

    if self.first is None:
      self.last = None
    else:
      self.first.previous_node = None

    return first_node.number

  def removeLast(self):
    if self.isEmpty():
      return None

    last_node = self.last
    self.last = last_node.previous_node

    if self.last is None:
      self.first = None
    else:
      self.last.next_node = None

    return last_node.number

  def iterator(self):
    current_node = self.first

    while current_node is not None:
      yield current_node.number
      current_node = current_node.next_node

