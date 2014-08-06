# -*- coding: utf-8 -*-
import math
import random
import pylab
import numpy
from scipy import stats


def parametros_normal(v):
	X = math.fsum(v) / float(len(v))
	X2 = math.fsum(map(lambda x:x ** 2.0, v)) / float(len(v))
	S2 = X2 - X ** 2.0
	return X, S2

def graficar_histograma(v):
	lbins = [364.8, 364.9, 365.0, 365.1, 365.2, 365.3, 365.4, 365.5,
         365.6, 365.7, 365.8, 365.9, 366.0, 366.1, 366.2, 366.3]
	bins = zip(lbins[:-1],lbins[1:]) + [(366.3, 366.4)]

	hist, bin_edges = numpy.histogram(v, bins=lbins + [366.4])
	pylab.bar((bin_edges-0.025)[:-1], hist*0.1, color='blue', width=0.05, label=u'Valores simulados')
	
	pylab.hist(v, bins=100,normed=1)    
	X, S2 = parametros_normal(v)
	dist = stats.norm(loc=365.6, scale=numpy.sqrt(0.04))
	pylab.plot(bin_edges, dist.cdf(bin_edges+0.1) - dist.cdf(bin_edges), color='red', label=u'Ajuste normal', 
		linewidth=2.0)

	#pylab.ylim(0, 0.25)
	pylab.title(u'Ganancia media semanal')
	pylab.xlabel(u'Datos')
	pylab.ylabel(u'Frecuencia Relativa')
	pylab.show()


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
        Xsim, S2sim = parametros_normal(v)
        distSim = stats.norm(loc=Xsim, scale=numpy.sqrt(S2sim))
        D1 = max([float(j+1)/float(n) - distSim.cdf(v[j]) for j in xrange(0, n)])
        D2 = max([distSim.cdf(v[j]) - (float(j+1)-1.0)/float(n) for j in xrange(0, n)])
        D = max(D1, D2)
        if D >= d:
            p += 1

    return float(p) / float(r)

# Leer datos:
filename = "ganancia_media.dat"

f = open(filename, 'r')
v = []

for line in f:
	v.append(float(line))

#graficar_normal(v)
graficar_histograma(v)