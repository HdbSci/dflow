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
# Visit https://en.wikipedia.org/wiki/Taylor_series for
# more information about Taylor series and aproximations
# of sin, cos, tan, exp, log...
sin = lambda x: sum([((-1)**n)/(fact(2*n+1))*(x**(2*n+1)) for n in range(100)])
cos = lambda x: sum([((-1)**n)/(fact(2*n))*(x**(2*n)) for n in range(100)])

sinh = lambda x: e**x - e**-x
cosh = lambda x: e**x + e**-x

tanh = lambda x: sinh(x) / cosh(x)