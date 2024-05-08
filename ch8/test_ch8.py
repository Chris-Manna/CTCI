import unittest, random
from ch8 import triple_step


class TestGraphs(unittest.TestCase):

    def setUp(self):
        pass

    def test_triple_step(self):
        """
        Triple Step:
        A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.
        Implement a method to count how many possible ways the child can run up the stairs.
        """
        # 0
        self.assertEqual(triple_step(0), 0)
        # 1
        self.assertEqual(triple_step(1), 1)
        # 1+1,                                 2
        self.assertEqual(triple_step(2), 2)
        # 1+1+1,                             1+2,   2+1,                     3
        self.assertEqual(triple_step(3), 4)

        # paths:   1+1+1+(1),   (1)+1+2, (1)+2+1, 2+1+(1), 2+2, 1+3, 3+1 steps
        self.assertEqual(triple_step(4), 7)

        # paths on staircase with 5 steps
        # 1+1+1+1+1, 
        # 1+1+1+2, 1+1+1+2+1, 1+1+2+1, 1+2+1+1, 2+1+1+1,
        # 1+2+2,   2+1+2,     2+2+1
        # 1+1+3, 1+3+1, 3+1+1,
        # 2+3, 3+2
        print(f"5 steps: {triple_step(5)}")
        # print(triple_step(6))
        # print(triple_step(7))
        # print(triple_step(8))
        # print(triple_step(9))
        # print(triple_step(10))


if __name__ == "__main__":
    unittest.main()
