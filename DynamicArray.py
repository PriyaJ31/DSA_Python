import ctypes
class DynamicArray:
    def __init__(self):
        self.n=0 # number of elements
        self.capacity = 1 # initial capacity
        self.array=self._make_array(self.capacity)
    
    def _make_array(self, size):
        return (size * ctypes.py_object)()  # Create a new array of given capacity
    
    def __len__(self):
        return self.n
    
    def __getitem__(self, index):
        if 0<= index < self.n:
            return self.array[index]
        else:
            raise IndexError("Index out of bounds")
    
    def append(self, item):
        if self.n==self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.n] = item
        self.n += 1

    def _resize(self, new_capacity):
        new_array=self._make_array(new_capacity)
        for i in range(self.n):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def insert(self, index, elem):
        if index<0 or index > self.n:
            raise IndexError("Index out of bounds")
        if self.n==self.capacity:
            self._resize(2 * self.capacity)
        for i in range(self.n,index,-1):
            self.array[i] = self.array[i-1]
        self.array[index] = elem
        self.n += 1
    
    def delete(self,index):
        if index<0 or index >= self.n:
            raise IndexError("Index out of bounds")
        for i in range(index, self.n-1):
            self.array[i] = self.array[i+1]
        self.array[self.n-1] = None
        self.n -= 1

    def __str__(self):
        return "["+", ".join(str(self.array[i]) for i in range(self.n))+"]"
    
    # example usage
if __name__ == "__main__":
    arr = DynamicArray()

# append the new elements

arr.append(1)

arr.append(2)

arr.append(3)

# length of the given append in array

print(len(arr))
print(arr)
# access the given append in array

print(arr[1])

print(arr[2])

# remove the given the array

arr.delete(2)

# length of the array

print(len(arr))

# index of the array

print(arr[1])