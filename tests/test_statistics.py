import pytest
from dflow.array import dfarray


dataset = dfarray(1, 3, 3, 2, 1.5, -2)


# mean test
def test_MeanTest():
    assert dataset.mean == 1.4166666666666667

# median test
def test_MedianTest():
    assert dataset.median == 1.75

# mode test
def test_ModeTest():
    assert dataset.mode[0] == 3