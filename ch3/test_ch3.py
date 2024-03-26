import unittest, random
from ch3 import EmptyStackException, StackNode, MyStack

class TestStack(unittest.TestCase):
    
    def setUp(self):
        self.test_stack = MyStack()
        zero_to_ten = list(range(10))
        random.shuffle(zero_to_ten)
        for element in zero_to_ten:
            self.test_stack.push(element)

    def test_min(self):
        self.assertEqual(self.test_stack.min(), 0)


if __name__ == '__main__':
    unittest.main()
