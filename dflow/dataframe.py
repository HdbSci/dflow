# DFLOW LIBRARY:
#  dflow dataframes module
# with dfdataframe class and
# asCSV function

from dflow import utils
from dflow import array


# dfdataframe #
class dfdataframe:
    def __init__(self, rows=['hello'], columns=['a'], data=[[1]]):
        self.rows={}
        self.columns=utils.dictenumerate(columns)

        for r, d in zip(rows, data):
            self.rows[r] = array.dfarray(d)

    def __repr__(self):
        return "dflow data frame object"

    def __str__(self):
        return "dflow data frame object"

    def at(self, row, column):
        return self.rows[row][self.columns[column]]

    def assign(self, row, column, value):
        self.rows[row].assign(self.columns[column], value)

    def row(self, name):
    	return self.rows[name]