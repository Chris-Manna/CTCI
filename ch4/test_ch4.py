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
        self.test_graph_1 = Graph([self.a1, self.a, self.b, self.c, self.d])

        # directed graph
        self.a2 = Node("a")
        self.b2 = Node("b")
        self.c2 = Node("c")
        self.d2 = Node("d")
        self.e2 = Node("e")
        self.f2 = Node("f")
        self.g2 = Node("g")

        # [
        # (self.f2, self.b2),
        # (self.b2, self.d2),
        # (self.f2, self.a2),
        # (self.a2, self.d2),
        # (self.d2, self.c2),
        # ]
        self.test_graph_2 = Graph(
            [self.a2, self.b2, self.c2, self.d2, self.e2, self.f2],
            [
                (self.a2, self.d2),
                (self.f2, self.b2),
                (self.b2, self.d2),
                (self.f2, self.a2),
                (self.d2, self.c2),
            ],
        )

        self.test_graph_3 = Graph(
            [self.a2, self.b2, self.c2, self.d2, self.e2, self.f2],
            [
                (self.a2, self.d2),
                (self.f2, self.b2),
                (self.b2, self.d2),
                (self.f2, self.a2),
                (self.d2, self.c2),
                (self.d2, self.g2),
            ],
        )

        self.test_graph_cycle_exists_1 = Graph(
            [self.a2, self.b2, self.c2, self.d2, self.e2, self.f2],
            [(self.a2, self.d2), (self.d2, self.a2)],
        )
        self.test_graph_cycle_exists_2 = Graph(
            [self.a2, self.b2, self.c2, self.d2, self.e2, self.f2],
            [(self.a2, self.b2), (self.b2, self.d2), (self.d2, self.a2)],
        )
        self.test_graph_cycle_exists_3 = Graph(
            [self.a2, self.b2, self.c2, self.d2, self.e2, self.f2],
            [
                (self.a2, self.b2),
                (self.b2, self.c2),
                (self.a2, self.c2),
                (self.b2, self.d2),
                (self.d2, self.a2),
            ],
        )

        self.basic_test = Graph(
            [self.a2, self.b2, self.c2, self.d2, self.e2, self.f2],
            [
                (self.a2, self.d2),
                (self.f2, self.b2),
                (self.b2, self.d2),
                (self.f2, self.a2),
                (self.d2, self.c2),
            ],
        )

        self.cycle_test = Graph(

            [self.a2, self.b2, self.c2, self.d2, self.e2, self.f2],
            [
                (self.a2, self.d2),
                (self.d2, self.a2),
            ],
        )

        # inorder tree traversal, brute force

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
        # 1   5
        #   / \
        #  4   6

        self.ten.left = self.three
        self.three.left = self.one
        self.three.right = self.five
        self.five.left = self.four
        self.five.right = self.six
        self.test_binary_tree = BinarySearchTree(self.ten)

        # Question 4.2 Minimal Tree
        self.elements_list = list(range(10))
        self.test_create_binary_tree = BinarySearchTree()

        self.test_unbalanced_binary_tree = BinarySearchTree()

    def test_route_between_two_nodes_bidirectional_bfs_1(self):
        # Given a directed graph, design an algorithm to find out whether there is a route between two nodes
        self.assertTrue(self.test_graph_1.bidirectional_bfs(self.a, self.a))
        self.assertTrue(self.test_graph_1.bidirectional_bfs(self.a, self.a1))
        self.assertTrue(self.test_graph_1.bidirectional_bfs(self.a, self.d))

    def test_minimal_tree_2(self):
        # Minimal Tree:
        # Given a sorted (increasing order) array with unique integer elements,
        # write an algorithm to create a binary search tree with minimal height.
        #
        # test that all elements are in order

        self.test_create_binary_tree.create_binary_tree_root(self.elements_list)
        passed_list = []
        passed_list = self.test_create_binary_tree.traverse_inorder(passed_list)
        i = 0
        while i < len(passed_list):
            self.assertEqual(str(passed_list[i]), str(self.elements_list[i]))
            i += 1
        # print(self.test_create_binary_tree.level_order_traversal())
        #
        # test that all leaves in the tree at at the same height or
        # within one of the maximum height leaf

    def test_list_of_depths_3(self):
        # Given a binary tree, design an algorithm which creates a linked list of all
        # the nodes at each depth (e.g., if you have a tree with depth D,
        # you'll have D linked lists).

        # self.test_create_binary_tree.create_binary_tree_root(self.elements_list)
        # depths = self.test_create_binary_tree.list_of_depths()
        # i = 0
        # tiers = [["head",5,"tail"],["head",2, 8,"tail"],["head",1,4,7,9,"tail"],["head",0,3,6,"tail"]]
        # while i < len(depths):
        #     current_node = depths[i]
        #     tier = tiers[i]
        #     j = 0
        #     while current_node != None:
        #         # print(f"current_node: {current_node.name} element: {tier[j]}")
        #         self.assertEqual(str(tier[j]), str(current_node.name))
        #         current_node = current_node.next
        #         j += 1
        #     i += 1
        pass

    def test_check_balanced_4(self):
        # Implement a function to check if a binary tree is balanced. For the purposes of
        # this question, a balanced tree is defined to be a tree such that the heights of
        # the two subtrees of any node never differ by more than one.

        self.test_create_binary_tree.create_binary_tree_root([])
        self.assertTrue(self.test_create_binary_tree.is_balanced())

        self.test_create_binary_tree.create_binary_tree_root([0])
        self.assertTrue(self.test_create_binary_tree.is_balanced())

        self.test_create_binary_tree.create_binary_tree_root([0, 1])
        self.assertTrue(self.test_create_binary_tree.is_balanced())

        self.test_create_binary_tree.create_binary_tree_root([0, 1, 2])
        self.assertTrue(self.test_create_binary_tree.is_balanced())

        self.test_create_binary_tree.create_binary_tree_root([0, 1, 2, 3])
        self.assertTrue(self.test_create_binary_tree.is_balanced())

        self.test_create_binary_tree.create_binary_tree_root([0, 1, 2, 3, 4])
        self.assertTrue(self.test_create_binary_tree.is_balanced())

        self.test_create_binary_tree.create_binary_tree_root([0, 1, 2, 3, 4, 5])
        self.assertTrue(self.test_create_binary_tree.is_balanced())

        self.test_create_binary_tree.create_binary_tree_root([0, 1, 2, 3, 4, 5, 6])
        self.assertTrue(self.test_create_binary_tree.is_balanced())

        self.test_create_binary_tree.create_binary_tree_root([0, 1, 2, 3, 4, 5, 6, 7])
        self.assertTrue(self.test_create_binary_tree.is_balanced())

        self.test_create_binary_tree.create_binary_tree_root(
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        )
        self.assertTrue(self.test_create_binary_tree.is_balanced())

        self.test_create_binary_tree.create_binary_tree_root(
            [0, 1, 2, 7, 8, 9, 10, 3, 4, 5, 6]
        )
        self.assertTrue(self.test_create_binary_tree.is_balanced())

        self.test_unbalanced_binary_tree.create_unbalanced_tree_root(
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        )
        self.assertFalse(self.test_unbalanced_binary_tree.is_balanced())

    def test_validate_bst_5(self):
        # Implement a function to check if a binary tree is a binary search tree.

        # tree is is balanced
        self.test_create_binary_tree.create_binary_tree_root(
            [0, 1, 2, 7, 8, 9, 10, 3, 4, 5, 6]
        )
        self.assertFalse(self.test_create_binary_tree.elements_in_order_root())

        self.test_create_binary_tree.create_binary_tree_root(
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        )
        self.assertTrue(self.test_create_binary_tree.elements_in_order_root())

        self.assertTrue(self.test_create_binary_tree.is_binary_search_tree())

        # all elements in the left subtree are smaller than the parent element &
        # all elements int he right subtree are greater than the parent element

        # height of the tree is log n of total number of elements - is this right?

        # ignored this
        # self.assertTrue(self.test_create_binary_tree.is_fewer_than_two_children_root())

    def test_successor_6(self):
        # Write an algorithm to find the "next" node (i.e., in-order successor)
        # of a given node in a binary search tree.
        # You may assume that each node has a link to its parent.
        # this tree is not yet included
        #      15
        #    /     \
        #  12       20
        # /  \      / \
        # 10   14   17  22

        # self.assertEqual(self.test_binary_tree.in_order_traversal(6), 10)
        pass


    def test_build_order_with_dfs(self):

        self.basic_test.build_order()

        with self.assertRaises(Exception):
            self.cycle_test.build_order()
        

    def test_build_order_7(self):
        # You are given a list of projects and a list of dependencies
        # (which is a list of pairs of projects, where the second project is dependent on
        # the first project).
        # All of a project's dependencies must be built before the project is.
        # Find a build order that will allow the projects to be built.
        # If there is no valid build order, return an error.
        # EXAMPLE
        # Input:
        # projects: a, b, c, d, e, f
        # dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
        # Output: f, e, a, b, d, c
        # Hints: #26, #47, #60, #85, #725, #133

        # pseudocode: DAG
        # WATCH FOR: cycles
        # - go through each project and get the dependency
        # - treat each project like a vertex

        # go through dependencies and resolve them one at a time, creating a chain - it may be a linked list
        # a <- d
        # f <- b
        # b <- d
        # f <- a
        # d <- c
        # they may intersect and there should never be a cycle
        # arrange the list of projects
        # start from the element that has the most dependencies and then work backwards from that point
        # ve
        # this depends on the number of edges go into a single project
        # FIRST:
        # ensure there are no cycles
        # f <- a <- d
        # f <- b
        # b <- d
        # # to do this, we can create a linked list or a hash table
        # # if there is a cycle, throw error
        # SECOND:
        # organize based on the number of vertices in a build
        # organize based on the number of edges in a single build
        # if there are the same number of edges, organize based on the number of

        # no cycle
        # print("no cycle: ")

        with self.assertRaises(Exception):
            self.test_graph_cycle_exists_1.build_order()

        with self.assertRaises(Exception):
            self.test_graph_3.build_order()

        # # test cycle
        with self.assertRaises(Exception):
            self.test_graph_cycle_exists.build_order()
        
        self.test_graph_2.build_order()
        
        # projects: a, b, c, d, e, f
        # dependencies: (a,d), (f,b), (b,d), (f,a), (d,c)
    
    def test_build_order_72(self):
        # solve using depth first search
        # You are given a list of projects and a list of dependencies
        # (which is a list of pairs of projects, where the second project is dependent on
        # the first project).
        # All of a project's dependencies must be built before the project is.
        # Find a build order that will allow the projects to be built.
        # If there is no valid build order, return an error.
        # EXAMPLE
        # Input:
        # projects: a, b, c, d, e, f
        # dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
        # Output: f, e, a, b, d, c
        # Hints: #26, #47, #60, #85, #725, #133

        pass

    def test_first_common_ancestor_8(self):

        # [0,1,2,3,4,5,6,7,8,9]
        self.test_create_binary_tree.create_binary_tree_root(self.elements_list)
        self.assertEqual(self.test_create_binary_tree.first_common_ancestor(3,25), None)
        self.assertEqual(self.test_create_binary_tree.first_common_ancestor(3,5).name, 5)
        #    10
        #   /
        #  3
        # / \
        # 1   5
        #   / \
        #  4   6
        # 
        self.test_binary_tree = BinarySearchTree(self.ten)

        self.assertEqual(self.test_binary_tree.first_common_ancestor(10,3).name,10)
        self.assertEqual(self.test_binary_tree.first_common_ancestor(self.four.name,self.six.name).name,5)
        self.assertEqual(self.test_binary_tree.first_common_ancestor(3,6).name,3)

    def test_bst_sequences_9(self):
        def hint1(self):
            # What is the very first value that must be in each array? 
            pass
        def hint2(self):
            #48
            pass
        def hint3(self):
            #66
            pass
        def hint4(self):
            #82
            pass

        elements0 = [2]
        self.bst_sequences_tree_test1 = BinarySearchTree()
        self.bst_sequences_tree_test1.insert_multiple_elements(elements0)
        paths0 = self.bst_sequences_tree_test1.bst_sequences()
        print(f"paths0: {paths0}")
        # self.assertListEqual(paths0,[elements0])
        
        elements0_left = [2,1]
        self.bst_sequences_tree_test2 = BinarySearchTree()
        self.bst_sequences_tree_test2.insert_multiple_elements(elements0_left)
        paths1 = self.bst_sequences_tree_test2.bst_sequences()
        print(f"paths1: {paths1}")

        elements0_right = [2,3]
        self.bst_sequences_tree_test3 = BinarySearchTree()
        self.bst_sequences_tree_test3.insert_multiple_elements(elements0_right)
        paths2 = self.bst_sequences_tree_test3.bst_sequences()
        print(f"paths2: {paths2}")

        elements1 = [2, 1, 3]
        self.bst_sequences_tree_test4 = BinarySearchTree()
        self.bst_sequences_tree_test4.insert_multiple_elements(elements1)
        paths3 = self.bst_sequences_tree_test4.bst_sequences()
        print(f"paths3: {paths3}")
        
        elements1 = [2, 1, 3]
        self.bst_sequences_tree_test4 = BinarySearchTree()
        self.bst_sequences_tree_test4.insert_multiple_elements(elements1)
        paths3 = self.bst_sequences_tree_test4.bst_sequences()
        print(f"paths3: {paths3}")

        elements1 = [3,1,2,0,5,4,6]
        self.bst_sequences_tree_test5 = BinarySearchTree()
        self.bst_sequences_tree_test5.insert_multiple_elements(elements1)
        paths4 = self.bst_sequences_tree_test5.bst_sequences()
        print(f"paths4: {len(paths4)}")

        
        # self.bst_sequences_tree_test1.bst_sequences()
        # print(f"permuted_levels: {all_levels_combined}")
     
        
        # # self.bst_sequences_tree_test1.bst_sequences()
        
        # elements2 = [2,3,1]
        # self.bst_sequences_tree_test1.root = None
        # self.bst_sequences_tree_test2 = BinarySearchTree()
        # self.bst_sequences_tree_test2.insert_multiple_elements(elements2)

        # self.bst_sequences_tree_test3 = BinarySearchTree()

        # test = set()
        # test.add((1,3))
        # test.add((3,1))
        # self.assertSetEqual(self.bst_sequences_tree_test3.create_permutations([1,3]),test)
        # self.bst_sequences_tree_test3.create_permutations([1,3,6,8])


    def test_check_subtree_10(self):
        # Check Subtree: 
        # T1 and T2 are two very large binary trees, with T1 much bigger than T2. 
        # Create an algorithm to determine if T2 is a subtree of T1.
        # A tree T2 is a subtree of T1 if there exists a node n in T1 such that 
        # the subtree of n is identical to T2. That is, if you cut off the tree 
        # at node n, the two trees would be identical. 
        def hint1(self):
            # If T2 is a subtree of Tl, how will its in-order traversal compare to Tl's? 
            # What about its pre-order and post-order traversal?
            pass
        def hint2(self):
            pass
        def hint3(self):
            pass
        def hint4(self):
            pass

        pass

    def test_random_node_11(self):
        pass

    def test_paths_with_sum_12(self):
        pass

    def test_nine_balls(self):
        123456789
        a = 123
        b = 456
        c = 789
        
        balance1 = 123^456
        balance2 = 1^3 # (2) on the side OR if 123^456 is balanced...
        balance3 = 7^9 # (8) on the side
        pass


if __name__ == "__main__":
    unittest.main()
