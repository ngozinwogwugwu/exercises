from enum import Enum


class IllegalArgumentException(Exception):
    pass


class NodeState(Enum):
    OPEN = "open"
    CLOSED = "closed"


class NodePosition(Enum):
    TOP = "top"
    BOTTOM = "bottom"


class NodeType(Enum):
    SYSTEM = "system"
    SPECIAL = "special"


class Node:
    state = NodeState.CLOSED
    node_type = NodeType.SYSTEM

    def __init__(self):
        self.parent = self

    def set_parent(self, parent_node):
        self.parent = parent_node

    def get_root(node):
        if node.parent is node:
            return node

        root_node = Node.get_root(node.parent)
        node.parent_node = root_node
        return root_node

    def get_tree_depth(node, depth_so_far=0):
        depth_so_far += 1
        if node.parent is node:
            return depth_so_far

        return Node.get_tree_depth(node.parent, depth_so_far)

    def is_open(self):
        return self.state is NodeState.OPEN

    def is_connected(node_a, node_b):
        return Node.get_root(node_a) == Node.get_root(node_b)

    def connect_nodes(node_a, node_b):
        big_tree_node = node_a
        little_tree_node = node_b

        if Node.get_tree_depth(node_a) < Node.get_tree_depth(node_b):
            big_tree_node = node_b
            little_tree_node = node_a

        Node.get_root(little_tree_node).set_parent(
            Node.get_root(big_tree_node))


class SpecialNode(Node):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.state = NodeState.OPEN

    def __repr__(self):
        return self.position.value


class SystemNode(Node):
    def __init__(self, row, col):
        super().__init__()
        self.row = row
        self.col = col

    def __repr__(self):
        return f"[{self.row},{self.col}]"

    def open(self):
        self.state = NodeState.OPEN


class Percolation:
    top_node = None
    bottom_node = None
    nodes = []
    n = 0
    num_open_nodes = 0

    def __init__(self, n):
        self.n = n
        self.nodes = [
            [SystemNode(row, col) for col in range(0, n)] for row in range(0, n)
        ]
        self.top_node = SpecialNode(NodePosition.TOP)
        self.bottom_node = SpecialNode(NodePosition.BOTTOM)

    def __repr__(self):
        all_text = ""
        for row in self.nodes:
            line_text = ""
            line_text += str([" " if node.state is NodeState.CLOSED else "x" for node in row])
            line_text += "      "
            line_text += str([node.parent for node in row])
            all_text += line_text
            all_text += '\n'
        return all_text

    def get_node(self, row, col):
        if row not in range(0, self.n) or col not in range(0, self.n):
            raise IllegalArgumentException
        return self.nodes[row][col]

    def connect_system_node_to_special_nodes(self, node):
        # if in top row, connect to top node
        if node.row is 0:
            Node.connect_nodes(node, self.top_node)

        # if in bottom row, connect to bottom row
        if node.row is self.n - 1:
            Node.connect_nodes(node, self.bottom_node)

    def connect_node_to_adjascents(self, node):
        for adjacent in self.get_adjacent_nodes(node):
            self.connect_system_nodes(adjacent, node)

    def get_node_if_exists(self, row, col):
        try:
            return self.get_node(row, col)
        except (IllegalArgumentException):
            return None

    def get_adjacent_nodes(self, node):
        adjacents = [
            self.get_node_if_exists(node.row - 1, node.col),
            self.get_node_if_exists(node.row + 1, node.col),
            self.get_node_if_exists(node.row, node.col - 1),
            self.get_node_if_exists(node.row, node.col + 1),
        ]

        return [adj for adj in adjacents if adj is not None]

    def open(self, row, col):
        node = self.get_node(row, col)
        if not node.is_open():
            node.open()
            self.num_open_nodes += 1

        self.connect_system_node_to_special_nodes(node)
        self.connect_node_to_adjascents(node)

    def is_open(self, row, col):
        return self.get_node(row, col).is_open()

    def connect_system_nodes(self, node_a, node_b):
        if NodeState.CLOSED in [node_a.state, node_b.state]:
            return

        Node.connect_nodes(node_a, node_b)

    def is_full(self, row, col):
        node = self.get_node(row, col)
        return Node.is_connected(node, self.top_node)

    def percolates(self):
        return Node.is_connected(self.bottom_node, self.top_node)

    def number_of_open_sites(self):
        return self.num_open_nodes
