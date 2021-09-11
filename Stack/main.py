#define a stack
class StackExample():
    def __init__(self):
        #assign it to an empty list
        self.items = []
    
    #define the push method
    def push(self, items):
        self.items.append(items)
    
    #define the pop method
    def pop(self):
        return self.items.pop()
    
    #check if list is empty
    def is_empty(self):
        return self.items == []
    
    #return the list
    def get_stack(self):
        return self.items
    
    #define peek method (1st item from the rear)
    def peek(self):
        if self.is_empty() == False:
            return self.items[-1]

#example = StackExample()
""" example.push(7)
example.push("two")
example.push("three")
print(example.get_stack())
example.pop()
print(example.get_stack())
print(example.is_empty())
print(example.peek()) """