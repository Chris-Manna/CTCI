# adjacency list example
class Node:
    def __init__(self, name, neighbors = []) -> None:
        self.name = name
        self.neighbors = neighbors

class Graph:
    def __init__(self, vertices = [], edges = []):
        self.vertices = vertices
        self.edges = edges
    
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
        
        pass

    def add_vertices(self, pass_vertices):
        for vertex in pass_vertices:
            self.vertices.append(vertex)
    
    def dfs(self, start_vertex, target_vertex):
        # potentially the O(n)
        # return True
        pass

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
def dfs(root):
    if (root == None):
        return None
    
    visit(root)
    root.visited = True
    for n in root.adjacent:
        if (n.visited == False):
            search(n)

def visit(node):
    pass

# BFS uses a queue
# node a visits each of a's neighbors before visiting any 
# of their neighbors. You can think of this as searching level 
# by level out from a. An iterative solution involving a queue 
# usually works best.
def bfs(root):
    queue = Queue()
    root.marked= True
    queue.enqueue(root) # Add to the end of queue
    while (not queue.is_empty()):
        r = queue.dequeue() # Remove from the front of the queue
    
    visit(r)
    
    for n in r.adjacent:
        if (n.marked == False):
            n. marked = True
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
    def __init__(self, name, next = None) -> None:
        self.name = name
        self.next = next
    
    
class LinkedList:
    def __init__(self, head = None, tail = None) -> None:
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
    def __init__(self, name = "", left = None, right = None, parent = None, height = 0) -> None:
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
    def __init__(self, root = None) -> None:
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
        if current_node.left == None and current_node.right == None or current_node == None:
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
            i+=1
        return self.root
    def create_binary_tree_root(self, elements_list):
        if len(elements_list) == 0:
            return
        i = len(elements_list) // 2
        self.root = BinaryNode(elements_list[i])
        self.root.left = self.create_binary_tree(elements_list[:i])
        self.root.right = self.create_binary_tree(elements_list[(i+1):])
        
        return self.root
        
    def create_binary_tree(self, elements_list):
        if len(elements_list) == 0:
            return
        if len(elements_list) == 1:
            return BinaryNode(elements_list[0])
        
        i = len(elements_list) // 2
        parent_node = BinaryNode(elements_list[i])
        parent_node.right = self.create_binary_tree(elements_list[(i+1):])
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
