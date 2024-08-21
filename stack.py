class Stack:
    def __init__(self):
        self.stack = []
 
    def push(self,item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from empty stack")
    
    def top(self):
        if not self.is_empty():
            return self.stack[-1]

    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return len(self.stack) == 0

stack = Stack()
stack.push(3)
stack.push(4)

print("弹出元素：", stack.pop())
print("查看栈顶元素：", stack.top())
print("栈大小：", stack.size())
print("栈是否为空：", stack.is_empty())