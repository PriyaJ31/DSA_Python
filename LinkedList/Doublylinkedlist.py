class Node:
    def __init__(self, data):
        self.data = data
        self.next = self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def insert_at_beginning(self, data):
        new_node=Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self.size += 1

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
        else:
            self.head = new_node
        self.tail = new_node
        self.size += 1

    def insert_at_pos(self, data, pos):
        if pos < 0 or pos > self.size:
            raise IndexError("Index out of bounds")
        if pos == 0:
            self.insert_at_beginning(data)
        elif pos == self.size:
            self.insert_at_end(data)
        else:
            new_node = Node(data)
            temp = self.head
            for _ in range(pos):
                temp = temp.next
            prev_node = temp.prev
            new_node.prev = prev_node
            new_node.next = temp
            prev_node.next = new_node
            temp.prev = new_node
            self.size += 1

    def delete_at_beginning(self):
        if self.head is None:
            raise IndexError("List is empty")
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1

    def delete_at_end(self):
        if self.tail is None:
            raise IndexError("List is empty")
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1

    def delete_at_pos(self, pos):
        if pos < 0 or pos >= self.size:
            raise IndexError("Index out of bounds")
        if pos == 0:
            self.delete_at_beginning()
        elif pos == self.size - 1:
            self.delete_at_end()
        else:
            temp = self.head
            for _ in range(pos):
                temp = temp.next
            prev_node = temp.prev
            next_node = temp.next
            prev_node.next = next_node
            next_node.prev = prev_node
            self.size -= 1

    def delete_by_value(self, value):
        temp = self.head
        while temp:
            if temp.data == value:
                if temp == self.head:
                    self.delete_at_beginning()
                elif temp == self.tail:
                    self.delete_at_end()
                else:
                    prev_node = temp.prev
                    next_node = temp.next
                    prev_node.next = next_node
                    next_node.prev = prev_node
                    self.size -= 1
                return
            temp = temp.next
        raise ValueError("Value not found in the list")
    
    def search(self, value):
        temp = self.head
        index= 0
        while temp:
            if temp.data == value:
                return index
            index += 1
            temp = temp.next
        return -1
    
    def __len__(self):
        return self.size
    
    def printForward(self):
        temp = self.head
        res=[]
        while temp:
            res.append(str(temp.data))
            temp = temp.next
        return " <-> ".join(res)+" <-> None"
    
    def printBackward(self):
        temp = self.tail
        res=[]
        while temp:
            res.append(str(temp.data))
            temp = temp.prev
        return "None <-> "+" <-> ".join(res)

# Example usage
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_beginning(10)
    dll.insert_at_end(20)
    dll.insert_at_pos(15, 1)
    print("Forward:", dll.printForward())
    print("Backward:", dll.printBackward())
    
    dll.delete_at_beginning()
    print("After deleting at beginning:", dll.printForward())
    
    dll.delete_at_end()
    print("After deleting at end:", dll.printForward())
    
    dll.delete_at_pos(0)
    print("After deleting at position 0:", dll.printForward())
    
    dll.insert_at_end(30)
    dll.insert_at_end(40)
    print("After inserting 30 and 40 at end:", dll.printForward())
    
    print("Search for 30:", dll.search(30))
    print("Search for 50 (not present):", dll.search(50))
    
    try:
        dll.delete_by_value(40)
        print("After deleting value 40:", dll.printForward())
    except ValueError as e:
        print(e)
    
    try:
        dll.delete_by_value(50)  # This will raise an error
    except ValueError as e:
        print(e)