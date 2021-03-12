# DFLOW LIBRARY:
#  dflow arrays module
# with dfarray class and
# linspace function

from dflow.utils import *
from dflow.error import *


# dfarray #
class dfarray:
    def __init__(self, *args):
        self.value = []
        for v in args:
            if type(v) != int and type(v) != float:
                raise dfArrayError("dfarray type error: dfarray objects must contain numbers")
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
        if type(data) != int and type(data) != float:
            raise dfArrayError("dfarray type error: dfarray objects must contain numbers")
        self.value.append(data)

    def __rshift__(self, num):
        data = []
        for n in range(0, num):
            data.append(self.value.pop(-1))
        return dfarray(data)

    def __matmul__(self, other):
        return sum(x*y for x, y in zip(self.value, other.value))

    def __getitem__(self, key):
        try:
            return self.value[key - 1]
        except IndexError:
            return None

    def __setitem__(self, key, value):
        self.value[key - 1] = value

    def __delitem__(self, key):
        return self.value.pop(key - 1)

    def __contains__(self, item):
        if item in self.value:
            return True
        else:
            return False

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
    def sum(self):
        return sum(self.value)

    @property
    def mean(self):
        return self.sum / self.length

    @property
    def median(self):
        d = self.copy
        d.sort
        if d.length % 2 == 0:
            return dfarray([int(d.value[d.length/2]), int(d.value[d.length/2+1])]).mean
        else:
            return d.values[int(d.length/2)]

    @property
    def mode(self):
        data = {}
        vals = self.value.copy()
        maximum = [None, 0]

        for d in vals:
            try:
                data[d] += 1
            except Exception:
                data[d] = 1 

        for d in data:
            if max(maximum[1], data[d]) == data[d]:
                maximum = [d, data[d]]
            else: pass
            return maximum[0]

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
        return dfarray(*self.value.copy())

    def plot(self, title='dflow array graph'):
        import matplotlib.pyplot as plt
        plt.plot(self.value)
        plt.title(title)
        plt.show()

    @property
    def list(self):
        return self.value.copy()

def add(x, y):   # add elements of 2 dfarray
    X = x.list
    Y = y.list
    res = dfarray()
    for i, j in zip(X, Y):
        res << i + j
    return res

def sub(x, y):   # substract elements of 2 dfarray
    X = x.list
    Y = y.list
    res = dfarray()
    for i, j in zip(X, Y):
        res << i - j
    return res

def mul(x, y):   # multiply elements of 2 dfarray
    X = x.list
    Y = y.list
    res = dfarray()
    for i, j in zip(X, Y):
        res << i * j
    return res

def div(x, y):   # divide elements of 2 dfarray
    X = x.list
    Y = y.list
    res = dfarray()
    for i, j in zip(X, Y):
        res << i / j
    return res


# linspace #
def linspace(_from, _to, _nums):
    return dfarray(*range(_from, _to, _nums / (_to - _from)))


# zeros & ones #
def zeros(num):
    res = dfarray()
    for i in range(0, num):
        res << 0
    return res

def ones(num):
    res = dfarray()
    for i in range(0, num):
        res << 1
    return res


# arange #
def arange(_to):
    return dfarray(range(0, _to))

def arange(_from, _to, step=1):
    return dfarray(range(_from, _to, step))