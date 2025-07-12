class Node:
    def __init__(self, data):
        self.data = data
        self.next = self.prev = None

class QueueDLL:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        new_node.prev = self.rear
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if not self.is_empty():
            temp = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            else:
                self.front.prev = None
            return temp
        else:
            raise Exception("Queue is empty")
        
    def peek(self):
        if not self.is_empty():
            return self.front.data
        else:
            raise Exception("Queue is empty")
        
    def size(self):
        count = 0
        temp = self.front
        while temp:
            count += 1
            temp = temp.next
        return count
    
    def clear(self):
        self.front = self.rear = None
        print("Queue cleared")

    def __str__(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            elements = []
            temp = self.front
            while temp:
                elements.append(temp.data)
                temp = temp.next
            return "Queue: " + " <-> ".join(map(str, elements))
        
# Example usage:
if __name__ == "__main__":
    queue = QueueDLL()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)  # Output: Queue: 1 <-> 2 <-> 3
    print("dequeued: ",queue.dequeue())  # Output: 1
    print(queue)  # Output: Queue: 2 <-> 3
    print("front element: ",queue.peek())  # Output: 2
    print("queue size: ",queue.size())  # Output: 2
    queue.clear()  # Output: Queue cleared
    print(queue)  # Output: Queue is empty