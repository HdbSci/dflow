# DFLOW LIBRARY:
#  dflow arrays module
# with dfarray class and
# linspace function

from dflow.utils import *


# dfarray #
class dfarray:
    def __init__(self, value):
        self.value = []
        for v in value:
            self.value.append(v)

    def __repr__(self):
        return "dflow array with value {}".format(self.value)

    def __str__(self):
        return "dflow array with value {}".format(self.value)

    def __add__(self, other):
        arr = self.value.copy()
        for v in other.value:
            arr.append(v)
        return dfarray(arr)

    def __IADD__(self, other):
        self.value.expand(other.value)

    def __lshift__(self, data):
        self.append(data)

    def __rshift__(self, num):
        data = []
        for n in range(0, num):
            data.append(self.delete(0))
        return dfarray(data)

    def __matmul__(self, other):
        return sum(x*y for x, y in zip(self.value, other.value))

    def at(self, index: int):
        try:
            return self.value[index - 1]
        except IndexError:
            return None

    def assign(self, index: int, value):
    	self.value[index] = value

    def append(self, data):
        self.value.append(data)

    def delete(self, index):
        return self.value.pop(index - 1)

    @property
    def iter(self):
        return self.value.copy()

    @property
    def length(self):
    	return len(self.value)

    @property
    def sort(self):
        self.value = sorted(self.value)

    @property
    def reverse(self):
        self.value = self.value[::-1]

    def aply(self, f=lambda x: x):
        V = self.value.copy()
        self.value = []
        for v in V:
            self.value.append(f(v))

    @property
    def clean(self):
        V = []
        for v in self.value:
            if v not in V:
                V.append(v)
            else:
                pass
        self.value = V.copy()

    @property
    def copy(self):
        return dfarray(self.value.copy())

    def plot(self, aply=lambda x: x):
        import matplotlib.pyplot as plt
        V = []
        for v in self.value:
            V.append(aply(v))
        plt.plot(V)
        plt.show()

    @property
    def list(self):
        return self.value.copy()

def add(x, y):   # add elements of 2 dfarray
    X = x.list
    Y = y.list
    res = dfarray([])
    for i, j in zip(X, Y):
        res << i + j
    return res

def sub(x, y):   # substract elements of 2 dfarray
    X = x.list
    Y = y.list
    res = dfarray([])
    for i, j in zip(X, Y):
        res << i - j
    return res

def mul(x, y):   # multiply elements of 2 dfarray
    X = x.list
    Y = y.list
    res = dfarray([])
    for i, j in zip(X, Y):
        res << i * j
    return res

def div(x, y):   # divide elements of 2 dfarray
    X = x.list
    Y = y.list
    res = dfarray([])
    for i, j in zip(X, Y):
        res << i / j
    return res


# linspace #
def linspace(_from, _to, _nums):
    return dfarray(range(_from, _to, _nums / (_to - _from)))
