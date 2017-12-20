class ReverseIterator:

    def __init__(self, data):
        self.__data = data
        self.__index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index == 0:
            raise StopIteration
        self.__index -= 1
        return self.__data[self.__index]

if __name__ == '__main__':
    for c in ReverseIterator('abc'):
        print(c)
