import unittest
from ch2.ch2 import Node, LinkedList

class TestLinkedList(unittest.TestCase):
    
    def setUp(self):
        # This will run before each test
        self.list = LinkedList()
        self.nodes_values = [1, 2, 3, 2, 1]
        self.nodes = [Node(value=val) for val in self.nodes_values]

        for i in range(len(self.nodes) - 1):
            self.nodes[i].next = self.nodes[i + 1]
        self.list.head = self.nodes[0]
        self.list.tail = self.nodes[-1]

        # Setting up the second list with string values
        self.list2 = LinkedList()
        self.nodes_values2 = ['a', 'b', 'c', 'b', 'a']
        self.nodes2 = [Node(value=val) for val in self.nodes_values2]

        for i in range(len(self.nodes2) - 1):
            self.nodes2[i].next = self.nodes2[i + 1]
        self.list2.head = self.nodes2[0]
        self.list2.tail = self.nodes2[-1]

    def test_remove_dups(self):
        # Assuming remove_dups removes duplicate values
        self.list.remove_dups()
        current = self.list.head
        values = []
        while current:
            values.append(current.value)
            current = current.next
        self.assertEqual(values, [1, 2, 3])

    def test_is_palindrome_simple(self):
        self.assertTrue(self.list2.is_palindrome_simple())

    def test_get_kth_to_last_val(self):
        kth_val = self.list.get_kth_to_last_val(2)
        self.assertEqual(kth_val, 2)

    # More tests for each method...

if __name__ == '__main__':
    unittest.main()
