import pytest
from dflow import lists


# linspace test
def test_LinspaceTest():
    a = lists.linspace(0, 10, 10)
    assert a.length == 10

# zeros and ones test
def test_ZerosAndOnes():
    a = lists.zeros(1000)
    A = a.copy

    a.aply(lambda x: x**2)

    assert a.list == A.list

    a = lists.ones(1000)
    A = a.copy

    a.aply(lambda x: x**2)

    assert a.list == A.list

# arange test
def test_ArangeTest():
    a = lists.arange(_from=0, _to=10, step=1)
    assert a.length == 10

# randlist test
def test_RandlistTest():
    a = lists.randlist(1, 2, 4)
    assert a.length == 7