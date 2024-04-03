# adjacency list example
class Node:
    def __init__(self, name, children = []) -> None:
        self.name = name
        self.children = children

class Graph:
    def __init__(self, nodes = []):
        self.nodes = nodes
    
    def add_nodes(self, pass_nodes):
        for node in pass_nodes:
            self.nodes.append(node)
    
    def dfs(self, start_node, target_node):
        # potentially the O(n)
        # return True
        pass

    def bidirectional_bfs(self, start_node, end_node):
        # O(k^(d/2))
        if start_node == end_node:
            return True
        
        visited = set()

        queue_left = []
        queue_left.append(start_node)
        
        queue_right = []
        queue_right.append(end_node)
        
        left_element = start_node
        right_element = end_node
        while len(queue_left) != 0 or len(queue_right) != 0:

            neighbors_left = left_element.children
            neighbors_right = right_element.children
            
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
    

class BinaryNode:
    def __init__(self, name = "", left = None, right = None) -> None:
        self.name = name
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self, root = None) -> None:
        self.root = root

    def in_order_traversal(self, element):
        nodes_list = []
        self.traverse_inorder(nodes_list)
        
        i = 0
        while element != current_element:
            current_element = nodes_list[i]
            i += 1

        return nodes_list[i + 1]
    
    def traverse_inorder(self, nodes_list):
        if self.left != None:
            self.left.in_order_traversal(nodes_list)
        
        nodes_list.append(self)

        if self.right != None:
            self.right.in_order_traversal()
        