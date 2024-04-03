import unittest, random
from ch4 import Node, Graph

class TestStack(unittest.TestCase):
    
    def setUp(self):
        # directed graph
        a1 = Node("a1")
        a = Node("a", [a1])
        b = Node("b", [a])
        c = Node("c", [b])
        d = Node("d", [c])
        test_graph = Graph([a1,a,b,c,d])

    def test_route_between_two_nodes_dfs(self):
        # Given a directed graph, design an algorithm to find out whether there is a route between two nodes
        self.assertTrue(self.test_graph.dfs(), )
        self.assertFalse(self.test_graph.dfs(), )

    def test_route_between_two_nodes_bfs(self):
        # Given a directed graph, design an algorithm to find out whether there is a route between two nodes
        self.assertEqual(self.test_stack.min(), 0)
