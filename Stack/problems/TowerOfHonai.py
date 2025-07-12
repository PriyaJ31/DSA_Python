def push(stack,item):
    stack.append(item)

def pop(stack):
    if is_empty(stack):
        return None
    return stack.pop()

def peek(stack):
    if is_empty(stack):
        return None
    return stack[-1]

def is_empty(stack):
    return len(stack) == 0

def hanoi(n, src, target, aux, rods):
    if n==1:
        item= pop(rods[src])
        push(rods[target], item)
        print("Move disk", item, "from", rods[src], "to", rods[target],"\n")
    else:
        hanoi(n-1,src, aux, target, rods)
        hanoi(1, src, target, aux, rods)
        hanoi(n-1, aux, target, src, rods)

def print_rods(rods):
   print("A:", rods["A"])
   print("B:", rods["B"])
   print("C:", rods["C"])
   print('='*40)

def tower_of_hanoi(n):
    rods={
        "A": list(reversed(range(1, n + 1))),
        "B": [],
        "C": []
    }
    print("Initial state:")
    print("A:", rods["A"])
    print("B:", rods["B"])
    print("C:", rods["C"])
    hanoi(n, "A", "C", "B", rods)
    print("Final state:")
    print_rods(rods)

if __name__ == "__main__":
    n = int(input("Enter the number of disks: "))
    tower_of_hanoi(n)
