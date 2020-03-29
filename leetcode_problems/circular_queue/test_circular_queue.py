import unittest
from circular_queue import MyCircularQueue


class TestMyCircularQueue(unittest.TestCase):
  def test_init(self):
    circ_q = MyCircularQueue(4)

    self.assertEqual(circ_q.array, [None, None, None, None])
    self.assertEqual(circ_q.head, 0)
    self.assertEqual(circ_q.tail, -1)

  def test_enQueue(self):
    circ_q = MyCircularQueue(2)
    self.assertTrue(circ_q.enQueue(1))
    self.assertTrue(circ_q.enQueue(2))
    self.assertFalse(circ_q.enQueue(3))

  def test_deQueue(self):
    circ_q = MyCircularQueue(3)
    circ_q.enQueue(2)
    circ_q.enQueue(4)
    circ_q.enQueue(6)
    self.assertEqual(circ_q.array, [2, 4, 6])

    self.assertTrue(circ_q.deQueue())
    self.assertTrue(circ_q.deQueue())
    self.assertTrue(circ_q.deQueue())
    self.assertFalse(circ_q.deQueue())

  def test_Front(self):
    circ_q = MyCircularQueue(3)
    circ_q.enQueue(2)
    circ_q.enQueue(4)
    self.assertEqual(circ_q.Front(), 2)

  def test_Rear(self):
    circ_q = MyCircularQueue(3)
    circ_q.enQueue(2)
    circ_q.enQueue(4)
    self.assertEqual(circ_q.Rear(), 4)

  def test_isEmpty(self):
    circ_q = MyCircularQueue(4)
    self.assertTrue(circ_q.isEmpty())

    # fill it up
    circ_q.enQueue(2)
    self.assertFalse(circ_q.isEmpty())
    circ_q.enQueue(2)
    self.assertFalse(circ_q.isEmpty())
    circ_q.enQueue(2)
    self.assertFalse(circ_q.isEmpty())    
    circ_q.enQueue(2)
    self.assertFalse(circ_q.isEmpty())

    # empty it out
    circ_q.deQueue()
    self.assertFalse(circ_q.isEmpty())
    circ_q.deQueue()
    self.assertFalse(circ_q.isEmpty())
    circ_q.deQueue()
    self.assertFalse(circ_q.isEmpty())    
    circ_q.deQueue()
    self.assertTrue(circ_q.isEmpty())


  def test_isFull(self):
    circ_q = MyCircularQueue(4)
    self.assertFalse(circ_q.isFull())

    # fill it up
    circ_q.enQueue(2)
    self.assertFalse(circ_q.isFull())
    circ_q.enQueue(2)
    self.assertFalse(circ_q.isFull())
    circ_q.enQueue(2)
    self.assertFalse(circ_q.isFull())    
    circ_q.enQueue(2)
    self.assertTrue(circ_q.isFull())

    # empty it out
    circ_q.deQueue()
    self.assertFalse(circ_q.isFull())    

    # fill it up again
    circ_q.enQueue(2)
    self.assertTrue(circ_q.isFull())

  def test_nextPointerPosition(self):
    circ_q = MyCircularQueue(4)
    self.assertEqual(circ_q.nextPointerPosition(circ_q.head), 1)

    circ_q.head = 3
    self.assertEqual(circ_q.nextPointerPosition(circ_q.head), 0)

  def test_case_from_leetcode(self):
    circularQueue = MyCircularQueue(3)
    self.assertTrue(circularQueue.enQueue(1))
    self.assertTrue(circularQueue.enQueue(2))
    self.assertTrue(circularQueue.enQueue(3))
    self.assertFalse(circularQueue.enQueue(4))

    self.assertEqual(circularQueue.Rear(), 3)
    self.assertTrue(circularQueue.isFull())
    self.assertTrue(circularQueue.deQueue())
    self.assertTrue(circularQueue.enQueue(4))
    self.assertEqual(circularQueue.Rear(), 4)

if __name__ == "__main__":
  unittest.main()
