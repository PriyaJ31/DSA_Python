class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class QueueSLL:
    def __init__(self):
        self.front= self.rear = None

    def is_empty(self):
        return self.front is None
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
    
    def dequeue(self):
        if not self.is_empty():
            temp=self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
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
            return "Queue: " + " -> ".join(map(str, elements))
        
# Example usage:
if __name__ == "__main__":
    queue = QueueSLL()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(queue)  # Output: Queue: 10 -> 20 -> 30
    print("Front element:", queue.peek())  # Output: Front element: 10
    print("Queue size:", queue.size())  # Output: Queue size: 3
    print("Dequeue:", queue.dequeue())  # Output: Dequeue: 10
    print(queue)  # Output: Queue: 20 -> 30
    queue.clear()  # Output: Queue cleared
    print(queue)  # Output: Queue is empty
