# DFLOW LIBRARY:
#  dflow arrays module
# with dfarray class

import utils


# dfarray #
class dfarray:
    def __init__(self, value):
        self.value = []
        for v in value:
            self.value.append(v)

    def __repr__(self):
        return "dflow array with value {self.value}".format()

    def __str__(self):
        return "dflow array with value {self.value}".format()

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

    def append(self, data):
        self.value.append(data)

    def delete(self, index):
        return self.value.pop(index - 1)

    @property
    def iter(self):
        return self.value.copy()

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