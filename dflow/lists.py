# DFLOW LIBRARY:
#  dflow array (list)
# initialization functions
# module with linspace,
# arange, randlist...

from dflow.array import dfarray
from dflow.utils import range

import random as rd


# linspace #
def linspace(_from, _to, _nums):
    lst = range(_from, _to, (_to - _from) / _nums)
    return dfarray(*lst)


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
def arange(_from, _to, step=1):
    return dfarray(*range(_from, _to, step))


# randlist #
def randlist(*args):
    res = dfarray()
    for i in range(0, sum(args)):
        res << rd.random()
    return res