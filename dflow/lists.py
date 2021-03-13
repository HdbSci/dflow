# DFLOW LIBRARY:
#  dflow array (list)
# initialization functions
# module with linspace,
# arange, randlist...

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


# randlist #
def randlist(*args):
    res = dfarray()
    for i in range(sum(args)):
        res << rd.random()
    return res