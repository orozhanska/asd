class KseStack:
    def __init__(self):
        self._stack = []
        
    def push(self, data):
        self._stack.append(data)
    
    def pop(self):
        if not self.is_empty():
            last = self.peak() 
            self._stack.pop()   
            return last         
        else:
            return "Stack is empty"

    def size(self):
        return len(self._stack)
    
    def peak(self):
        if not self.is_empty():
            return self._stack[-1]
        else:
            return "Stack is empty"

    def is_empty(self):
        return self.size() == 0

    def __str__(self):
        res = "Our stack is here ->> ["
        if self._stack:
            res += ", ".join(str(x) for x in self._stack)
        res += "]"
        return res

stack = KseStack()

stack.push("Olesia")
stack.push("George")
stack.push("Me")

print(stack.is_empty())  
print(stack.pop())       
print(stack.size())     
print(stack.peak())
print(stack)      
stack.push(KseStack())