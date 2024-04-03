import unittest, random
from ch4 import Node, Graph

class TestGraphs(unittest.TestCase):
    
    def setUp(self):
        # directed graph
        self.a1 = Node("a1")
        self.a = Node("a", [self.a1])
        self.b = Node("b", [self.a])
        self.c = Node("c", [self.b])
        self.d = Node("d", [self.c])
        self.test_graph = Graph([self.a1, self.a, self.b, self.c, self.d])

    def test_route_between_two_nodes_bidirectional_bfs(self):
        print("inside test")
        # Given a directed graph, design an algorithm to find out whether there is a route between two nodes
        self.assertTrue(self.test_graph.bidirectional_bfs(self.a, self.a))
        # self.assertTrue(self.test_graph.bidirectional_bfs(self.a, self.a1))

    def test_route_between_two_nodes_bfs(self):
        # Given a directed graph, design an algorithm to find out whether there is a route between two nodes
        # self.assertEqual(self.test_stack.min(), 0)
        pass

    

if __name__ == '__main__':
    unittest.main()
