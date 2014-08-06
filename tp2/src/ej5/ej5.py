import numpy as np
import math
import matplotlib.pyplot as plt
import pylab as P
import scipy.stats as stats


N = 500
espR = lambda a, x, j :  a + (x - a) / (j+1)
varR = lambda a, x, j, y: (1 - 1 / j) * a + (j+1) * pow(x - y, 2) if (j > 0) else 0
values = [ float(x.strip()) for x in open("ganancia_media.dat")]
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

def kolmogorov_smirnov_normal(muestra, dist):
    muestra.sort()
    n = len(muestra)

    # Calcular el estadístico D:
    d1 = max([float(j+1)/float(n) - dist.cdf(muestra[j]) for j in xrange(0, n)])
    d2 = max([dist.cdf(muestra[j]) - (float(j+1)-1.0)/float(n) for j in xrange(0, n)])
    d = max(d1, d2)

    # Calcular el valor p.
    p = 0
    r = 100
    for _ in xrange(r):
        v = dist.rvs(n)
        v.sort()
        Xsim, S2sim = np.mean(values), np.std(values)
        distSim = stats.norm(loc=Xsim, scale=numpy.sqrt(S2sim))
        D1 = max([float(j+1)/float(n) - distSim.cdf(v[j]) for j in xrange(0, n)])
        D2 = max([distSim.cdf(v[j]) - (float(j+1)-1.0)/float(n) for j in xrange(0, n)])
        D = max(D1, D2)
        if D >= d:
            p += 1

    return float(p) / float(r)
                                                                                                                                

if __name__ == "__main__":
    bins = np.arange(int(min(values)), int(max(values))+1, 0.1)
    plt.hist(values, bins=bins, normed=1, width=0.017)
    plt.xticks(bins, rotation='vertical')
    
    d = stats.norm(loc=esp-0.05, scale=np.std(values))
    bins = np.linspace(int(min(values)), int(max(values))+1, 200)
    plt.plot(bins, d.pdf(bins), color='red', linewidth=2.0)
    
    plt.ylabel("Probabilidad")
    plt.xlabel("Valores")
    plt.title("Comparativa")

    plt.show()


"""
def graficar_normal(v):
    X, S2 = esp, s

    fig = plt.figure()
    width = 0.35
    bins = [i for i in xrange(int(min(v)), int(max(v)) + 1)]
    plt.hist(v, bins=bins, rwidth=width, align='right', normed=True, 
    label=u'Valores simulados', color='blue', histtype='bar')

    x = np.linspace(min(v),max(v),200)
    dist = stats.norm(loc=X, scale=S2)
    plt.plot(x, dist.pdf(x), color='red', label=u'Ajuste normal', 
        linewidth=2.0)

    plt.ylim(0, 0.15)
    plt.legend()
    plt.title(u'Ajuste Normal')
    plt.xlabel(u'Datos semanales')
    plt.ylabel(u'Frecuencia Relativa')
    plt.show()

    print "p-valor: %f" % kolmogorov_smirnov_normal(v, dist)
"""
