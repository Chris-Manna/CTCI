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
        self.next = None

class MyStack:
    def __init__(self):
        self.top = None
        self.min_list = []

    def pop(self):
        if self.top is None:
            raise EmptyStackException("Stack is empty")
        item = self.top.data
        if len(self.min_list) == 0: 
            raise EmptyStackException("Stack is empty")
        if item == self.min_list[-1]:
            self.min_list.pop()
        self.top = self.top.next
        return item

    def push(self, item):
        t = StackNode(item)
        if len(self.min_list) == 0 or t.data < self.min_list[-1].data:
            self.min_list.append(t)
        t.next = self.top
        self.top = t

    def peek(self):
        if self.top is None:
            raise EmptyStackException("Stack is empty")
        return self.top.data
    
    def min(self):
        if len(self.min_list) == 0:
            raise EmptyStackException("Stack is empty")
        return self.min_list[-1].data

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