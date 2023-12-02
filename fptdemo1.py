# first-form fixed point iteration for f(x) = x^2 - 1/2
#
import math
import sys

# set tolerance to machine precision
tolerance = sys.float_info.epsilon

k = 0
x_k = 0.7071

# guaranteed interval of convergence: epsilon <= x_0 <= 1-epsilon
# (both conditions of FPT are satisfied within this interval)

# iterate until F-test satisfied
while abs(x_k**2 - 0.5) > tolerance:
    print (k, x_k)
    x_k = x_k - x_k**2 + 0.5
    k = k + 1

print ("fixed point within F-test tolerance:", k, x_k)
