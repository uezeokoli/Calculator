# author: Ugonna Ezeokoli
# date: March 2, 2023
# file: stack.py is a Python program that implements an abstract data type, stack
# input: creates the Stack object
# output: returns certain type of data like, list, int, or float based on function called

class Stack:

    def __init__(self):         #initializes list the belongs to stack object
        self.list = []    
    def isEmpty(self):          # Returns true if list is empty
        return len(self.list) == 0      
    def push(self, item):           #Adds a new item to end of object list 
        self.list.append(item)      
    def pop(self):          # removes item from end of object list and returns the value of item removed
        popped_val = self.list[-1]  
        self.list.pop()
        return popped_val
    def peek(self):         # returns the value of last item in object list
        if self.isEmpty():
            return None
        return self.list[-1]
    def size(self):         # returns the number of items in object list
        return len(self.list)
    
if __name__ == '__main__':
    
    data_in = ['hello', 'how', 'are', 'you']
    s = Stack()
    for i in data_in:
        s.push(i)
           
    assert s.size() == len(data_in)
    assert s.peek() == data_in[-1]
    data_out = []
    while not s.isEmpty():
        data_out.append(s.pop())
    assert data_out == data_in[::-1]
    assert s.size() == 0
    assert s.peek() == None