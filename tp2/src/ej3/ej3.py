from __future__ import division
from math import log, sqrt
import math

N = 500
espR = lambda a, x, j :  a + (x - a) / (j+1)
varR = lambda a, x, j, y: (1 - 1 / j) * a + (j+1) * pow(x - y, 2) if (j > 0) else 0
values = [ x.strip() for x in open("ganancia-ins-500.dat")]

if __name__ == "__main__":

    # EMV Normal
    esp = 0
    var = 0
    pEsp = 0
    pVar = 0
    for i in range(N):
        esp = espR(pEsp, float(values[i]), i)
        var = varR(pVar, esp, i, pEsp)
        pEsp = esp
        pVar = var
    s = math.sqrt(var)
    print "EMV media: %s\nEMV sigma: %s\n" % (esp, s)
    

    # EMV LogNormal
    esp = 0
    var = 0
    pEsp = 0
    pVar = 0
    for i in range(N):
        esp = espR(pEsp, log(float(values[i])), i)
        var = varR(pVar, esp, i, pEsp)
        pEsp = esp
        pVar = var
    s = sqrt(var)
    print "EMV media: %s\nEMV sigma: %s\n" % (esp, s)

    # EMV LogNormal
    espLogNormal = esp
    esp = 0
    var = 0
    pEsp = 0
    pVar = 0
    for i in range(N):
        esp = espR(pEsp, float(values[i]), i)
        var = varR(pVar, esp, i, pEsp)
        pEsp = esp
        pVar = var
    A = log(esp) - espLogNormal
    alpha = (1/(4*A)) * ( 1 + sqrt(1 + 4/3 * A))
    lambd = alpha/esp
    print "EMV alpha: %s\nEMV lambda: %s\n" % (alpha, lambd)

