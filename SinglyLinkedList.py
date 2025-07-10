class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SinglyLinkedList:
    def __init__(self):
        self.head=self.tail=None
        self.size=0

    def insert_at_beginning(self,data):
        new_node=Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self.size += 1
    
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail = new_node
        self.size += 1

    def insert_at_pos(self,data,pos):
        if pos<0 or pos>self.size:
            raise IndexError("Index out of bounds")
        if pos == 0:
            self.insert_at_beginning(data)
        elif pos == self.size:
            self.insert_at_end(data)
        else:
            new_node=Node(data)
            temp=self.head
            for _ in range(pos-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            self.size += 1

    def delete_at_beginning(self):
        if self.head is None:
            raise IndexError("List is empty")
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1

    def delete_at_end(self):
        if self.head is None:
            raise IndexError("List is empty")
        if self.head==self.tail:
            self.head = self.tail = None
        else:
            temp=self.head
            while temp.next != self.tail:
                temp = temp.next
            temp.next = None
            self.tail = temp
        self.size -= 1

    def delete_at_pos(self,pos):
        if pos<0 or pos>self.size-1:
            raise IndexError("Index out of bounds")
        if pos == 0:
            self.delete_at_beginning()
        elif pos == self.size - 1:
            self.delete_at_end()
        else:
            temp = self.head
            for _ in range(pos - 1):
                temp = temp.next
            temp.next = temp.next.next
            self.size -= 1
    
    def delete_by_value(self,data):
        if self.head is None:
            raise ValueError("List is empty")
        if self.head.data == data:
            self.delete_at_beginning()
            return
        temp = self.head
        while temp.next and temp.next.data != data:
            temp = temp.next
        if temp.next is None:
            raise ValueError("Value not found in the list")
        if temp.next == self.tail:
            self.tail = temp
        temp.next = temp.next.next
        self.size -= 1

    def search(self,data):
        temp = self.head
        index = 0
        while temp:
            if temp.data == data:
                return index
            temp = temp.next
            index += 1
        return -1
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        elements = []
        temp = self.head
        while temp:
            elements.append(str(temp.data))
            temp = temp.next
        return " -> ".join(elements)+"-> None"
    
    def reverse(self):
        prev = None
        current = self.head
        self.tail = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        print("Reversed List:", self)
    
    
# Example usage
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_at_beginning(10)
    sll.insert_at_end(20)
    sll.insert_at_pos(15, 1)
    print(sll)  # Output: 10 -> 15 -> 20 -> None
    sll.delete_at_beginning()
    print(sll)  # Output: 15 -> 20 -> None
    sll.delete_at_end()
    print(sll)  # Output: 15 -> None
    sll.insert_at_end(25)
    print(sll.search(25))  # Output: 1
    sll.delete_by_value(15)
    print(sll)  # Output: 25 -> None
    sll.insert_at_beginning(30)
    sll.insert_at_end(40)   
    print(sll)  # Output: 30 -> 25 -> 40 -> None
    sll.reverse()   

    