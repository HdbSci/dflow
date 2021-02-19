import pytest
from dflow import array


A = array.dfarray([3, 2, 4, 1])


# __str__ test
def test_StrTest():
	assert str(A) == 'dflow array with value [3, 2, 4, 1]'

# copy test
def test_CopyTest():
	assert str(A.copy) == str(A)

# sort test
def test_SortTest():
	B = A.copy
	B.sort
	assert B.value == [1, 2, 3, 4]
