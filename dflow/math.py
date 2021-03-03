# DFLOW LIBRARY:
#  dflow math module
# with functions like
# sin, cos, exp... and
# consts like e or pi

# constants #
π = 3.1415926535
pi = π

φ = 1.6180339887
phi = φ

e = 2.7182818284


# functions #
sinh = lambda x: e**x - e**-x
cosh = lambda x: e**x + e**-x

tanh = lambda x: sinh(x) / cosh(x)