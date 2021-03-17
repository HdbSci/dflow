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

    def __getitem__(self, *loc):
        return self.value[loc[0]][loc[1]]

    def __setitem__(self, *loc):
        self.value[loc[0]][loc[1]] = loc[2]

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
    def rows(self):
        return self.value.length

    @property
    def iter(self):
        res = []
        for l in self.value.iter:
            res.append(l.list)
        return res

    @property
    def shape(self):
        return [self.value.length, self.value[1].length]

    @property
    def copy(self):
        return dfmatrix(self.list.copy())

    def aply(self, f=lambda x: x):
        for r in self.value.iter:
            r.aply(f)