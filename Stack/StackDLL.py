class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class StackDoblyLinkedList:
    def __init__(self):
        self.top=None
        self.size=0
        self.head=None

    def push(self, data):
        new_node=Node(data)
        if self.top is None:
            self.top = self.head = new_node
        else:
            new_node.prev = self.top
            self.top.next = new_node
            self.top = new_node
        self.size += 1

    def pop(self):
        if not self.empty():
            popped_data = self.top.data
            if self.top.prev is None:
                self.top = self.head = None # Reset both if stack becomes empty
            else:
                self.top=self.top.prev
                self.top.next = None
            self.size -= 1
            return popped_data
        else:
            raise IndexError("Pop from empty stack")
    
    def peek(self):
        if not self.empty():
            return self.top.data
        else:
            raise IndexError("Peek from empty stack")
        
    def empty(self):
        return self.size == 0
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        temp = self.head
        stack = []
        while temp:
            stack.append(str(temp.data))
            temp = temp.next
        return "[" + ", ".join(stack) + "]"
    
# Example usage
if __name__ == "__main__":
    stack = StackDoblyLinkedList()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stack after pushing 1, 2, 3:", stack)
    print("Top element:", stack.peek())
    print("Popped element:", stack.pop())
    print("Stack after popping:", stack)
    print("Is stack empty?", stack.empty())
    print("Stack size:", len(stack))