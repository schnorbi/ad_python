class Stack():
    def __init__(self):
        self.__stack = []

    def push(self, e):
        self.__stack.append(e)

    def pop(self):
        if bool(self.__stack):
            return self.__stack.pop()

    def top(self):
        if bool(self.__stack):
            return self.__stack[-1]

    def is_empty(self):
        return not (bool(self.__stack))


#Testcases
s = Stack()
print(s.is_empty())

s = Stack()
s.push("Element")
_ = s.pop()
print(s.is_empty())

s = Stack()
e = 42
s.push(e)
f = s.top()
print(f == e)

s = Stack()
e = 42
s.push(e)
f = s.pop()
print(f == e + 1)