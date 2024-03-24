class Node:
    def __init__(self, prev = None, next = None, value = None) -> None:
        self.prev = prev
        self.next = next
        self.value = value

class LinkedList:
    def __init__(self, head = None, tail = None) -> None:
        self.head = head
        self.tail = tail
    
    def ross_func(self):
        # node is first node of list
        ptr = self.head
        # ptr is another node used as a pointer

        while (ptr != None):
            tempPtr = ptr

            while(tempPtr != None and tempPtr.next != None):
                if (tempPtr.next.value == ptr.value):
                    tempPtr.next = tempPtr.next.next
                else:
                    tempPtr = tempPtr.next

            ptr = ptr.next

    def ryans_func(self):
        # 0, 1 0
        # p1p2
        p1 = self.head
        p2 = self.head
        while (True):
            # print(f"outter loop: p1.value: {p1.value}, p2.value {p2.value}, p2.next.value: {p2.next.value}")
            # 0, 1, None
            # p1, , p2,
            while (p2 != None and p2.next != None):
                # print(f"inner loop: p1.value: {p1.value}, p2.value {p2.value}, p2.next.value: {p2.next.value}")
                
                if (p1.value == p2.next.value):
                    p2.next = p2.next.next
                
                p2 = p2.next
            p1 = p1.next
            p2 = p1
            if (p1 != None or p1.next != None):
                break

    # using mergesort
    # slow n^2
    def remove_dups_no_space(self):
        count = 0
        current_node = self.head
        while (current_node != None):
            if self.is_dups_starting_at(count, current_node.value):
                print("is dup")
                print(f"current_node.value: {current_node.value}")
                if current_node.prev == None: 
                    current_node = current_node.next
                else: 
                    current_node.prev.next = current_node.next
            current_node = current_node.next
            count += 1
        return self.head
    
    def is_dups_starting_at(self, count, value):
        value_to_check = value
        current_node = self.head
        i = 0
        while (i < count):
            current_node = current_node.next
            i += 1
        
        while current_node != None:
            if current_node.value == value_to_check:
                return True
            current_node = current_node.next
        return False 
    
    # if we assume the value of each linked list is an ascii char 
    def remove_dups_ascii(self):
        ascii_list = [None]*377

        current_node = self.head
        while (current_node != None):
            if ascii_list[ord(current_node.value)] != None:
                # delete current node using previous node
                current_node.prev.next = current_node.next
            else: 
                ascii_list[ord(current_node.value)] = True
            current_node = current_node.next
        return self.head
    

    # if we can change the order of the elements we can use sort (binary sort)
    # to sort the array and then remove those items that are duplicates
    # O(n log n) time complexity
    def remove_dups_binary_sort(self):
        sorted_list = merge_sort_linked_list(self)


    def merge_sort_linked_list(self):
        current_node = self.head
        
        r_partition = Node(None, None, None)
        r_partition_head = r_partition
        right_list = LinkedList(r_partition_head, r_partition)

        l_partition = Node(None, None, None)
        l_partition_head = l_partition
        left_list = LinkedList(l_partition_head, l_partition)
        
        # choosing partition as head is not optimal time complexity, 
        # we normally want to get three nodes at random and choose the median value
        while current_node != None:
            # using the objects location in memory
            if r_partition.value == None: 
                r_partition.value = current_node.value
            elif current_node >= r_partition:
                r_partition.next = Node(r_partition, None, current_node.value)
                r_partition = r_partition.next
            elif l_partition.value == None:
                l_partition.value = current_node.value
            else:
                l_partition.next = Node(l_partition, None, current_node.value)
                l_partition = l_partition.next
            
            current_node = current_node.next
        left_list.merge_sort_linked_list()
        right_list.merge_sort_linked_list()

        left_list.union_linked_lists(right_list)
        
    def union_linked_lists(self, right_list):
        left_head = self.head


    # if we can include more space complexity
    # if singly linked list
    def remove_dups(self):
        current_node = self.head
        h = {}
        while (current_node != None):
            if current_node.value in h:
                # delete current node using previous node
                current_node.prev.next = current_node.next
                if current_node.next != None: 
                    current_node.next.prev = current_node
            else: 
                h[current_node.value] = True
            current_node = current_node.next
        return self.head
    
    def get_kth_to_last_val(self, k):
        current_node = self.head
        trailing_node = None
        while current_node != None:
            if k <= 0:
                if trailing_node == None: 
                    trailing_node = self.head
                else: 
                    trailing_node = trailing_node.next
            
            k -= 1
            current_node = current_node.next

        return trailing_node.value
    
    def delete_middle_node(self):
        current_node = self.head
        trailing_node = self.head
        second_trailing_node = None
        counter = 0
        while current_node != None:
            if counter % 2 == 0:
                second_trailing_node = trailing_node
                trailing_node = trailing_node.next
            current_node = current_node.next
            counter += 1
        
        if counter <= 2: 
            return
        
        print(f"trailing_node.value {trailing_node.value}")
        second_trailing_node.next = second_trailing_node.next.next
        
    def partition(self, val):
        current_node = self.head
        left_head = None
        left_tail = None
        right_head = None
        right_tail = None
        while current_node != None:
            if current_node.value < val and left_head == None:
                left_head = Node(None, None, current_node.value)
                left_head = left_tail
            elif current_node.value < val:
                left_tail.next = Node(left_tail, None, current_node.value)
                left_tail = left_tail.next
            
            if current_node.value >= val and right_head == None:
                right_head = Node(None, None, current_node.value)
                right_tail = right_head
            elif current_node.value >= val:
                right_tail.next = Node(right_tail, None, current_node.value)
                right_tail = right_tail.next

            current_node = current_node.next
        if right_head == None: 
            union_list = LinkedList(left_head, left_tail)
        elif left_head == None: 
            union_list = LinkedList(right_head, right_tail)
        else:
            left_tail.next = right_head
            union_list = LinkedList(right_head, left_tail)
        return union_list
    

    def sum_lists_forward(self, second_head):
        current_node = self.head
        total_1 = 0
        exp = 0
        while current_node != None:
            print(f'current_node.value: {current_node.value}')
            total_1 *= 10
            total_1 += current_node.value
            exp += 1
            current_node = current_node.next
        print(f"total_1: {total_1}")
        total_2 = 0
        exp = 0
        current_node = second_head.head
        while current_node != None: 
            total_2 *= 10
            total_2 += current_node.value
            exp += 1
            current_node = current_node.next
        print(f"total_2: {total_2}")
        
        new_node = Node(None, None, 0)
        current_node = new_node
        total_1 += total_2
        print(f"total_1: {total_1}")
        total_str = str(total_1)
        i = 0
        while i < len(total_str):
            digit = total_str[i]
            
            current_node.value = int(digit)
            if i == len(total_str) - 1:
                temp_node = None
            else: 
                temp_node = Node(current_node, None, 0)
            current_node.next = temp_node
            current_node = current_node.next
            i += 1

        return LinkedList(new_node, current_node)
    
    def sum_lists_backward(self, second_head):
        current_node = self.head
        total_1 = 0
        exp = 0
        while current_node != None:
            print(f'current_node.value: {current_node.value}')
            total_1 += current_node.value * (10 ** exp)
            exp += 1
            current_node = current_node.next
        print(f"total_1: {total_1}")
        total_2 = 0
        exp = 0
        current_node = second_head.head
        while current_node != None: 
            total_2 += current_node.value * (10 ** exp)
            exp += 1
            current_node = current_node.next
        print(f"total_2: {total_2}")
        
        new_node = Node(None, None, 0)
        current_node = new_node
        total_1 += total_2
        print(f"total_1: {total_1}")
        while total_1 > 0:
            digit = total_1 % 10
            total_1 //= 10
            current_node.value = digit
            if total_1 == 0: 
                temp_node = None
            else: 
                temp_node = Node(current_node, None, 0)
            current_node.next = temp_node
            current_node = current_node.next

        return LinkedList(new_node, current_node)
    
    def is_palindrome_simple(self):
        current_node = self.head
        
        test_str = ""
        while current_node != None:
            test_str += current_node.value
            current_node = current_node.next
        
        i = 0
        while i < len(test_str):
            if test_str[i] != test_str[-i - 1]:
                return False
            i += 1
        return True
    def is_intersecting(self, l2):
        list1 = self.head
        list2 = l2.head
        s = set()
        while list1 != None: 
            s.add(list1)
            list1 = list1.next

        while list2 != None: 
            if list2 in s:
                return list2
            list2 = list2.next
        return None
    
    def loop_detection(self):
        s = set()
        current_node = self.head
        while current_node != None:
            if current_node in s:
                return current_node
            else: 
                s.add(current_node)
            current_node = current_node.next
        return None
        
    def __str__(self) -> str:
        s = ""
        current_node = self.head
        while current_node != None: 
            s += str(current_node.value)
            current_node = current_node.next
            s+= ", "
        
        return s


node0 = Node(None, None, 0)
node1 = Node(node0, None, 1)
node_dup = Node(node1, None, 0)
node0.next = node1
node1.prev = node0
node1.next = node_dup
node_dup.prev = node1
test_link = LinkedList(node0, node_dup)

print(f"test_link 0: {test_link}")
test_link.remove_dups()
print(f"test_link 1: {test_link}")



node0 = Node(None, None, "0")
node1 = Node(node0, None, "1")
node_dup = Node(node1, None, "0")
node0.next = node1
node1.prev = node0
node1.next = node_dup
node_dup.prev = node1
test_link = LinkedList(node0, node_dup)
print(f"test_link 2: {test_link}")
test_link.remove_dups_ascii()
print(f"test_link 3: {test_link}")


node0 = Node(None, None, "0")
node1 = Node(node0, None, "1")
node_dup = Node(node1, None, "0")
node0.next = node1
node1.prev = node0
node1.next = node_dup
node_dup.prev = node1
test_link = LinkedList(node0, node_dup)
print(f"test_link 4: {test_link}")
test_link.remove_dups_no_space()
print(f"test_link 5: {test_link}")


# RYANS CODE
# print("RYANS CODE")
# node0 = Node(None, None, "0")
# node1 = Node(node0, None, "1")
# node_dup = Node(node1, None, "0")
# node2 = Node(None, None, "2")
# node_dup2 = Node(None, None, "0")

# node0.next = node1
# # node1.prev = node0
# node1.next = node_dup
# node_dup.next = node2
# node2.next = node_dup2


# test_link = LinkedList(node0, node_dup2)
# print(f"test_link 6: {test_link}")
# test_link.ryans_func()
# print(f"test_link 7: {test_link}")

# ROSS CODE: 
# print("ROSS CODE")
# node0 = Node(None, None, "0")
# node1 = Node(node0, None, "1")
# node_dup = Node(node1, None, "0")
# node2 = Node(None, None, "2")
# node_dup2 = Node(None, None, "0")

# node0.next = node1
# # node1.prev = node0
# node1.next = node_dup
# node_dup.next = node2
# node2.next = node_dup2


# test_link = LinkedList(node0, node_dup2)
# print(f"test_link 6: {test_link}")
# test_link.ross_func()
# print(f"test_link 7: {test_link}")




print("QUESTION 2.2")
node0 = Node(None, None, "0")
node1 = Node(node0, None, "1")
node_dup = Node(node1, None, "2")
node2 = Node(None, None, "3")
node_dup2 = Node(None, None, "4")

node0.next = node1
# node1.prev = node0
node1.next = node_dup
node_dup.next = node2
node2.next = node_dup2


test_link = LinkedList(node0, node_dup2)

print(f"test_link 2.2: {test_link}")
print(f"{test_link.get_kth_to_last_val(2)} == 2")
print(f"{test_link.get_kth_to_last_val(1)} == 3")
print(f"{test_link.get_kth_to_last_val(0)} == 4")
print("")
print("QUESTION 2.3 delete middle node")
print(f"{test_link}")
test_link.delete_middle_node()
print(f"{test_link}")
print("QUESTION 2.3 delete middle node")
print(f"{test_link}")
test_link.delete_middle_node()
print(f"{test_link}")
test_link.delete_middle_node()
print(f"{test_link}")
test_link.delete_middle_node()
print(f"{test_link}")

print("QUESTION 2.4 partition")
# Partition: 
# Write code to partition a linked list around 
# a value x, such that all nodes less than x 
# come before all nodes greater than or equal to
# x. If x is contained within the list, the 
# values of x only need to be after the elements 
# less than x (see below). The partition element 
# x can appear anywhere in the "right partition"; 
# it does not need to appear between the left and right partitions.
# EXAMPLE
# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1[partition=5] 
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
# Hints: #3, #24

node0 = Node(None, None, 3)
node1 = Node(node0, None, 5)
node2 = Node(node1, None, 8)
node3 = Node(node2, None, 5)
node4 = Node(node3, None, 10)
node5 = Node(node4, None, 2)
node6 = Node(node5, None, 1)

node0.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

test_list = LinkedList(node0, node6)
test_list.partition(5)

print(f"test_list: {test_list}")

print("")
print(f"TEST: sum_list, forwards")
node0 = Node(None, None, 3)
node1 = Node(node0, None, 5)
node2 = Node(node1, None, 8)
print("853")

node3 = Node(None, None, 5)
node4 = Node(node3, None, 1)
node5 = Node(node4, None, 2)
node6 = Node(node5, None, 1)
print("1215")

node0.next = node1
node1.next = node2

node3.next = node4
node4.next = node5
node5.next = node6


test_list_1 = LinkedList(node0, node2)
test_list_2 = LinkedList(node3, node6)
print(f"test_list.sum_lists_backward(test_list_2) {test_list_1.sum_lists_backward(test_list_2)}")
print(f"test_list.sum_lists_forward(test_list_2) {test_list_1.sum_lists_forward(test_list_2)}")

# print(f'test_list: {test_list}')

print("QUESTION 2.6 is_palindrome_simple: ")
node0 = Node(None, None, "")
node_a0 = Node(None, None, "a")
node_b1 = Node(None, None, "b")
node_a2 = Node(None, None, "a")
node_a0.next = node_b1
node_b1.next = node_a2

node_a3 = Node(None, None, "a")
node_b4 = Node(None, None, "b")
node_a3.next = node_b4



print(f"word: {node0}; {LinkedList(node0).is_palindrome_simple()}")
print(f"word: {LinkedList(node_a0, node_a2)}; {LinkedList(node_a0, node_a2).is_palindrome_simple()}")
print(f"word: {LinkedList(node_a3, node_b4)}; {LinkedList(node_a3, node_b4).is_palindrome_simple()}")

print("QUESTION 2.7 Intersection")
print("Given two (singly) linked lists, determine if the two lists intersect.")
print("Return the intersecting node. Note that the intersection is defined ")
print("based on reference, not value.That is, if the kth node of the first ")
print("linked list is the exact same node (by reference) as the jth node of ")
print("the second linked list, then they are intersecting.")

node_b4.next = node_a2
list_1 = LinkedList(node_a0, node_a2)
list_2 = LinkedList(node_a3, node_a2)
print(f"node0.is_intersecting(node_a3): {list_1.is_intersecting(list_2)}")
print("")
print("")


print("QUESTION 2.8 Loop Detection")
print("Given a circular linked list, implement an algorithm that returns the node at the")
print("beginning of the loop.")
print("DEFINITION")
print("Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so as to make a loop in the linked list.")
print("EXAMPLE")
print("Input: A -> B -> C -> D -> E -> C[thesameCasearlier]")
print("Output: C")

node0 = Node(None, None, 'a')
node1 = Node(None, None, 'b')
node2 = Node(None, None, 'c')
node0.next = node1
node1.next = node2
node2.next = node0
test_0 = LinkedList(node0, node2)
print(test_0.loop_detection())