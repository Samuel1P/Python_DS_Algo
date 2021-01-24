class stack:
    def __init__(self):
        self.stack=[]

    def __len__(self):
        return len(self.stack)

    def stack_contents(self):
        return self.stack

    def is_empty(self):
        return len(self.stack) == 0

    def pop(self, index=None):
        if index and int(index) not in range(self.__len__()) :
            raise Exception("Index does not exist")
        elif not self.is_empty:
            raise Exception("Stack is empty")
        elif index:
            return self.stack.pop(index)
        else:
            return self.stack.pop()
    def push(self, ele):
        self.stack.append(ele)

stack_obj = stack()
stack_obj.push(2)
stack_obj.push(6)
stack_obj.push(3)
stack_obj.push("lewis")
print (stack_obj.stack_contents())
print (stack_obj.pop(1))
print (stack_obj.stack_contents())
print (stack_obj.pop())
print (stack_obj.stack_contents())
