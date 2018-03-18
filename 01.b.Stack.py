class Stack:
    def __init__(self, size):
        self.size = size
        self.top = -1
        self.arr = [0] * size
    def push(self, element):
        if self.top == self.size - 1:
            print("Overflow")
        else:
            self.top += 1
            self.arr[self.top] = element
    def pop(self):
        if self.top == -1:
            print("Underflow")
        else:
            print("Popped:", self.arr[self.top])
            self.top -= 1
    def display(self):
        if self.top == -1:
            print("Stack empty")
        else:
            for i in range(self.top + 1):
                print(self.arr[self.top - i], sep = " ")

if __name__ == '__main__':
    n = int(input("Enter size of stack: "))
    stk = Stack(n)
    print("1. Push\n2. Pop\n3. Display\n4. Exit")
    while(True):
        ch = int(input("Enter choice: "))
        if ch == 1:
            emt = int(input("Enter element to push: "))
            stk.push(emt)
        elif ch == 2:
            stk.pop()
        elif ch == 3:
            stk.display()
        elif ch == 4:
             break
        else:
            pass
