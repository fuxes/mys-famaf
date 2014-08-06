import random
import math
from math import floor, log
import matplotlib.pyplot as plt
import scipy
import numpy as np

P = 0.4
Q = 0.6
L = 12

def geometric(q):
    u = random.random()
    x = floor(log(u)/float(log(q))) + 1
    return int(x)
    
def norm(xs, n):
    for i in range(L):
        xs[i] = xs[i]/float(n)

if __name__ == "__main__":
    a = [0 for _ in range(L+1)]
    for _ in range(100):
        a[min(geometric(Q), L)] += 1
    norm(a, 100)

    b = [0 for _ in range(L+1)]
    for _ in range(1000):
        b[min(geometric(Q), L)] += 1
    norm(b, 1000)
    
    c = [0 for _ in range(L+1)]
    for _ in range(10000):
        c[min(geometric(Q), L)] += 1
    norm(c, 10000)

    gpuntual = [P * pow(Q,i-1) for i in range(L+1)]
    
    print a
    print b
    print c
    print gpuntual

    params = dict(normed=True, alpha=0.5,range=(0,15))
    plt.hist((a,b,c,gpuntual), **params)
    plt.show()
