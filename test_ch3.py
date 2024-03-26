import unittest, random
from ch3 import EmptyStackException, StackNode, MyStack

class TestStack(unittest.TestCase):
    
    def setUp(self):
        self.test_stack = MyStack()
        for element in random.shuffle(list(range(10))):
            self.test_stack.push(element)

    def test_min(self):
        self.assertEqual(self.test_stack.min(), 0)


    def test_is_palindrome_simple(self):
        self.assertTrue(self.list2.is_palindrome_simple())

    def test_get_kth_to_last_val(self):
        kth_val = self.list.get_kth_to_last_val(2)
        self.assertEqual(kth_val, 2)

    # More tests for each method...

if __name__ == '__main__':
    unittest.main()
