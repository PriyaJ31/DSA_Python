class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top=0
        self.head = None
        self.size = 0

    def push(self, data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        self.size+=1

    def pop(self):
        if not self.empty():
            popped_data=self.head.data
            self.head=self.head.next
            self.size-=1
            return popped_data
        else:
            raise IndexError("Pop from empty stack")
        
    def peek(self):
        if not self.empty():
            return self.head.data
        else:
            raise IndexError("Peek from empty stack")
        
    def empty(self):
        return self.size == 0
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        temp=self.head
        stack= []
        while temp:
            stack.append(str(temp.data))
            temp= temp.next
        return "["+", ".join(stack)+"]"
    
# Example usage
if __name__ == "__main__":
    stack = StackLinkedList()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stack after pushing 1, 2, 3:", stack)
    print("Top element:", stack.peek())
    print("Popped element:", stack.pop())
    print("Stack after popping:", stack)
    print("Is stack empty?", stack.empty())
    print("Stack size:", len(stack))
    stack.pop()
    print("Stack after popping:", stack)
    print("Is stack empty?", stack.empty())
    stack.pop()
    print("Stack after popping:", stack)
    print("Is stack empty?", stack.empty())
    stack.pop()  # This will raise an IndexError