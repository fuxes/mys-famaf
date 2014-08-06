import random
import math
from math import floor, log
import matplotlib.pyplot as plt
import scipy
import numpy as np

P = 0.4
Q = 1 - P
L = 12

def geometric(p):
    u = random.random()
    x = floor(log(u)/float(log(1-p))) + 1
    return int(x)
    
def norm(xs, n):
    for i in range(len(xs)):
        xs[i] = xs[i]/float(n)

if __name__ == "__main__":
    a = [0 for _ in range(16)]
    for _ in range(100):
        a[min(geometric(P), L)] += 1
    norm(a, 100)

    b = [0 for _ in range(16)]
    for _ in range(1000):
        b[min(geometric(P), L)] += 1
    norm(b, 1000)

    c = [0 for _ in range(16)]
    for _ in range(10000):
        c[min(geometric(P), L)] += 1
    norm(c, 10000)

    a = a[1:]
    b = b[1:]
    c = c[1:]
    
    # a = [int(x.strip()) for x in open("100.txt", "r")]
    # b = [int(x.strip()) for x in open("1000.txt", "r")]
    # c = [int(x.strip()) for x in open("10000.txt", "r")]
    
    params = dict(normed=1, bins=100, alpha=0.5,range=(0,15), histtype='bar')

    g = [P * pow(Q,i-1) for i in range(1,16)]
    print g
    bins = np.arange(15)
    w = 0.15
    plt.bar(bins, g, w, color='r')
    plt.bar(bins+w, c, w, color='b')
    plt.bar(bins+2*w, b,w, color='g')
    plt.bar(bins+3*w, a, w, color='y')

    plt.title("Histograma comparativo entre simulaciones y distribucion teorica")
    plt.ylabel("Frecuencia relativa")
    plt.xlabel("Valores")
    plt.legend((u'Distribucion teorica', "10000 Simulaciones", "1000 Simulaciones", "100 Simulaciones"))



    plt.show()
