import copy


# adjacency list example
class Node:
    def __init__(self, name, neighbors=None) -> None:
        self.name = name
        self.neighbors = [] if not neighbors else neighbors

    def __str__(self) -> str:
        return f"{self.name}"


class Projects:
    def __init__(self, projects=None, dependencies=None):
        self.projects = [] if projects == None else projects
        self.dependencies = [] if dependencies == None else dependencies

    # pseudocode:
    # process projects with no dependencies
    # - if the project you're processing is already in path, raise an exception - you can't have projects in the path twice
    # - add project to path
    # - remove roject keys that have no dependencies
    # - remove project from values
    # return path
    # space complexity: O(V+E)
    # time complexity: O(V+E)
    #  we have to create the hash and we have to iterate through the edges once
    def build_order(self):
        projects_hash = {}
        path = []
        path_set = set()

        for project in self.projects:
            projects_hash[project] = []

        for dependency in self.dependencies:
            project = dependency[1]
            depends_on = dependency[0]
            projects_hash[depends_on].append(project)

        self.dfs(projects_hash, path, path_set)

    def dfs(self, projects_hash, path, path_set):
        if len(projects_hash) == 0:
            return path

        projects_with_no_dependencies = set()
        for depends_on in projects_hash:
            if (projects_hash[depends_on]) == 0:
                projects_with_no_dependencies.add(depends_on)

        # if there are only projects with dependencies left there must be a cycle somewhere
        if len(projects_with_no_dependencies) == 0 and len(projects_hash) > 0:
            raise Exception("cycle exists")

        # use the set of projects with no dependencies to remove the keys from the projects_hash dict
        # no projects are depending on projects when they have no elements in their dependency lists
        # add those projects to the path set for quick access and append them to the path
        for project in projects_with_no_dependencies:
            if project in path_set:
                raise Exception("cycle exists")
            del (projects_hash, project)
            path.append(project)
            path_set.add(project)

        # process the projects that depend on the project with no dependency to free up the projects that depend on them
        for depends_on in projects_hash:
            if depends_on in path_set:
                raise Exception("cycle exists")

            # process project
            for project in projects_with_no_dependencies:
                if project in projects_hash[depends_on]:
                    projects_hash.remove(project)

        return self.dfs(projects_hash, path, path_set)


class Graph:
    def __init__(self, vertices=None, edges=None):
        self.vertices = [] if vertices == None else vertices
        self.edges = [] if edges == None else edges

    # [
    # (self.a2, self.d2),
    # (self.d2, self.a2)
    # ]
    def depth_first_search(self, edge, path=set(), processed_edges=set()):
        # print(f"edge: {edge} path: {path} id:{id(path)}; processed_edges: {processed_edges} id:{id(processed_edges)}")

        processed_edges.add(edge)  # processed_edges = [(self.a2, self.d2)]

        starting_vertex = edge[0]  # self.a2
        path.add(starting_vertex)  # path = { self.a2 }

        ending_vertex = edge[1]  # self.d2
        path.add(ending_vertex)  # path = { self.a2, self.d2 }

        # [
        # (self.a2, self.d2),
        # (self.d2, self.a2) <--- edge_to_process
        # ]
        for edge_to_process in self.edges:
            # self.a2 > self.d2 > self.a2
            # (self.d2, >self.a2<) # self.a2
            if (
                edge_to_process[1] == starting_vertex
                and not (edge_to_process in processed_edges)
                and edge_to_process[1] in path
                and edge_to_process[0] in path
            ):
                # print(f"edge_to_process: ({edge_to_process[0].name},{edge_to_process[1].name}), starting_vertex: {starting_vertex.name}")
                raise Exception("cycle exists")

            # (>self.a2<, self.d2)
            if edge_to_process[0] == ending_vertex and not (
                edge_to_process in processed_edges
            ):
                self.depth_first_search(
                    edge_to_process, copy.deepcopy(path), copy.deepcopy(processed_edges)
                )

    def is_cycle(self):
        # for each starting point, we should never have a path that returns to the starting point, if we do, return False
        # traverse every path starting from every starting point
        # in every edge & traverse to the edge's ending point

        for edge in self.edges:
            new_path = set()
            new_processed_edges = set()
            self.depth_first_search(edge, new_path, new_processed_edges)

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
    def build_order(self):
        processed_projects = list()

        # get vertices with no in edges
        in_edges_hash = self.create_dependency_hash()
        in_edges_hash_2 = self.create_dependency_hash()
        if self.is_cycle():
            raise Exception("There exists a cycle in the dependencies")
        vertices_without_in_edges = self.get_no_in_edges(in_edges_hash)

        while len(vertices_without_in_edges) >= 1:
            # process vertices
            for vertex in vertices_without_in_edges:
                no_in_edges = set()
                # get outgoing edge from vertex
                for edge in in_edges_hash:
                    if vertex in in_edges_hash_2[edge]:
                        if len(in_edges_hash_2[edge]) == 1:
                            no_in_edges.add(edge)
                            in_edges_hash_2[edge].remove(vertex)
                            del in_edges_hash_2[edge]
                        else:
                            in_edges_hash_2[edge].remove(vertex)
                processed_projects.append(vertex)
            in_edges_hash = copy.deepcopy(in_edges_hash_2)
            vertices_without_in_edges = list(no_in_edges)
        if len(processed_projects) != len(self.vertices):
            raise Exception(
                "There exists a project that depends on building another project that is not available"
            )
        return processed_projects

    def build_order_dfs(self):
        hash_path = {}
        for edge in self.edges:
            starting_vertex = edge[0]
            ending_vertex = edge[1]

            if not (starting_vertex in self.vertices) or not (
                ending_vertex in self.vertices
            ):
                raise Exception("Dependency doesn't exist")

            hash_path[starting_vertex] = ending_vertex

        processed_vertices = []
        for vertex in self.vertices:
            if not (vertex in hash_path):
                processed_vertices.append(vertex)
            else:
                self.dfs(hash_path[vertex])

    def get_no_in_edges(self, in_edges_hash):
        no_in_edges = []
        for vertex in self.vertices:
            if not (vertex.name in in_edges_hash):
                no_in_edges.append(vertex.name)
        return no_in_edges

    def create_dependency_hash(self):
        # second element in edges tuple depends on the first element in tuple
        in_edges = {}
        # edges are dependencies
        for dependency in self.edges:
            if dependency[1].name in in_edges:
                in_edges[dependency[1].name].append(dependency[0].name)
            else:
                in_edges[dependency[1].name] = []
                in_edges[dependency[1].name].append(dependency[0].name)
        return in_edges

    def add_vertices(self, pass_vertices):
        for vertex in pass_vertices:
            self.vertices.append(vertex)

    def bidirectional_bfs(self, start_vertex, end_vertex):
        # O(k^(d/2))
        if start_vertex == end_vertex:
            return True

        visited = set()

        queue_left = []
        queue_left.append(start_vertex)

        queue_right = []
        queue_right.append(end_vertex)

        left_element = start_vertex
        right_element = end_vertex
        while len(queue_left) != 0 or len(queue_right) != 0:

            neighbors_left = left_element.neighbors
            neighbors_right = right_element.neighbors

            for neighbor in neighbors_left:
                if neighbor in visited:
                    return True
                else:
                    visited.add(neighbor)
                queue_left.append(neighbor)

            for neighbor in neighbors_right:
                if neighbor in visited:
                    return True
                else:
                    visited.add(neighbor)
                queue_right.append(neighbor)

            if len(queue_left) > 0:
                left_element = queue_left.pop(0)
            if len(queue_right) > 0:
                right_element = queue_right.pop(0)

        return False


# You don't necessarily need any additional classes to represent a graph. An array (or a hash table) of lists
# (arrays, arraylists, linked lists, etc.) can store the adjacency list. The graph above could be represented as:
# 0: 1
# 1: 2
# 2: 0, 3
# 3: 2
# 4: 6
# 5: 4
# 6: 5
# This is a bit more compact, but it isn't quite as clean. We tend to use node classes unless there's a compelling
# reason not to.


# Adjacency Matrices


# DFS
# def dfs(root):
#     if root == None:
#         return None

#     visit(root)
#     root.visited = True
#     for n in root.adjacent:
#         if n.visited == False:
#             search(n)


# def visit(node):
#     pass


# BFS uses a queue
# node a visits each of a's neighbors before visiting any
# of their neighbors. You can think of this as searching level
# by level out from a. An iterative solution involving a queue
# usually works best.
def bfs(root):
    queue = Queue()
    root.marked = True
    queue.enqueue(root)  # Add to the end of queue
    while not queue.is_empty():
        r = queue.dequeue()  # Remove from the front of the queue

    visit(r)

    for n in r.adjacent:
        if n.marked == False:
            n.marked = True
    queue.enqueue(n)


# Bidirectional Search
# Bidirectional search is used to find the shortest path between a source and destination node. It operates
# by essentially running two simultaneous breadth-first searches, one from each node. When their searches
# collide, we have found a path.
#
# In traditional breadth-first search, we would search up to k nodes in the first "level" of the search. In the
# second level, we would search up to k nodes for each of those first k nodes, so k
# 2 nodes total (thus far). We would do this d times, so that's 0(k^d) nodes.
#
# In bidirectional search, we have two searches that collide after approximately (d/2) levels (the midpoint
# of the path). The search from s visits approximately k^(d/2), as does the search from t. That's
# approximately 2*k^(d/2), or O(k^(d/2)), nodes total.

# Additional Reading:
# Topological Sort (pg 632),
# Dijkstra's Algorithm (pg 633),
# AVL Trees (pg 637),
# RedBlackTrees (pg 639).

# Questions
# Route Between Nodes:
# Given a directed graph, design an algorithm to find out whether there is a
# route between two nodes.


class LinkedListNode:
    def __init__(self, name, next=None) -> None:
        self.name = name
        self.next = next


class LinkedList:
    def __init__(self, head=None, tail=None) -> None:
        self.head = head
        self.tail = tail
        self.head.next = self.tail

    def add_after(self, element):
        self.tail.next = LinkedListNode(self.tail.name)
        self.tail.name = element
        self.tail = self.tail.next

    def __str__(self) -> str:
        current_node = self.head
        s = ""
        while current_node != None:
            s += f"{current_node.name} "
            current_node = current_node.next
        return s


class BinaryNode:
    def __init__(self, name=0, left=None, right=None, parent=None, height=0) -> None:
        self.name = name
        self.left = left
        self.right = right
        self.parent = parent
        self.height = height

    def traverse_inorder(self, nodes_list):
        if self == None:
            return

        if self.left != None:
            self.left.traverse_inorder(nodes_list)

        nodes_list.append(self)

        if self.right != None:
            self.right.traverse_inorder(nodes_list)

        return nodes_list

    def is_node_balanced(self):
        # print(f"0 self.name: {self.name} height: {self.height}")

        if self == None:
            return True
        if self.left == None and self.right == None:
            self.height = 0
            return True

        # print(f"1 self.name: {self.name} height: {self.height}")

        left_height = -1
        right_height = -1
        if self.left != None:
            # print(f"1.5 self.name: {self.name} height: {self.height} self.left.name: {self.left.name}")
            is_left_balanced = self.left.is_node_balanced()
            if is_left_balanced == False:
                return False
            left_height = self.left.height

        # print(f"2 self.name: {self.name} height: {self.height}")

        if self.right != None:
            # print(f"2.5 self.name: {self.name} height: {self.height} self.right.name: {self.right.name}")
            is_right_balanced = self.right.is_node_balanced()
            if is_right_balanced == False:
                return False
            right_height = self.right.height

        # print(f"3 self.name: {self.name} height: {self.height}")
        # l3 r1
        # l2 r1

        if left_height > right_height and left_height - 1 > right_height:
            # print(f"4 self.name: {self.name} height: {self.height}")
            return False
        if right_height > left_height and right_height - 1 > left_height:
            # print(f"5 self.name: {self.name} height: {self.height}")
            return False
        self.height = 1 + max(left_height, right_height)
        # print(f"6 self.name: {self.name} height: {self.height}")
        return True

    def __str__(self) -> str:
        return f"{self.name}"


class BinarySearchTree:
    def __init__(self, root=None) -> None:
        self.root = root

    def is_binary_search_tree(self):
        # ignored this because we would have to change the code to a list or something
        # self.is_fewer_than_two_children_root()

        return self.is_balanced() and self.elements_in_order_root()

    # helper function
    # def is_fewer_than_two_children_root(self):
    #     self.root.
    #     # return self.is_fewer_than_two_children(self.root)

    # def is_fewer_than_two_children(self, current_node = None):
    #     # base case 1
    #     if current_node == None:
    #         return True
    #     # base case 2
    #     print(f'keys: {current_node.keys}')
    #     if current_node.left == None and current_node.right == None:
    #         return True

    #     # check left subtree
    #     if current_node.left != None:
    #         if current_node.left >= current_node.name:
    #             return False
    #         if self.elements_in_order(current_node.left) == False:
    #             return False

    #     # check right subtree
    #     if current_node.right != None:
    #         if current_node.right <= current_node.name:
    #             return False
    #         if self.elements_in_order(current_node.right) == False:
    #             return False
    #     # all passed
    #     return True

    # helper function
    def elements_in_order_root(self):
        return self.elements_in_order(self.root)

    def elements_in_order(self, current_node):
        # print(f"0: {current_node.name}")
        if (
            current_node.left == None
            and current_node.right == None
            or current_node == None
        ):
            return True
        # print(f"1: {current_node.name}")

        if current_node.left != None:
            # print(f"1.5: {current_node.name}")

            if current_node.left.name >= current_node.name:
                # print(f"1.70: {current_node.name}")

                return False
            if self.elements_in_order(current_node.left) == False:
                # print(f"1.71: {current_node.name}")
                return False
        # print(2)
        if current_node.right != None:
            # print(f"2.5: {current_node.name}")

            if current_node.right.name <= current_node.name:
                # print(f"2.70: {current_node.name}")

                return False
            if self.elements_in_order(current_node.right) == False:
                # print(f"2.71: {current_node.name}")

                return False
        # print(f"3: {current_node.name}")
        return True

    def is_balanced(self):
        # print("inside is balanced")
        #          5
        #     2,            8
        #  1,     4,      7,     9
        # 0, N,  3, N,   6, N,  N, N
        # create the height of a single node
        # compare the height of left child node to right child node
        # print(f"self: {self}")
        if self.root == None:
            return True
        return self.root.is_node_balanced()

    def list_of_depths(self):
        depths = []

        queue = []
        queue.append(self.root)

        while len(queue) != 0:
            next_tier = []
            new_list = LinkedList(LinkedListNode("head"), LinkedListNode("tail"))
            depths.append(new_list.head)

            while len(queue) != 0:
                visit = queue.pop(0)
                # print(f"visit: {visit}")
                new_list.add_after(visit)
                if visit != None and visit.left != None:
                    next_tier.append(visit.left)
                if visit != None and visit.right != None:
                    next_tier.append(visit.right)
            queue = next_tier

        return depths

    def level_order_traversal(self):
        h = {}
        h[f"{self.root.name}"] = self.root.name
        self.root
        queue = []
        queue.append(self.root)
        s = ""
        while len(queue) != 0:
            next_tier = []
            while len(queue) != 0:
                visit = queue.pop(0)
                s += f" {visit} "
                if visit != None and visit.left != None:
                    h[f"{visit.name} left"] = visit.left.name
                    next_tier.append(visit.left)
                if visit != None and visit.right != None:
                    h[f"{visit.name} right"] = visit.right.name
                    next_tier.append(visit.right)
            queue = next_tier
            s += "\n"
        # print(s)
        return h

    def in_order_traversal(self, element):
        nodes_list = []
        self.traverse_inorder(nodes_list)

        i = 0
        while element != current_element:
            current_element = nodes_list[i]
            i += 1

        return nodes_list[i + 1]

    def traverse_inorder(self, nodes_list):

        return self.root.traverse_inorder(nodes_list)

    def create_unbalanced_tree_root(self, elements_list):

        self.root = BinaryNode(elements_list[0])
        current_node = self.root
        i = 0
        while i < len(elements_list):
            current_node.right = BinaryNode(elements_list)
            current_node = current_node.right
            i += 1
        return self.root

    def create_binary_tree_root(self, elements_list):
        if len(elements_list) == 0:
            return
        i = len(elements_list) // 2
        self.root = BinaryNode(elements_list[i])
        self.root.left = self.create_binary_tree(elements_list[:i])
        self.root.right = self.create_binary_tree(elements_list[(i + 1) :])

        return self.root

    def create_binary_tree(self, elements_list):
        if len(elements_list) == 0:
            return
        if len(elements_list) == 1:
            return BinaryNode(elements_list[0])

        i = len(elements_list) // 2
        parent_node = BinaryNode(elements_list[i])
        parent_node.right = self.create_binary_tree(elements_list[(i + 1) :])
        parent_node.left = self.create_binary_tree(elements_list[:i])
        return parent_node

    def get_next_node(self):
        if self.right != None:
            while self.left != None:
                self = self.left
            return self
        else:
            while self.parent != None:
                if self.parent.right != None and self.parent.right != trailing_node:
                    return self.parent.right.get_next_node()
                trailing_node = self
                self = self.parent

    # def get_next_node_recursion(self, trailing_node = None):
    #     if self.right != None:
    #         while self.left != None:
    #             self = self.left
    #         return self

    #     trailing_node = self
    #     self = self.parent

    #     if self.parent.right != None and self.parent.right != trailing_node:
    #         return self.parent.right.get_next_node()
    #     if self.parent.right != None and self.
    #     trailing_node = self
    #     self = self.parent

    # pseudocode:
    # use dfs to find the first occurrence of t1 or t2.
    # When they are on different branches, return the node where they split.
    # Assume both targets exist in the tree and if they both do not, then the first
    # target that appears will serve as the first common ancestor
    def first_common_ancestor(self, target1, target2):
        if self.root == None:
            return None

        if (
            self.dfs_target(self.root, target1) == None
            or self.dfs_target(self.root, target2) == None
        ):
            return None

        common_ancestor = self.dfs_or(self.root, target1, target2)
        return common_ancestor

    def dfs_target(self, current_node, target):
        if current_node == None:
            return None
        if current_node.name == target:
            return current_node
        left = None
        right = None
        if current_node.left != None:
            left = self.dfs_target(current_node.left, target)
        if left != None:
            return left
        if current_node.right != None:
            right = self.dfs_target(current_node.right, target)
        if right != None:
            return right

    def dfs_or(self, current_node, target1, target2):
        if (
            current_node == None
            or current_node.name == target1
            or current_node.name == target2
        ):
            return current_node
        left = None
        right = None

        if current_node.left != None:
            left = self.dfs_or(current_node.left, target1, target2)

        if current_node.right != None:
            right = self.dfs_or(current_node.right, target1, target2)

        if left != None and right != None:
            return current_node

        if left != None:
            return left

        if right != None:
            return right

        return None

    def insert_multiple_elements(self, elements):
        for element in elements:
            self.insert(element)

    def insert(self, element):
        if self.root == None:
            self.root = BinaryNode(element)
            return self.root

        current_node = self.root
        trailing_node = None
        while current_node != None:
            trailing_node = current_node
            if element > current_node.name:
                current_node = current_node.right
            else:
                current_node = current_node.left
        if trailing_node.name > element:
            trailing_node.left = BinaryNode(element)
        else:
            trailing_node.right = BinaryNode(element)

    # prompt:
    # A binary search tree was created by traversing through an array from left to right and inserting each element. Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree.
    # EXAMPLE
    # Input:
    #      2
    #   1     3
    # Output: {2, 1, 3}, {2, 3, 1}
    #
    # pseudocode:
    # using level traverse on a binary tree we are going to generate combinations
    # of the potential lists that could have been used to create a binary search tree
    # from the insert_multiple_elements method above
    def bst_sequences(self):
        paths = [[]]
        return self.bst_sequences_helper(self.root, paths)

    def bst_sequences_helper(self, node):
        left_paths = []
        right_paths = []

        if node == None:
            return

        if node.left != None:
            # get_left_paths
            pass

        if node.right != None:
            # get_right_paths
            pass

        # create lr_paths
        lr_paths = []

        # create rl_paths
        rl_paths = []

        if len(lr_paths + rl_paths) == 0:
            return [[node.name]]
        extensions = lr_paths + rl_paths
        for path in extensions:
            path = [node.name] + path

        return extensions

    #
    def check_subtree(self):
        pass
