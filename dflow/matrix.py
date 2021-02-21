# DFLOW LIBRARY:
#  dflow matrices module
# with dfmatrix class

from dflow.array import dfarray


# dfmatrix #
class dfmatrix:
    def __init__(self, mat):
        self.value = dfarray([])
        for m in mat:
            self.value << dfarray(m)

    def __matmul__(self, other):
        x = self.list
        y = self.list
        # TODO: Write matrix multiplication

    def row(self, index):
        return self.value.at(index)

    @property
    def list(self):
        res = []
        for l in self.value.iter:
            res.append(l.list)
        return res

    @property
    def iter(self):
        res = []
        for l in self.value.iter:
            res.append(l.list)
        return res

    @property
    def dimension(self):
        res = 0
        for r in self.value.iter:
            for c in r.iter:
                res += 1
        return res

    @property
    def copy(self):
        return dfmatrix(self.list.copy())

    def aply(self, f=lambda x: x):
        for r in self.value.iter:
            r.aply(f)