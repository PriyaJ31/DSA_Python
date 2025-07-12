class StackArray:
    def __init__(self):
        self.stack = []
        self.size = 0 
        self.top = -1 # this can be used to track the top element

    def push(self, data):
        self.stack.append(data)
        self.size += 1
        self.top += 1 # update the top index

    def pop(self):
        if not self.empty():
            self.size-=1
            self.top -= 1
            return self.stack.pop()
        else:
            raise IndexError("Pop from empty stack")
        
    def peek(self):
        if not self.empty():
            return self.stack[-1] # Return the last element without removing it
        else:
            raise IndexError("Peek from empty stack")

    def empty(self):
        return self.size == 0

    def __len__(self):
        return self.size
    
    def __str__(self):
        return "["+", ".join(str(i) for i in self.stack)+"]"
    
# Example usage
if __name__ == "__main__":
    stack = StackArray()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stack after pushing 1, 2, 3:", stack)
    print("Top element:", stack.peek())
    print("Popped element:", stack.pop())
    print("Stack after popping:", stack)
    print("Is stack empty?", stack.empty())
    print("Stack size:", len(stack))
