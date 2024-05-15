import unittest, random
from ch8 import Stairs


class TestGraphs(unittest.TestCase):

    def setUp(self):
        pass

    def test_triple_step(self):
        """
        Triple Step:
        A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.
        Implement a method to count how many possible ways the child can run up the stairs.
        """
        stairs = Stairs()
        # 0
        self.assertEqual(stairs.triple_step(0), 0)
        # 1
        self.assertEqual(stairs.triple_step(1), 1)
        # 1+1,                                 2
        self.assertEqual(stairs.triple_step(2), 2)
        # 1+1+1,                             1+2,   2+1,                     3
        self.assertEqual(stairs.triple_step(3), 4)

        # paths:   1+1+1+(1),   (1)+1+2, (1)+2+1, 2+1+(1), 2+2, 1+3, 3+1 steps
        # self.assertEqual(stairs.triple_step(4), 7)

        # paths on staircase with 5 steps
        # 1+1+1+1+1,
        # 1+1+1+2, 1+1+2+1, 1+2+1+1, 2+1+1+1,
        # 1+2+2,   2+1+2,     2+2+1
        # 1+1+3, 1+3+1, 3+1+1,
        # 2+3, 3+2
        print(f"5 steps: {stairs.triple_step(5)}")
        print(f"6 steps: {stairs.triple_step(6)}")
        print(f"7 steps: {stairs.triple_step(7)}")
        print(f"8 steps: {stairs.triple_step(8)}")
        print(f"9 steps: {stairs.triple_step(9)}")
        print(f"10 steps: {stairs.triple_step(10)}")
        for i in range(11, 200):
            print(f"{i} steps: {stairs.triple_step(i)}")

    def test_towers_of_hanoi_86(self):
        # Towers of Hanoi:
        # In the classic problem of the Towers of Hanoi, you have
        # 3 towers and N disks of different sizes which can slide onto any tower.
        # The puzzle starts with disks sorted in ascending order of size from top to bottom
        #   (i.e., each disk sits on top of an even larger one).
        # You have the following constraints:
        # (1) Only one disk can be moved at a time.
        # (2) A disk is slid off the top of one tower onto another tower.
        # (3) A disk cannot be placed on top of a smaller disk.
        # Write a program to move the disks from the first tower to the last using stacks.
        # Hints: #744, #224, #250, #272, #318

        def hint744(self):
            pass

        def hint224(self):
            pass

        def hint250(self):
            pass

        def hint272(self):
            pass

        def hint318(self):
            pass

        pass


if __name__ == "__main__":
    unittest.main()
