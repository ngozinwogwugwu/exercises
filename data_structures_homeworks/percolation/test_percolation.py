import unittest
from percolation import (
    IllegalArgumentException,
    Percolation,
    Node,
    NodeState,
    SystemNode,
)


class TestSystemNode(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.node = SystemNode(1, 2)

    def test_init(self):
        node = SystemNode(0, 2)
        self.assertEqual(node.row, 0)
        self.assertEqual(node.col, 2)
        self.assertEqual(node.parent, node)
        self.assertEqual(node.state, NodeState.CLOSED)

    def test_set_parent(self):
        parent_node = SystemNode(1, 0)
        self.node.set_parent(parent_node)
        self.assertEqual(self.node.parent, parent_node)

    def test_get_root(self):
        root_node = SystemNode(0, 0)
        grandparent_node = SystemNode(0, 1)
        parent_node = SystemNode(0, 2)
        child_node = SystemNode(0, 3)

        child_node.set_parent(parent_node)
        parent_node.set_parent(grandparent_node)
        grandparent_node.set_parent(root_node)

        self.assertEqual(Node.get_root(child_node), root_node)


class TestPercolation(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.percolator = Percolation(5)

    def test_percolation_init(self):
        percolator = Percolation(5)
        self.assertEqual(len(percolator.nodes), 5)
        self.assertEqual(percolator.get_node(2, 3).state, NodeState.CLOSED)

    def test_open_handles_illegal_args(self):
        with self.assertRaises(IllegalArgumentException):
            self.percolator.open(-1, 2)

    def test_open(self):
        self.percolator.get_node(2, 3).open()
        self.assertEqual(self.percolator.get_node(2, 3).state, NodeState.OPEN)

    def test_open_top(self):
        self.assertNotEqual(
            Node.get_root(self.percolator.get_node(0, 3)),
            Node.get_root(self.percolator.top_node),
        )
        self.assertEqual(
            Node.is_connected(self.percolator.get_node(0, 3),
                              self.percolator.top_node),
            False,
        )

        self.percolator.open(0, 3)
        self.assertEqual(
            Node.get_root(self.percolator.get_node(0, 3)),
            Node.get_root(self.percolator.top_node),
        )

    def test_doesnt_connect_closed_nodes(self):
        percolator = Percolation(5)
        percolator.get_node(2, 3).open()

        percolator.connect_system_nodes(
            percolator.get_node(2, 3), percolator.get_node(3, 3)
        )
        self.assertEqual(percolator.get_node(
            2, 3).parent, percolator.get_node(2, 3))
        self.assertEqual(percolator.get_node(
            3, 3).parent, percolator.get_node(3, 3))

    def test_get_node_if_exists(self):
        self.assertEqual(self.percolator.get_node_if_exists(0, -1), None)
        self.assertEqual(
            self.percolator.get_node_if_exists(
                0, 0), self.percolator.get_node(0, 0)
        )

    def test_get_adjacent_nodes(self):
        center = self.percolator.get_node(2, 2)
        up = self.percolator.get_node(1, 2)
        down = self.percolator.get_node(3, 2)
        left = self.percolator.get_node(2, 1)
        right = self.percolator.get_node(2, 3)
        adjacents = [up, down, left, right]

        self.assertEqual(self.percolator.get_adjacent_nodes(center), adjacents)

    def test_get_adjacent_edge(self):
        center = self.percolator.get_node(0, 2)
        down = self.percolator.get_node(1, 2)
        left = self.percolator.get_node(0, 1)
        right = self.percolator.get_node(0, 3)
        adjacents = [down, left, right]

        self.assertEqual(self.percolator.get_adjacent_nodes(center), adjacents)

    def test_doesnt_connect_non_adjacent_nodes(self):
        self.percolator.get_node(2, 3).open()
        self.percolator.get_node(2, 3).open()

        self.percolator.connect_system_nodes(
            self.percolator.get_node(2, 3), self.percolator.get_node(0, 0)
        )
        self.assertEqual(
            self.percolator.get_node(
                2, 3).parent, self.percolator.get_node(2, 3)
        )
        self.assertEqual(
            self.percolator.get_node(
                0, 0).parent, self.percolator.get_node(0, 0)
        )

    def test_connect_three_nodes(self):
        node_a = self.percolator.get_node(2, 1)
        node_b = self.percolator.get_node(2, 2)
        node_c = self.percolator.get_node(2, 3)
        node_a.open()
        node_b.open()
        node_c.open()

        Node.connect_nodes(node_a, node_b)
        Node.connect_nodes(node_c, node_b)
        self.assertEqual(node_a.parent, node_c.parent)

    def test_is_open(self):
        self.percolator.get_node(0, 0).state = NodeState.CLOSED
        self.assertEqual(self.percolator.is_open(0, 0), False)

        self.percolator.open(0, 0)
        self.assertEqual(self.percolator.is_open(0, 0), True)

    def test_is_full(self):
        # here's my example - [2, 2] is not full
        #   [x][ ][ ][ ]
        #   [x][ ][ ][ ]
        #   [ ][x][*][ ]
        #   [ ][ ][ ][ ]
        percolator = Percolation(4)
        percolator.open(0, 0)
        percolator.open(2, 2)
        percolator.open(1, 0)
        percolator.open(2, 1)
        self.assertEqual(
            Node.is_connected(percolator.get_node(
                2, 2), percolator.top_node), False
        )

        # [2, 2] is not full
        #   [x][ ][ ][ ]
        #   [x][ ][ ][ ]
        #   [x][x][*][ ]
        #   [ ][ ][ ][ ]

        percolator.open(2, 0)
        self.assertEqual(
            Node.is_connected(percolator.get_node(2, 2),
                              percolator.top_node), True
        )

    def test_percolates(self):
        # here's my example - does not percolate
        #   [x][ ][ ][ ]
        #   [x][ ][ ][ ]
        #   [ ][x][ ][ ]
        #   [ ][x][ ][ ]
        percolator = Percolation(4)
        percolator.open(0, 0)
        percolator.open(1, 0)
        percolator.open(2, 1)
        percolator.open(3, 1)
        self.assertEqual(percolator.percolates(), False)

        # here's my example - does percolate
        #   [x][ ][ ][ ]
        #   [x][x][ ][ ]
        #   [ ][x][ ][ ]
        #   [ ][x][ ][ ]

        percolator.open(1, 1)
        self.assertEqual(percolator.percolates(), True)

    def test_number_of_open_sites(self):
        percolator = Percolation(5)
        self.assertEqual(percolator.number_of_open_sites(), 0)

        percolator.open(0, 0)
        self.assertEqual(percolator.number_of_open_sites(), 1)

        percolator.open(0, 0)
        self.assertEqual(percolator.number_of_open_sites(), 1)

        percolator.open(0, 2)
        self.assertEqual(percolator.number_of_open_sites(), 2)


if __name__ == "__main__":
    unittest.main()
