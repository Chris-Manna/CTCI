import unittest, random
from ch3 import EmptyStackException, StackNode, MyStack, SetOfStacks, SetOfStacksLists

class TestStack(unittest.TestCase):
    
    def setUp(self):
        self.test_stack = MyStack()
        zero_to_ten = list(range(10))
        random.shuffle(zero_to_ten)
        for element in zero_to_ten:
            self.test_stack.push(element)
        

        self.new_stack_set = SetOfStacksLists()
        zero_to_twenty = list(range(20))
        # random.shuffle(zero_to_twenty)
        for element in zero_to_twenty:
            self.new_stack_set.push(element)

    def test_min(self):
        self.assertEqual(self.test_stack.min(), 0)
    
    def test_set_of_stacks_lists_pop(self):
        self.assertEqual(self.new_stack_set.pop(), 19)
    
    def test_set_of_stacks_lists_pop_at_1(self):
        self.assertEqual(self.new_stack_set.pop_at(1), 19)

    def test_set_of_stacks_lists_pop_at_0(self):
        self.assertEqual(self.new_stack_set.pop_at(0), 9)
        self.assertEqual(self.new_stack_set.pop_at(0), 8)


if __name__ == '__main__':
    unittest.main()
