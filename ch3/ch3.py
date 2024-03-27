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
        t = StackNode(item)
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
    
class QueueMadeOfStacks:
    def __init__(self) -> None:
        stack_1 = MyStack()
        stack_2 = MyStack()
        
    def add(self, item):
        pass

    def remove(self):
        pass

    def peek(self):
        pass

    def is_empty(self):
        pass

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
            if len(self.lists[list_index]) == 0:
                self.lists.pop(list_index)
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