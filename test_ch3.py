import unittest, random
from ch3 import EmptyStackException, StackNode, MyStack

class TestStack(unittest.TestCase):
    
    def setUp(self):
        self.test_stack = MyStack()
        for element in random.shuffle(list(range(10))):
            self.test_stack.push(element)

    def test_min(self):
        self.assertEqual(self.test_stack.min(), 0)


if __name__ == '__main__':
    unittest.main()
