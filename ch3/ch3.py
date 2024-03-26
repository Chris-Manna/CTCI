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
