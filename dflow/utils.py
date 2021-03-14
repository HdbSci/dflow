# DFLOW LIBRARY:
#  dflow utilities module
# with new range function
# and dictenumerate

def range(_from, _to, step=1):
    out = []
    aux = _from
    while aux < _to:
        out.append(aux)
        aux += step
    return out

def dictenumerate(d):
    return {k: v for v, k in enumerate(d)}

def prod(x):
    res = 1
    for X in x:
        res *= X
    return res