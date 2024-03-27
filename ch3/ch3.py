# class Stack:
#     class StackNode:
#         self.data
#         self.next
#         class StackNode(self, data):
#             self.data = data
#         private StackNode<T> top
#         public T pop():
#             if (top == null) throw new EmptystackException()
#             T item = top.data

print("QUESTION 3.1 Three in One")
print("Describe how you could use a single array to implement three stacks.")
# use an iterator to dynamically point to the bottom of the stack and move the stacks around inside an array

print("QUESTION 3.2 Stack Min: ")
print("How would you design a stack which, ")
print("in addition to push and pop, has a function min ")
print("which returns the minimum element? Push, pop and ")
print("min should all operate in 0(1) time.")
# if we can keep the same stack

class EmptyStackException(Exception):
    pass

class StackNode:
    def __init__(self, data):
        self.data = data
        self.min_val = None
        self.next = None

class MyStack:
    def __init__(self):
        self.top = None

    def pop(self):
        if self.top is None:
            raise EmptyStackException("Stack is empty")
        item = self.top.data
        self.top = self.top.next
        return item

    def push(self, item): 
        # stack = []

        # # first = {min_val: None, data: 0, next: None}
        # stack = [first]
        # first = {min_val: 0, data: 0, next: None}
        # second = {min_val: None, data: 1, next: None}
        # stack = [first]
        # first.min_val < second.data:
        # 0 < 1
        # stack = [
        #     (first) {min_val: 0, data: 0, next: None},
        #     (second) {min_val: 0, data: 1, next: first}
        # ]
        # stack = [first, second]

        # third = {min_val: None, data: -1, next: None}
        # third.min_val < second.min_val
        # third.min_val = -1
        # stack = [
        #     (first) {min_val: 0, data: 0, next: None},
        #     (second) {min_val: 0, data: 1, next: first}
        #     (third) {min_val: -1, data: -1, next: second}
        # ]



        t = StackNode(item)

        # print(f"self.top: {self.top}; t.data: {t.data}")
        t.next = self.top
        
        if self.top == None: # nothing in the stack yet
            t.min_val = t.data
        
        elif self.top.min_val < t.data:
            # check top before assigning val
            t.min_val = self.top.min_val
        else: 
            t.min_val = t.data
        
        self.top = t

    def peek(self):
        if self.top is None:
            raise EmptyStackException("Stack is empty")
        return self.top.data
    
    def min(self):
        if self.top is None:
            raise EmptyStackException("Stack is empty")
        return self.top.min_val

    def is_empty(self):
        return self.top is None
    
    def __str__(self) -> str:
        s = ""
        if self.top is None: 
            return ""
        
        new_stack  = MyStack()
        
        while self.top != None:
            new_stack.push(self.pop())
        
        while new_stack.top != None: 
            element = new_stack.pop()
            s += str(element) + ", "
            self.push(element)
        return s
    

class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, item):
        t = QueueNode(item)
        if self.last is not None:
            self.last.next = t
        self.last = t
        if self.first is None:
            self.first = self.last

    def remove(self):
        if self.first is None:
            raise Exception("Queue is empty")
        data = self.first.data
        self.first = self.first.next
        if self.first is None:
            self.last = None
        return data

    def peek(self):
        if self.first is None:
            raise Exception("Queue is empty")
        return self.first.data

    def is_empty(self):
        return self.first is None


print("QUESTION 3.3")
# class SetOfStacks:
#     #  start a new stack when the previous stack exceeds some threshold
#     def __init__(self):
#         self.top = None
#         self.THRESHOLD = 10
#         self.capacity = 0
#         self.previous_stack = None
#         self.stack_count = 0
#     def pop(self):
#         sub_stack = self
    
#         while sub_stack.previous_stack != None:
#             sub_stack = sub_stack.previous_stack
    
#         if sub_stack.top is None:
#             if sub_stack.capacity == 0 and sub_stack.previous_stack != None: 
#                 sub_stack = sub_stack.previous_stack
#                 item = sub_stack.top.data
#                 sub_stack.top = sub_stack.top.next
#                 sub_stack.capacity -= 1
#                 # return item
#                 sub_stack = None
#             else:
#                 raise EmptyStackException("Stack is empty")
#         else:
#             item = sub_stack.top.data
#             sub_stack.top = sub_stack.top.next
#             sub_stack.capacity -= 1
#         return item
#     def push(self, item):
#         t = StackNode(item)
#         t.next = self.top
#         # print(f"item: {item}, self.top: {self.top}")
#         # met and exceeds the stack threshold
#         if self.capacity == self.THRESHOLD: 
#             # print(f'inside conditional: item: {item}, self.top: {self.top.data}')
            
#             new_stack = SetOfStacks()
#             new_stack.previous_stack = self
#             new_stack.stack_count = 1 + self.stack_count
#             self = new_stack
#         self.capacity += 1
#         self.top = t
#         # print(f"1 self.stack_count: {self.stack_count}; self.top.data: {self.top.data}")
#     def peek(self):
#         if self.top is None:
#             raise EmptyStackException("Stack is empty")
#         return self.top.data
#     def is_empty(self):
#         return self.top is None
#     def __str__(self) -> str:
#         s = ""
#         if self.top is None: 
#             return ""

#         new_stack  = SetOfStacks()        
#         while self.top != None:
#             new_stack.push(self.pop())
    
#         while new_stack.top != None: 
#             element = new_stack.pop()
#             s += str(element) + ", "
#             self.push(element)
#         return s

class SetOfStacksLists:
    def __init__(self):
        self.lists = [list()]
        self.top = None
        self.THRESHOLD = 10

    def push(self, item):
        if len(self.lists) == 0:
            self.lists.append([])
        
        list_index = len(self.lists) - 1
        if len(self.lists[list_index]) >= self.THRESHOLD:
            self.lists.append([])
        
        list_index = len(self.lists) - 1
        self.lists[list_index].append(item)
    
    def pop(self):        
        # no lists
        if len(self.lists) == 0 or len(self.lists[0]) == 0:
            raise EmptyStackException("Stack is empty")
        
        list_index = len(self.lists) - 1
        if len(self.lists[list_index]) == 0:
            self.lists[list_index].pop()
            self.pop()
        else: 
            item = self.lists[list_index].pop()
            return item
    
    def pop_at(self, list_index):
        # no lists
        if len(self.lists) == 0 or len(self.lists[0]) == 0 or list_index > len(self.lists) - 1:
            raise EmptyStackException("Stack is empty")
        
        if len(self.lists[list_index]) == 0:
            self.lists[list_index].pop(list_index)
            self.pop_at(list_index)
        else:
            item = self.lists[list_index].pop()
            return item
    def peek(self):
        list_index = len(self.lists) - 1
        if list_index == -1 or len(self.lists[list_index]) == 0:
            raise EmptyStackException("Stack is empty")
        return self.lists[list_index][-1]

    def __str__(self) -> str:
        s = ""
        for l in self.lists:
            s += f"{l}"
        
        return s