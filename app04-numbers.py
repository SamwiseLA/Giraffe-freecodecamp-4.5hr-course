from math import *

def pf(a, n):
    n = n + 1
    print("result " + str(n) + ": "+ str(a))
    print("=================")
    return n

n = 0

print("<<<<<==============>>>>>")

n=pf(2,n)
n=pf(23.4532000,n)
n=pf(23.45320001,n)
n=pf(-23.45320001,n)
n=pf(3 + 4.5,n)
n=pf(3 * 4.5,n)
n=pf(3 * 4.5 + 5,n)
n=pf(5 + 3 * 4.5,n)
n=pf((5 + 3) * 4.5,n)
n=pf((5 + 3) * -4.5,n)
n=pf(abs((5 + 3) * -4.5),n)

n=pf(pow(5,3),n)

# From Math i mport
n=pf(floor(5.7),n)
n=pf(ceil(5.7),n)
n=pf(sqrt(144),n)



