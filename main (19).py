import numpy

class Numpy():
    def __init__(self, a):
        self.a = a
    
    def find_transpose(self):
        print(numpy.transpose(a))
    
    def find_flatten(self):
        print(a.flatten())

if __name__ == '__main__':
    row, colunm = map(int, input().split())
    a = numpy.array([input().split() for _ in range(row)], int)
    my_object = Numpy(a)
    my_object.find_transpose()
    my_object.find_flatten()