import unittest, random
from ch4 import Node, Graph, BinaryNode, BinarySearchTree

class TestGraphs(unittest.TestCase):
    
    def setUp(self):
        # directed graph
        self.a1 = Node("a1")
        self.a = Node("a", [self.a1])
        self.b = Node("b", [self.a])
        self.c = Node("c", [self.b])
        self.d = Node("d", [self.c])
        self.test_graph = Graph([self.a1, self.a, self.b, self.c, self.d])


        # inorder tree traversal

        self.ten = BinaryNode(10)
        self.three = BinaryNode(3)
        self.one = BinaryNode(1)
        self.five = BinaryNode(5)
        self.four = BinaryNode(4)
        self.six = BinaryNode(6)

        #    10
        #   /
        #  3
        # / \
        #1   5
        #   / \
        #  4   6

        self.ten.left = self.three
        self.three.left = self.one
        self.three.right = self.five
        self.five.left = self.four
        self.five.right = self.six
        self.test_binary_search_tree =  BinarySearchTree(self.ten)

    def test_route_between_two_nodes_bidirectional_bfs(self):
        # Given a directed graph, design an algorithm to find out whether there is a route between two nodes
        self.assertTrue(self.test_graph.bidirectional_bfs(self.a, self.a))
        self.assertTrue(self.test_graph.bidirectional_bfs(self.a, self.a1))
        self.assertTrue(self.test_graph.bidirectional_bfs(self.a, self.d))

    def test_minimal_tree(self):
        # Minimal Tree: 
        # Given a sorted (increasing order) array with unique integer elements, 
        # write an algorithm to create a binary search tree with minimal height. 

        pass
    
    def test_successor_6(self):
        # Write an algorithm to find the "next" node (i.e., in-order successor) 
        # of a given node in a binary search tree.
        # You may assume that each node has a link to its parent.
        # this tree is not yet included 
        #      4
        #   /    \
        #  2      6
        # / \    / \
        #1   3   5  7
        self.assertEqual(self.test_binary_search_tree.in_order_traversal(6), 10)
        pass

    

if __name__ == '__main__':
    unittest.main()
