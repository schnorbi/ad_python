class PQueue():
    def __init__(self):
        self.__data = []

    def insert(self, v):
        self.__data.append(v)
        self.__data.sort(reverse=True)

    def remove_largest(self):
        if bool(self.__data):
            return self.__data.pop(0)

    def largest(self):
        if bool(self.__data):
            return self.__data[0]

    def is_empty(self):
        return not (bool(self.__data))

#Testcases
q = PQueue()
q.insert(23)
q.insert(42)
q.insert(-3)
e = q.remove_largest()
print(e)

q = PQueue()
q.insert(42)
_ = q.remove_largest()
print(q.is_empty())

q = PQueue()
print(q.is_empty())