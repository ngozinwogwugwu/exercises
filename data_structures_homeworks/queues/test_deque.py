import unittest

from deque import *


class TestNode(unittest.TestCase):
  @classmethod
  def setUp(cls):
    cls.node = Node(2)

  def test_init(self):
    self.assertEqual(self.node.number, 2)
    self.assertEqual(self.node.next_node, None)
    self.assertEqual(self.node.previous_node, None)


class TestDeque(unittest.TestCase):
  def test_init(self):
    deque = Deque()
    self.assertEqual(deque.first, None)
    self.assertEqual(deque.last, None)
    self.assertEqual(deque.isEmpty(), True)

  def test_addFirst(self):
    deque = Deque()
    my_num = 2
    deque.addFirst(my_num)

    self.assertEqual(deque.first.number, my_num)
    self.assertEqual(deque.last.number, my_num)

    my_new_num = 4
    deque.addFirst(my_new_num)

    self.assertEqual(deque.first.number, my_new_num)
    self.assertEqual(deque.last.number, my_num)

  def test_addLast(self):
    deque = Deque()
    my_num = 2
    deque.addLast(my_num)

    self.assertEqual(deque.first.number, my_num)
    self.assertEqual(deque.last.number, my_num)

    my_new_num = 4
    deque.addLast(my_new_num)

    self.assertEqual(deque.last.number, my_new_num)
    self.assertEqual(deque.first.number, my_num)

  def test_addFirst(self):
    deque = Deque()
    my_num = 2
    my_second_num = 4

    deque.addFirst(my_num)
    deque.addFirst(my_second_num)

    self.assertEqual(deque.removeFirst(), my_second_num)
    self.assertEqual(deque.removeFirst(), my_num)
    self.assertEqual(deque.removeFirst(), None)

  def test_addLast(self):
    deque = Deque()
    my_num = 2
    my_second_num = 4

    deque.addLast(my_num)
    deque.addLast(my_second_num)

    self.assertEqual(deque.removeLast(), my_second_num)
    self.assertEqual(deque.removeLast(), my_num)
    self.assertEqual(deque.removeLast(), None)

  def test_iterator(self):
    deque = Deque()
    deque.addFirst(1)
    deque.addLast(2)
    deque.addFirst(3)
    deque.addLast(4)
    deque.addFirst(5)
    deque.addLast(6)
    deque.addFirst(7)
    deque.addLast(8)

    expected_output = [7, 5, 3, 1, 2, 4, 6, 8]
    actual_output = []

    for output in deque.iterator():
      actual_output.append(output)

    self.assertEqual(expected_output, actual_output)


if __name__ == "__main__":
  unittest.main()
