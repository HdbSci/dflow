# DFLOW LIBRARY:
#  dflow dataframes module
# with dfdataframe class and
# asCSV function

from dflow import utils


# dfdataframe #
class dfdataframe:
    def __init__(self, rows=['hello'], columns=['a'], data=[[1]]):
        self.rows={}
        self.columns=utils.dictenumerate(columns)

        for r, d in zip(rows, data):
            self.rows[r] = d

    def at(self, row, column):
        return self.rows[row][self.columns[column]]

    def assign(self, row, column, value):
        self.rows[row][self.columns[column]] = value